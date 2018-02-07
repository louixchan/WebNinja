from cefpython3 import cefpython as cef
import sys
import time
from threading import Lock
from WebNinjaLoadHandler import LoadHandler

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

class WebNinjaBrowserHandler():

	browserCount = 0
	browsers = {}
	browserUrls = {}
	browserCurrentUrl = {}
	browserCurrentState = {}
	nextUrlId = 0
	URLS = []

	def __init__(self):

		self.browserCount = 0
		sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
		cef.Initialize(settings={"windowless_rendering_enabled": True, "downloads_enabled": True})

		self.urls = [
			'http://www.imdb.com/title/tt1571235',
			'http://www.imdb.com/title/tt1571242',
			'http://www.imdb.com/title/tt1571247',
			'http://www.imdb.com/title/tt1571249',
			'http://www.imdb.com/title/tt1571401',
			'http://www.imdb.com/title/tt1571402',
			'http://www.imdb.com/title/tt1571406',
			'http://www.imdb.com/title/tt1571407',
			'http://www.imdb.com/title/tt1571408',
			'http://www.imdb.com/title/tt1571409',
			'http://www.imdb.com/title/tt1571415',
			'http://www.imdb.com/title/tt1571416',
			'http://www.imdb.com/title/tt1571563',
			'http://www.imdb.com/title/tt1571565',
			'http://www.imdb.com/title/tt1571570',
			'http://www.imdb.com/title/tt1571574',
			'http://www.imdb.com/title/tt1571585',
			'http://www.imdb.com/title/tt1571588',
			'http://www.imdb.com/title/tt1571599',
			'http://www.imdb.com/title/tt1571724',
			'http://www.imdb.com/title/tt1571729',
			'http://www.imdb.com/title/tt1571730',
			'http://www.imdb.com/title/tt1571737',
			'http://www.imdb.com/title/tt1571739',
			'http://www.imdb.com/title/tt1571741',
			'http://www.imdb.com/title/tt1571962',
			'http://www.imdb.com/title/tt1571963',
			'http://www.imdb.com/title/tt1571984',
			'http://www.imdb.com/title/tt1571985',
			'http://www.imdb.com/title/tt1571989',
			'http://www.imdb.com/title/tt1571991',
			'http://www.imdb.com/title/tt1572002',
			'http://www.imdb.com/title/tt1572005',
			'http://www.imdb.com/title/tt1572008',
			'http://www.imdb.com/title/tt1572146',
			'http://www.imdb.com/title/tt1572154',
			'http://www.imdb.com/title/tt1572158',
			'http://www.imdb.com/title/tt1572166',
			'http://www.imdb.com/title/tt1572167',
			'http://www.imdb.com/title/tt1572168',
			'http://www.imdb.com/title/tt1572169',
			'http://www.imdb.com/title/tt1572172',
			'http://www.imdb.com/title/tt1572178',
			'http://www.imdb.com/title/tt1572186',
			'http://www.imdb.com/title/tt1572189',
			'http://www.imdb.com/title/tt1572194',
			'http://www.imdb.com/title/tt1572196',
			'http://www.imdb.com/title/tt1572300',
			'http://www.imdb.com/title/tt1572306',
			'http://www.imdb.com/title/tt1572309',
			'http://www.imdb.com/title/tt1572311',
			'http://www.imdb.com/title/tt1572315',
			'http://www.imdb.com/title/tt1572491',
			'http://www.imdb.com/title/tt1572501',
			'http://www.imdb.com/title/tt1572502',
			'http://www.imdb.com/title/tt1572503',
			'http://www.imdb.com/title/tt1572504',
			'http://www.imdb.com/title/tt1572506'
		]

		self.loadHandler = LoadHandler(self.urls, 0)

		self.lock = Lock()

	def createBrowser(self, name):

		parentWindowHandle = 0

		windowInfo = cef.WindowInfo()
		# windowInfo.SetAsOffscreen(parentWindowHandle)

		browser = cef.CreateBrowserSync(
			window_info=windowInfo,
			url='www.google.com.hk'
		)

		# browser.SetClientHandler(LoadHandler())
		browser.SetClientHandler(self.loadHandler)
		# browser.SetClientHandler(RenderHandler())

		browser.SendFocusEvent(True)
		browser.WasResized()

		self.loadHandler.browsers[browser.GetIdentifier()] = browser
		# cef.MessageLoop()

	def start(self):

		# self.browsers[0].LoadUrl(self.browsers[0].urls[0])
		# self.browsers[1].LoadUrl(self.browsers[1].urls[0])
		cef.MessageLoop()
		cef.Shutdown()

	def kill(self):

		print("test")
		for browser in self.browsers:

			browser.CloseBrowser()
			browser = None

		cef.QuitMessageLoop()

	# def OnLoadingStateChange(self, browser, is_loading, **_):
	# 	"""Called when the loading state has changed."""
	#
	# 	if not is_loading:
	# 		print(browser.GetIdentifier(), browser.GetUrl())
	#
	# 		if self.nextUrlId < len(self.urls):
	# 			self.lock.accquire()
	# 			browser.LoadUrl(self.urls[self.nextUrlId])
	# 			self.nextUrlId = self.nextUrlId + 1
	# 			self.lock.accquire()
	# 		else:
	# 			browser.CloseBrowser()


def main():
	test = WebNinjaBrowserHandler()
	test.createBrowser('testing1')
	test.createBrowser('testing2')

	test.createBrowser('testing1')
	test.start()

	time.sleep(10)

	test.kill()

if __name__ == '__main__':
    main()

