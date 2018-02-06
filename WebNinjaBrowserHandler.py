from cefpython3 import cefpython as cef
import sys
import time
from WebNinjaLoadHandler import LoadHandler

class WebNinjaBrowserHandler:

	browserCount = 0
	browsers = []

	def __init__(self):

		self.browserCount = 0
		sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
		cef.Initialize(settings={"windowless_rendering_enabled": True, "downloads_enabled": True})

		self.urls = ['www.facebook.com', 'www.google.com.hk', 'www.youtube.com', 'www.reddit.com',
		        'www.instagram.com', 'www.twitter.com', 'www.maps.google.com', 'www.pypi.python.org']

	def createBrowser(self):

		parentWindowHandle = 0

		windowInfo = cef.WindowInfo()
		# windowInfo.SetAsOffscreen(parentWindowHandle)

		browser = cef.CreateBrowserSync(
			window_info=windowInfo,
			url='www.google.com.hk'
		)

		browser.SetClientHandler(LoadHandler(self.urls[0:4], -1))
		# browser.SetClientHandler(RenderHandler())

		# browser.urls =
		# browser.index = -1
		self.urls = self.urls[-4:]

		browser.SendFocusEvent(True)
		# You must call WasResized at least once to let know CEF that
		# viewport size is available and that OnPaint may be called.
		browser.WasResized()

		self.browsers.append(browser)
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


def main():
	test = WebNinjaBrowserHandler()
	test.createBrowser()
	test.createBrowser()

	test.start()

	time.sleep(10)

	test.kill()

if __name__ == '__main__':
    main()