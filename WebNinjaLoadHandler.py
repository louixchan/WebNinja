from cefpython3 import cefpython as cef
import pdfkit
from threading import Lock
from ExportUtility import *

class LoadHandler(object):

    stringVisitor = None
    RETRY_LIMIT = 0
    RETRY_COUNT = 0
    CURRENT_URL = ''

    browserCount = 0
    browsers = {}
    browserUrls = {}
    browserCurrentIndex = {}
    browserCurrentState = {}
    nextUrlId = 0
    URLS = []

    EXPORT_HTML = False
    EXPORT_SCREENSHOT = False
    EXPORT_PDF = False
    EXPORT_DOWNLOAD = False
    EXPORT_BASE_PATH = ""

    def __init__(self, urls, index=-1, name='', exportPath=""):

        self.urls = urls
        self.index = index
        self.name = name
        self.lock = Lock()
        self.EXPORT_BASE_PATH = exportPath

    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Called when the loading state has changed."""

        if not is_loading:
            # print(browser.GetIdentifier(), browser.GetUrl())

            # print("WebNinja is loading the webpage...", browser.GetUrl())

            if self.browserCurrentState[browser.GetIdentifier()] > 0:
                save_screenshot(browser,
                    self.EXPORT_BASE_PATH + self.urls.iloc[self.browserCurrentIndex[browser.GetIdentifier()]]['name'])

            self.browserCurrentState[browser.GetIdentifier()] = self.browserCurrentState[browser.GetIdentifier()] + 1


            # Loading is complete
            # sys.stdout.write(os.linesep)
            print("WebNinja has loaded the webpage...", browser.GetUrl())

            if self.nextUrlId < len(self.urls):
                with self.lock:
                    nextUrl = self.urls.iloc[self.nextUrlId]['url']
                    self.browserCurrentIndex[browser.GetIdentifier()] = self.nextUrlId
                    self.nextUrlId = self.nextUrlId + 1
                browser.LoadUrl(nextUrl)
            else:
                browser.CloseBrowser()
            # time.sleep(0.3)
            # save_screenshot(browser)
        #     # See comments in exit_app() why PostTask must be used
        #     cef.PostTask(cef.TID_UI, exit_app, browser)
        # pass

    # def OnLoadEnd(self, browser, frame, http_code):
    #
    #     # print(http_code)
    #     # if frame.IsMain():
    #     if self.browserCurrentState[browser.GetIdentifier()] > 0:
    #
    #         self.stringVisitor = StringVisitor()
    #         self.stringVisitor.EXPORT_PATH = self.EXPORT_BASE_PATH + \
    #                                          self.urls.iloc[self.browserCurrentIndex[browser.GetIdentifier()]]['name']
    #

            # if http_code == 200:
            #
            #     self.CURRENT_URL = browser.GetUrl()
                # global RETRY_ATTEMPT
                # RETRY_ATTEMPT = 0
                # # if MODE == "TEST":
                # #     MODE = "TEST3"
                # #     return
                # #
                # # elif MODE == "TEST2":
                # #
                # #     self.stringVisitor.EXPORT_PATH = EXPORT_BASE_PATH + "target"
                # #     frame.GetSource(self.stringVisitor)
                # #     return
                # #
                # # elif MODE == "TEST3":
                # #     testBrowseNext(browser, "http://www.qichacha.com/firm_CN_f470d4e4d2bf1fc59650255443707461.html")
                # #     return
                #
                # print("[WebNinja] Message: has loaded the website successfully...")
                #
                # if EXPORT_DOWNLOAD:
                #     print("Downloading...")
                #     browser.StartDownload(browser.GetUrl())
                #
                # else:
                #     # print("Here!")
                #     if self.EXPORT_HTML:
                #         frame.GetSource(self.stringVisitor)
                #
                #     if EXPORT_SCREENSHOT:
                #         save_screenshot(browser)
                # browser.Print()
                # frame.GetText(self.stringVisitor)
                # print(SV.value)

                # browser.browseNext()

        # if self.nextUrlId < len(self.urls):
        #     with self.lock:
        #         nextUrl = self.urls.iloc[self.nextUrlId]['url']
        #         self.browserCurrentIndex[browser.GetIdentifier()] = self.nextUrlId
        #         self.nextUrlId = self.nextUrlId + 1
        #     browser.LoadUrl(nextUrl)
        # else:
        #     browser.CloseBrowser()
#
#     def OnLoadError(self, browser, frame, error_code, error_text_out, failed_url):
#         """Called when the resource load for a navigation fails
#         or is canceled."""
#         global ERROR
#         if not frame.IsMain():
#             # We are interested only in loading main url.
#             # Ignore any errors during loading of other frames.
#             return
#         print("[WebNinja] ERROR: Failed to load url: {url}"
#               .format(url=failed_url))
#         print("[WebNinja] Error code: {code}"
#               .format(code=error_code))
#         print("[WebNinja] Error description: {text}"
#               .format(text=error_text_out))
#         # ERROR = True
#         global RETRY_LIMIT
#         global RETRY_ATTEMPT
#
#         if RETRY_ATTEMPT < RETRY_LIMIT:
#             print("[WebNinja] Message: Retrying to load url: {url}"
#                   .format(url=failed_url))
#             global CURRENT_ID
#             CURRENT_ID = CURRENT_ID - 1
#             RETRY_ATTEMPT = RETRY_ATTEMPT + 1
#             browseNext(browser)
#         # else:
#             # See comments in exit_app() why PostTask must be used
#             # cef.PostTask(cef.TID_UI, exit_app, browser)
#

class StringVisitor(object):
    EXPORT_PATH = ''

    def Visit(self, value):

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