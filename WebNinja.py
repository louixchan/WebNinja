from cefpython3 import cefpython as cef
from weasyprint import HTML, CSS
import os
import pandas
import platform
import re
import subprocess
import sys
import time

try:
    from PIL import Image, PILLOW_VERSION
except:
    print("[screenshot.py] Error: PIL module not available. To install"
          " type: pip install Pillow")
    sys.exit(1)


# Config
# URL = "https://github.com/cztomczak/cefpython"
URL = ""
URLs = []
VIEWPORT_SIZE = (1024, 5000)
# SCREENSHOT_BASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
#                                "screenshot.png")
EXPORT_BASE_PATH = os.path.abspath(os.path.dirname(__file__))
EXPORT_PDF = True
EXPORT_HTML = True
EXPORT_SCREENSHOT = True


def main():

    check_versions()

    urlFileLink = sys.argv[1]

    with open(urlFileLink, "r") as file:

    	URLs = file.readlines()

    for url in URLs:

    	URL = url

	    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
	    cef.Initialize(settings={"windowless_rendering_enabled": True})
	    window_info = cef.WindowInfo()
	    window_info.SetAsOffscreen(0)
	    browser = cef.CreateBrowserSync(
	    	window_info = window_info,
	    	url=URL, 
	    	window_title="Hello World!")
	    # create_browser()
	    handler = LoadHandler()
	    browser.SetClientHandler(LoadHandler())

	    cef.MessageLoop()



def check_versions():
    print("[hello_world.py] CEF Python {ver}".format(ver=cef.__version__))
    print("[hello_world.py] Python {ver} {arch}".format(
          ver=platform.python_version(), arch=platform.architecture()[0]))
    assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"

def create_browser():
    # Create browser in off-screen-rendering mode (windowless mode)
    # by calling SetAsOffscreen method. In such mode parent window
    # handle can be NULL (0).
    parent_window_handle = 0
    window_info = cef.WindowInfo()
    window_info.SetAsOffscreen(parent_window_handle)
    print("[screenshot.py] Viewport size: {size}"
          .format(size=str(VIEWPORT_SIZE)))
    print("[screenshot.py] Loading url: {url}"
          .format(url=URL))
    browser = cef.CreateBrowserSync(window_info=window_info,
                                    url=URL)
    browser.SetClientHandler(LoadHandler())
    browser.SetClientHandler(RenderHandler())
    browser.SendFocusEvent(True)
    # You must call WasResized at least once to let know CEF that
    # viewport size is available and that OnPaint may be called.
    browser.WasResized()


def save_screenshot(browser):
    # Browser object provides GetUserData/SetUserData methods
    # for storing custom data associated with browser. The
    # "OnPaint.buffer_string" data is set in RenderHandler.OnPaint.
    buffer_string = browser.GetUserData("OnPaint.buffer_string")
    if not buffer_string:
        raise Exception("buffer_string is empty, OnPaint never called?")
    image = Image.frombytes("RGBA", VIEWPORT_SIZE, buffer_string,
                            "raw", "RGBA", 0, 1)
    image.save(SCREENSHOT_PATH, "PNG")
    print("[screenshot.py] Saved image: {path}".format(path=SCREENSHOT_PATH))


def open_with_default_application(path):
    if sys.platform.startswith("darwin"):
        subprocess.call(("open", path))
    elif os.name == "nt":
        # noinspection PyUnresolvedReferences
        os.startfile(path)
    elif os.name == "posix":
        subprocess.call(("xdg-open", path))


def exit_app(browser):
    # Important note:
    #   Do not close browser nor exit app from OnLoadingStateChange
    #   OnLoadError or OnPaint events. Closing browser during these
    #   events may result in unexpected behavior. Use cef.PostTask
    #   function to call exit_app from these events.
    print("[screenshot.py] Close browser and exit app")
    browser.CloseBrowser()
    cef.QuitMessageLoop()

def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err


class LoadHandler(object):

	# stringVisitor = None

    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Called when the loading state has changed."""
        # if not is_loading:
        #     # Loading is complete
        #     sys.stdout.write(os.linesep)
        #     print("[screenshot.py] Web page loading is complete")
        #     save_screenshot(browser)
        #     # See comments in exit_app() why PostTask must be used
        #     cef.PostTask(cef.TID_UI, exit_app, browser)
        pass

    def OnLoadEnd(self, browser, frame, http_code):

    	if frame.IsMain():
    		self.stringVisitor = StringVisitor()
	    	frame.GetSource(self.stringVisitor)
	    	# browser.Print()
	    	# frame.GetText(self.stringVisitor)
	    	# print(SV.value)

    def OnLoadError(self, browser, frame, error_code, failed_url, **_):
        """Called when the resource load for a navigation fails
        or is canceled."""
        if not frame.IsMain():
            # We are interested only in loading main url.
            # Ignore any errors during loading of other frames.
            return
        print("[screenshot.py] ERROR: Failed to load url: {url}"
              .format(url=failed_url))
        print("[screenshot.py] Error code: {code}"
              .format(code=error_code))
        # See comments in exit_app() why PostTask must be used
        cef.PostTask(cef.TID_UI, exit_app, browser)

# class Frame(object):

	# def GetSource(self, stringVisitor):

		# print("test")

class StringVisitor(object):

	def Visit(self, value):
		# convertHtmlToPdf(value, "testing.pdf")
		html = HTML(string=value)
		html.write_pdf('testing.pdf')
		return True

class RenderHandler(object):
    def __init__(self):
        self.OnPaint_called = False

    def GetViewRect(self, rect_out, **_):
        """Called to retrieve the view rectangle which is relative
        to screen coordinates. Return True if the rectangle was
        provided."""
        # rect_out --> [x, y, width, height]
        rect_out.extend([0, 0, VIEWPORT_SIZE[0], VIEWPORT_SIZE[1]])
        return True

    def OnPaint(self, browser, element_type, paint_buffer, **_):
        """Called when an element should be painted."""
        if self.OnPaint_called:
            sys.stdout.write(".")
            sys.stdout.flush()
        else:
            sys.stdout.write("[screenshot.py] OnPaint")
            self.OnPaint_called = True
        if element_type == cef.PET_VIEW:
            # Buffer string is a huge string, so for performance
            # reasons it would be better not to copy this string.
            # I think that Python makes a copy of that string when
            # passing it to SetUserData.
            buffer_string = paint_buffer.GetString(mode="rgba",
                                                   origin="top-left")
            # Browser object provides GetUserData/SetUserData methods
            # for storing custom data associated with browser.
            browser.SetUserData("OnPaint.buffer_string", buffer_string)
        else:
            raise Exception("Unsupported element_type in OnPaint")


if __name__ == '__main__':
    main()