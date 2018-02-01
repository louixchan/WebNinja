# -*- coding: utf-8 -*-__author__ = 'djstava@gmail.com'
import sys
# from PyQt5.QtWidgets import QApplication , QMainWindow
# from testing import *
from WebNinjaBrowser import *
from WebNinja import checkDependencies
import htmlPy

if __name__ == '__main__':
	import htmlPy
	import os

	app = htmlPy.AppGUI(title=u"htmlPy Quickstart", maximized=True)

	app.template_path = os.path.abspath(".")
	app.static_path = os.path.abspath(".")

	app.template = ("startbootstrap-sb-admin-gh-pages/index.html", {"username": "htmlPy_user"})

	app.start()

	# checkDependencies()
	# app = QApplication(sys.argv)
	# mainWindow = QMainWindow()
	# ui = WebNinjaBrowser()
	# ui.setupUi(mainWindow)
	# mainWindow.show()
	# sys.exit(app.exec_())