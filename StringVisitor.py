class StringVisitor(object):

	EXPORT_PATH = ''
	EXPORT_NAME = ''
	EXPORT_HTML = False
	EXPORT_SCREENSHOT = False
	EXPORT_PDF = False
	EXPORT_SCREENSHOT = False

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