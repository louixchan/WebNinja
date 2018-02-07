from cefpython3 import cefpython as cef
import sys
import time
# from WebNinjaLoadHandler import LoadHandler

class WebNinjaBrowserHandler():

	browserCount = 0
	browsers = {}
	browserUrls = {}
	browserCurrentUrl = {}
	browserCurrentState = {}
	URLS = []


	def __init__(self):

		self.browserCount = 0
		sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
		cef.Initialize(settings={"windowless_rendering_enabled": True, "downloads_enabled": True})

		self.urls = ['www.facebook.com', 'www.google.com.hk', 'www.youtube.com', 'www.reddit.com',
		        'www.instagram.com', 'www.twitter.com', 'www.maps.google.com', 'www.pypi.python.org']

	def createBrowser(self, name):

		parentWindowHandle = 0

		windowInfo = cef.WindowInfo()
		# windowInfo.SetAsOffscreen(parentWindowHandle)

		browser = cef.CreateBrowserSync(
			window_info=windowInfo,
			url='www.google.com.hk'
		)

		browser.SetClientHandler(self)

		browser.SendFocusEvent(True)
		browser.WasResized()

		self.browsers[browser.GetIdentifier()] = browser
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

	def OnLoadingStateChange(self, browser, is_loading, **_):
		"""Called when the loading state has changed."""

		if not is_loading and self.CURRENT_URL != browser.GetUrl():
			print(self.name, browser.GetUrl())
			self.CURRENT_URL = browser.GetUrl()

			if self.index < len(self.urls):
				self.index = self.index + 1
				browser.LoadUrl(self.urls[self.index])
			else:
				browser.CloseBrowser()


def main():
	test = WebNinjaBrowserHandler()
	test.createBrowser('testing1')
	test.createBrowser('testing2')

	test.start()

	time.sleep(10)

	test.kill()

if __name__ == '__main__':
    main()