from cefpython3 import cefpython as cef
import sys
import time
from WebNinjaLoadHandler import LoadHandler
import datetime
import pandas
import os

VIEWPORT_SIZE = (1024, 5000)


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


class WebNinjaBrowserHandler(object):

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
'http://www.imdb.com/title/tt3460062'
		]

		self.loadHandler = LoadHandler(self.urls, 0)

	def createBrowser(self, name):

		parentWindowHandle = 0

		windowInfo = cef.WindowInfo()
		windowInfo.SetAsOffscreen(parentWindowHandle)

		browser = cef.CreateBrowserSync(
			window_info=windowInfo,
			url='www.google.com.hk'
		)

		# browser.SetClientHandler(LoadHandler())
		browser.SetClientHandler(self.loadHandler)
		browser.SetClientHandler(RenderHandler())

		browser.SendFocusEvent(True)
		browser.WasResized()

		self.loadHandler.browsers[browser.GetIdentifier()] = browser
		self.loadHandler.browserCurrentState[browser.GetIdentifier()] = 0
		# cef.MessageLoop()

	def start(self):

		# self.browsers[0].LoadUrl(self.browsers[0].urls[0])
		# self.browsers[1].LoadUrl(self.browsers[1].urls[0])

		# for key, browser in self.loadHandler.browsers.items():
		# 	print(key)
		# 	url = self.loadHandler.urls[self.loadHandler.nextUrlId]
		# 	browser.LoadUrl(url)
		# 	print(url)
		# 	self.loadHandler.nextUrlId = self.loadHandler.nextUrlId + 1

		print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f'))
		cef.MessageLoop()
		cef.Shutdown()
		print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f'))

	def kill(self):

		print("test")
		for browser in self.browsers:

			browser.CloseBrowser()
			browser = None

		cef.QuitMessageLoop()

def createBrowser():

	parentWindowHandle = 0

	windowInfo = cef.WindowInfo()
	windowInfo.SetAsOffscreen(parentWindowHandle)

	browser = cef.CreateBrowserSync(
		window_info=windowInfo,
		url='www.google.com.hk'
	)

	browser.SendFocusEvent(True)
	browser.WasResized()

	return browser
#
# def check_versions():
#     print("[WebNinja] CEF Python {ver}".format(ver=cef.__version__))
#     print("[WebNinja] Python {ver} {arch}".format(
#           ver=platform.python_version(), arch=platform.architecture()[0]))
#     assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"

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
	print("    python3 WebNinjaBrowserHandler.py -man")
	print()
	print("DESCRIPTION")
	print("    Open manual page.")
	print()
	print("NAME")
	print("    python3 WebNinjaBrowserHandler.py -s [link] -e [export link] -html [HTML flag] -pdf [PDF flag] -ss [screenshot flag]")
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
	print("    python3 WebNinjaBrowserHandler.py -m [file link] -e [export link] -html [HTML flag] -pdf [PDF flag] -ss [screenshot flag] -b [browser count]")
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
	print("    [browser count]: Number of browser to browse in parallel. (Default: 1)")
	print()

def main():

	print("WebNinjaBrowserHandler.py is the multi-thread version of WebNinja.")
	print("Please refer to WebNinja.py for the single thread version.")

	EXPORT_HTML = False
	EXPORT_SCREENSHOT = False
	EXPORT_PDF = False
	EXPORT_DOWNLOAD = False
	EXPORT_BASE_PATH = ''
	BROWSER_COUNT = 1

	URLs = []

	# check_versions()
	checkDependencies()

	if len(sys.argv) == 1:
		print("[WebNinja] Error: Not option specified. To see all options, "
			  "type: python3 WebNinja.py -man")
		sys.exit(1)

	if sys.argv[1] == "-man":

		manual()
		sys.exit(1)

	else:

		argvId = 1

		while argvId < len(sys.argv):

			if sys.argv[argvId] == "-s":

				URLs = pandas.DataFrame([{"name": "target", "url": sys.argv[argvId + 1]}])

				argvId = argvId + 1

			elif sys.argv[argvId] == "-m":

				try:
					URLs = pandas.read_csv(sys.argv[argvId + 1], None, names=["name", "url"], engine="python")
				except:
					print(
						"[WebNinja] Error: Invalid file path. To see other options, type: python3 WebNinjaBrowserHandler.py -man")

				argvId = argvId + 1

			elif sys.argv[argvId] == "-b":

				try:
					BROWSER_COUNT = int(sys.argv[argvId + 1])
				except:
					print(
						"[WebNinja] Error: Positive integer is expected for Browser Count. To see other options, type: "
						"python3 WebNinjaBrowserHandler.py -man"
					)

				if BROWSER_COUNT < 1:
					print(
						"[WebNinja] Error: Positive integer is expected for Browser Count. To see other options, type: "
						"python3 WebNinjaBrowserHandler.py -man"
					)
					sys.exit(1)

				argvId = argvId + 1

			elif sys.argv[argvId] == "-e":

				EXPORT_BASE_PATH = sys.argv[argvId + 1]
				argvId = argvId + 1

			elif sys.argv[argvId] == "-html":

				EXPORT_HTML = True

			elif sys.argv[argvId] == "-pdf":

				EXPORT_PDF = True

			elif sys.argv[argvId] == "-ss":

				EXPORT_SCREENSHOT = True

			elif sys.argv[argvId] == "-dl":

				EXPORT_DOWNLOAD = True

			else:

				print("[WebNinja] Error: Option %s not recognised. To see all options, "
					  "type: python3 WebNinjaBrowserHandler.py -man" % sys.argv[argvId])
				sys.exit(1)

			argvId = argvId + 1

		if (argvId != len(sys.argv)):
			print("[WebNinja] Error: Option %s has a missing specifier. To see all options, "
				  "type: python3 WebNinjaBrowserHandler.py -man" % sys.argv[argvId - 2])
			sys.exit(1)

	if len(URLs) == 0:
		print(
			"[WebNinja] Error: No URL specified. To see all options, "
			"type: python3 WebNinjaBrowserHandler.py -man"
		)
		sys.exit(1)

	if not os.path.exists(EXPORT_BASE_PATH):
		os.makedirs(EXPORT_BASE_PATH)

	# print(URLs)

	loadHandler = LoadHandler(urls=URLs, exportPath=EXPORT_BASE_PATH)

	sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
	cef.Initialize(settings={"windowless_rendering_enabled": True, "downloads_enabled": True})

	# test = WebNinjaBrowserHandler()

	i = 0
	while i < BROWSER_COUNT:
		browser = createBrowser()
		browser.SetClientHandler(loadHandler)
		browser.SetClientHandler(RenderHandler())

		loadHandler.browsers[browser.GetIdentifier()] = browser
		loadHandler.browserCurrentState[browser.GetIdentifier()] = 0
		i = i + 1

	cef.MessageLoop()
	cef.Shutdown()

	# time.sleep(10)
	#
	# test.kill()

if __name__ == '__main__':
	main()

