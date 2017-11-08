# -*- coding: utf-8 -*-__author__ = 'djstava@gmail.com'
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from testing import *
from WebNinjaBrowser import *
from WebNinja import checkDependencies

if __name__ == '__main__':
	checkDependencies()
	app = QApplication(sys.argv)    
	mainWindow = QMainWindow()    
	ui = WebNinjaBrowser()
	ui.setupUi(mainWindow)    
	mainWindow.show()    
	sys.exit(app.exec_()) 