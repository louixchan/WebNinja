import os
import platform
import re
import subprocess
import sys
import time
import datetime
from bs4 import BeautifulSoup

try:
    from cefpython3 import cefpython as cef
except:
    print("[WebNinja] Error: WebNinja needs CEFPYTHON module for web scraping. "
        " To install type: pip install cefpython3")
    sys.exit(1)

try:
    import pandas
except:
    print("[WebNinja] Error: WebNinja needs PANDAS module for reading your URL csv files. "
        " To install type: pip install pandas")
    sys.exit(1)

try:
    from PIL import Image, PILLOW_VERSION, ImageDraw, ImageFont
except:
    print("[WebNinja] Error: WebNinja needs PILLOW module for exporting screenshots. "
        "To install type: pip install Pillow")
    sys.exit(1)
#
# try:
#     from weasyprint import HTML, CSS
# except:
#     print("[WebNinja] Error: WebNinja needs WEASYPRINT module for exporting PDFs. "
#         "To install type: pip install weasyprint")
#     sys.exit(1)


# Config
# URL = "https://github.com/cztomczak/cefpython"
URL = ""
CURRENT_ID = 0
URLs = None
URL_COUNT = 0
VIEWPORT_SIZE = (1024, 5000)
# SCREENSHOT_BASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
#                                "screenshot.png")
EXPORT_BASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "export/")
EXPORT_NAME = ""
EXPORT_SCREENSHOT_PATH = ""
EXPORT_HTML_PATH = ""
EXPORT_PDF_PATH = ""
EXPORT_PDF = False
EXPORT_HTML = False
EXPORT_SCREENSHOT = False
EXPORT_DOWNLOAD = False
ERROR = False
RETRY_LIMIT = 5
RETRY_ATTEMPT = 0

MODE = "TEST"


def main():

    print("WebNinja.py is an archived version of the original single thread WebNinja.")
    print("Please refer to WebNinjaBrowserHandler.py for multi-thread version.")

    global URLs
    global URL
    global EXPORT_BASE_PATH
    global EXPORT_PDF
    global EXPORT_HTML
    global EXPORT_SCREENSHOT
    global EXPORT_DOWNLOAD

    check_versions()

    if len(sys.argv) == 1:

        print("[WebNinja] Error: Not option specified. To see all options, "
            "type: python3 WebNinja.py -man")
        sys.exit(1)

    if sys.argv[1] == "-man":

        manual()
        sys.exit(1)

    else:

        argvId = 1

        if (sys.argv[argvId] == "-test"):

            sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
            cef.Initialize(settings={"windowless_rendering_enabled": True})

            # parentWindowHandle = 0

            windowInfo = cef.WindowInfo()
            # windowInfo.SetAsOffscreen(parentWindowHandle)

            browser = cef.CreateBrowserSync(
                window_info=windowInfo,
                url="www.google.com"
            )

            # browser.SetClientHandler(LoadHandler())
            # browser.SetClientHandler(RenderHandler())

            browser.SendFocusEvent(True)
            # You must call WasResized at least once to let know CEF that
            # viewport size is available and that OnPaint may be called.
            browser.WasResized()

            cef.MessageLoop()

        else:

            while argvId < len(sys.argv):

                if sys.argv[argvId] == "-s":

                    URLs = pandas.DataFrame([{"name" : "target", "url" : sys.argv[argvId + 1]}])

                elif sys.argv[argvId] == "-m":

                    try:
                        URLs = pandas.read_csv(sys.argv[argvId + 1], None, names = ["name", "url"], engine="python")
                    except:
                        print("[WebNinja] Error: Invalid file path. To see other options, type: python3 WebNinja.py -man")

                elif sys.argv[argvId] == "-e":

                    EXPORT_BASE_PATH = sys.argv[argvId + 1]

                elif sys.argv[argvId] == "-html":

                    EXPORT_HTML = sys.argv[argvId + 1] == "T"

                elif sys.argv[argvId] == "-pdf":

                    EXPORT_PDF = sys.argv[argvId + 1] == "T"

                elif sys.argv[argvId] == "-ss":

                    EXPORT_SCREENSHOT = sys.argv[argvId + 1] == "T"

                elif sys.argv[argvId] == "-dl":

                    EXPORT_DOWNLOAD = sys.argv[argvId + 1] == "T"

                else:

                    print("[WebNinja] Error: Option %s not recognised. To see all options, "
                        "type: python3 WebNinja.py -man" % sys.argv[argvId])
                    sys.exit(1)

                argvId = argvId + 2

            if (argvId != len(sys.argv)):

                print("[WebNinja] Error: Option %s has a missing specifier. To see all option, "
                    "type: python3 WebNinja.py -man" % sys.argv[argvId - 2])
                sys.exit(1)

    if not os.path.exists(EXPORT_BASE_PATH):
        os.makedirs(EXPORT_BASE_PATH)

    startBrowsing()

    # for id, row in URLs:

    #     URL = row["url"]

       #  sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
       #  cef.Initialize(settings={"windowless_rendering_enabled": True})
       #  window_info = cef.WindowInfo()
       #  window_info.SetAsOffscreen(0)
       #  browser = cef.CreateBrowserSync(
       #      window_info = window_info,
       #      url=URL, 
       #      window_title="Hello World!")
       #  # create_browser()
       #  handler = LoadHandler()
       #  browser.SetClientHandler(LoadHandler())

       #  cef.MessageLoop()

    # exit_app()

def checkDependencies():

    try:
        __import__("cefpython3")
    except ImportError:
        print("[WebNinja] Error: WebNinja needs CEFPYTHON module for web scraping. "
              " To install type: pip install cefpython3")
        sys.exit(1)

    try:
        __import__("pandas")
    except ImportError:
        print("[WebNinja] Error: WebNinja needs PANDAS module for reading your URL csv files. "
              " To install type: pip install pandas")
        sys.exit(1)

    try:
        __import__("PIL")
    except ImportError:
        print("[WebNinja] Error: WebNinja needs PILLOW module for exporting screenshots. "
              "To install type: pip install Pillow")
        sys.exit(1)

    # try:
    #     __import__("weasyprint")
    # except ImportError:
    #     print("[WebNinja] Error: WebNinja needs WEASYPRINT module for exporting PDFs. "
    #           "To install type: pip install weasyprint")
    #     sys.exit(1)

    print("All dependencies satisfied...")


def manual():

    print("[WebNinja] DOCUMENTATION:")
    print("NAME")
    print("    python3 WebNinja.py -man")
    print()
    print("DESCRIPTION")
    print("    Open manual page.")
    print()
    print("NAME")
    print("    python3 WebNinja.py -s [link] -e [export link] -html [HTML flag] -pdf [PDF flag] -ss [screenshot flag]")
    print()
    print("DESCRIPTION")
    print("    Crawl the link specified.")
    print()
    print("    [link]:          Link of the webpage to be crawled.")
    print("    [export link]:   Directory for any export file.")
    print("    [HTML]:          T for exporting HTML source code of the webpage, F otherwise. (Default: T)")
    print("    [PDF]:           T for exporting PDF of the unstyled webpage, F otherwise. (Default: T)")
    print("    [screenshot]:    T for exporting screenshot of the webpage, F otherwise. (Default: T)")
    print()
    print("NAME")
    print("    python3 WebNinja.py -m [file link] -e [export link] -html [HTML flag] -pdf [PDF flag] -ss [screenshot flag]")
    print()
    print("DESCRIPTION")
    print("    Crawl the link in the file specified by the argument [file link]. The file must be ")
    print("    stored as a csv format with the first column containing the name for export file, ")
    print("    and the second column containing the link to the webpage.")
    print()
    print("    [file link]:     Link to the input file.")
    print("    [export link]:   Directory for any export file.")
    print("    [HTML]:          T for exporting HTML source code of the webpage, F otherwise. (Default: T)")
    print("    [PDF]:           T for exporting PDF of the unstyled webpage, F otherwise. (Default: T)")
    print("    [screenshot]:    T for exporting screenshot of the webpage, F otherwise. (Default: T)")
    print()


def check_versions():
    print("[WebNinja] CEF Python {ver}".format(ver=cef.__version__))
    print("[WebNinja] Python {ver} {arch}".format(
          ver=platform.python_version(), arch=platform.architecture()[0]))
    assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"


def startTestBrowsing():

    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize(settings={"windowless_rendering_enabled": True})

    # parentWindowHandle = 0

    windowInfo = cef.WindowInfo()
    # windowInfo.SetAsOffscreen(parentWindowHandle)

    browser = cef.CreateBrowserSync(
        window_info = windowInfo,
        url = "www.google.com"
        )

    # browser.SetClientHandler(LoadHandler())
    # browser.SetClientHandler(RenderHandler())

    browser.SendFocusEvent(True)
    # You must call WasResized at least once to let know CEF that
    # viewport size is available and that OnPaint may be called.
    browser.WasResized()

    cef.MessageLoop()

def testBrowseNext(browser, link):

    global MODE
    # input("Press Enter to continue...")
    MODE = "TEST2"
    browser.LoadUrl(link)

def startBrowsing():

    global URL
    global URLs
    global CURRENT_ID

    CURRENT_ID = 0
    URL = URLs.iloc[CURRENT_ID]["url"]

    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize(settings={"windowless_rendering_enabled": True, "downloads_enabled": True})

    parentWindowHandle = 0

    windowInfo = cef.WindowInfo()
    windowInfo.SetAsOffscreen(parentWindowHandle)

    browser = cef.CreateBrowserSync(
        window_info = windowInfo,
        url = URL
        )

    browser.SetClientHandler(LoadHandler())
    browser.SetClientHandler(RenderHandler())

    browser.SendFocusEvent(True)
    # You must call WasResized at least once to let know CEF that
    # viewport size is available and that OnPaint may be called.
    browser.WasResized()

    cef.MessageLoop()

def browseNext(browser):

    global CURRENT_ID, URL, URLs, EXPORT_NAME
    CURRENT_ID = CURRENT_ID + 1

    if CURRENT_ID >= len(URLs):
        print("[WebNinja] Message: All URLs have been browsed.")
        # time.sleep(5)
        cef.PostTask(cef.TID_UI, exit_app, browser)
        # exit_app()
    else:
        URL = URLs.iloc[CURRENT_ID]["url"]
        EXPORT_NAME = URLs.iloc[CURRENT_ID]["name"]
        print("[WebNinja] Message: Browsing %s." % URL)
        browser.LoadUrl(URL)


# def create_browser():
#     # Create browser in off-screen-rendering mode (windowless mode)
#     # by calling SetAsOffscreen method. In such mode parent window
#     # handle can be NULL (0).
#     parent_window_handle = 0
#     window_info = cef.WindowInfo()
#     window_info.SetAsOffscreen(parent_window_handle)
#     print("[screenshot.py] Viewport size: {size}"
#           .format(size=str(VIEWPORT_SIZE)))
#     print("[screenshot.py] Loading url: {url}"
#           .format(url=URL))
#     browser = cef.CreateBrowserSync(window_info=window_info,
#                                     url=URL)
#     browser.SetClientHandler(LoadHandler())
#     browser.SetClientHandler(RenderHandler())
#     browser.SendFocusEvent(True)
#     # You must call WasResized at least once to let know CEF that
#     # viewport size is available and that OnPaint may be called.
#     browser.WasResized()


def save_screenshot(browser):
    # Browser object provides GetUserData/SetUserData methods
    # for storing custom data associated with browser. The
    # "OnPaint.buffer_string" data is set in RenderHandler.OnPaint.
    global CURRENT_ID

    buffer_string = browser.GetUserData("OnPaint.buffer_string")
    if not buffer_string:
        raise Exception("buffer_string is empty, OnPaint never called?")
    image = Image.frombytes("RGBA", VIEWPORT_SIZE, buffer_string,
                            "raw", "RGBA", 0, 1)
    width, height = image.size

    draw = ImageDraw.Draw(image)
    text = "[WebNinja] Time Stamp: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    font = ImageFont.truetype('arial.ttf', 12)
    textwidth, textheight = draw.textsize(text, font)
    margin = 5
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text, font=font)

    image.save(EXPORT_BASE_PATH + str(URLs.iloc[CURRENT_ID]["name"]) + ".png", "PNG")
    print("[WebNinja] Saved image: {path}".format(path=EXPORT_BASE_PATH +
                                                       str(URLs.iloc[CURRENT_ID]["name"]
                                                           .encode("iso-8859-15", "replace")
                                                           .decode("iso-8859-15")) + ".png"))


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
    # browser.Destroy()
    cef.QuitMessageLoop()
    cef.Shutdown()

# def convertHtmlToPdf(sourceHtml, outputFilename):
#     # open output file for writing (truncated binary)
#     resultFile = open(outputFilename, "w+b")

#     # convert HTML to PDF
#     pisaStatus = pisa.CreatePDF(
#             sourceHtml,                # the HTML to convert
#             dest=resultFile)           # file handle to recieve result

#     # close output file
#     resultFile.close()                 # close output file

#     # return True on success and False on errors
#     return pisaStatus.err


class LoadHandler(object):

    # stringVisitor = None

    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Called when the loading state has changed."""
        # if not is_loading:
            # Loading is complete
            # sys.stdout.write(os.linesep)
            # print("WebNinja has loaded the webpage...")
            # time.sleep(0.3)
            # save_screenshot(browser)
        #     # See comments in exit_app() why PostTask must be used
        #     cef.PostTask(cef.TID_UI, exit_app, browser)
        # pass

    def OnLoadEnd(self, browser, frame, http_code):

        # print(http_code)
        if frame.IsMain():

            global MODE
            global EXPORT_NAME
            global ERROR
            self.stringVisitor = StringVisitor()
            self.stringVisitor.EXPORT_PATH = EXPORT_BASE_PATH + str(URLs.iloc[CURRENT_ID]["name"])\
                .encode("iso-8859-15", "replace").decode("iso-8859-15")

            if http_code == 200:
                global RETRY_ATTEMPT
                RETRY_ATTEMPT = 0
                # if MODE == "TEST":
                #     MODE = "TEST3"
                #     return
                #
                # elif MODE == "TEST2":
                #
                #     self.stringVisitor.EXPORT_PATH = EXPORT_BASE_PATH + "target"
                #     frame.GetSource(self.stringVisitor)
                #     return
                #
                # elif MODE == "TEST3":
                #     testBrowseNext(browser, "http://www.qichacha.com/firm_CN_f470d4e4d2bf1fc59650255443707461.html")
                #     return

                print("[WebNinja] Message: has loaded the website successfully...")

                if EXPORT_DOWNLOAD:
                    print("Downloading...")
                    browser.StartDownload(browser.GetUrl())

                else:
                    # print("Here!")
                    if EXPORT_HTML:
                        frame.GetSource(self.stringVisitor)

                    if EXPORT_SCREENSHOT:
                        save_screenshot(browser)
                # browser.Print()
                # frame.GetText(self.stringVisitor)
                # print(SV.value)

                browseNext(browser)

    def OnLoadError(self, browser, frame, error_code, error_text_out, failed_url):
        """Called when the resource load for a navigation fails
        or is canceled."""
        global ERROR
        if not frame.IsMain():
            # We are interested only in loading main url.
            # Ignore any errors during loading of other frames.
            return
        print("[WebNinja] ERROR: Failed to load url: {url}"
              .format(url=failed_url))
        print("[WebNinja] Error code: {code}"
              .format(code=error_code))
        print("[WebNinja] Error description: {text}"
              .format(text=error_text_out))
        # ERROR = True
        global RETRY_LIMIT
        global RETRY_ATTEMPT

        if RETRY_ATTEMPT < RETRY_LIMIT:
            print("[WebNinja] Message: Retrying to load url: {url}"
                  .format(url=failed_url))
            global CURRENT_ID
            CURRENT_ID = CURRENT_ID - 1
            RETRY_ATTEMPT = RETRY_ATTEMPT + 1
            browseNext(browser)
        # else:
            # See comments in exit_app() why PostTask must be used
            # cef.PostTask(cef.TID_UI, exit_app, browser)

# class Frame(object):

    # def GetSource(self, stringVisitor):

        # print("test")

class StringVisitor(object):

    def Visit(self, value):

        global CURRENT_ID, EXPORT_NAME

        # print(CURRENT_ID)
        # convertHtmlToPdf(value, "testing.pdf")
        # html = BeautifulSoup(value, "html.parser")
        # html.write_pdf('testing.pdf')

        if EXPORT_HTML:
            print("[WebNinja] Message: Working hard to export the HTML source code...")
            with open(self.EXPORT_PATH + ".html", "w+") as f:
                f.write(value)
                # f.write(html.prettify())

        # if EXPORT_PDF:
        #     print("[WebNinja] Message: Working hard to export PDF document...")
        #     html = HTML(string=value)
        #     html.write_pdf(self.EXPORT_PATH + ".pdf")

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
            sys.stdout.write("[WebNinja] OnPaint")
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