# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import platform
import re
import subprocess
import sys
import time
import WebNinja

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
    from PIL import Image, PILLOW_VERSION
except:
    print("[WebNinja] Error: WebNinja needs PILLOW module for exporting screenshots. "
        "To install type: pip install Pillow")
    sys.exit(1)

try:
    from weasyprint import HTML, CSS
except:
    print("[WebNinja] Error: WebNinja needs WEASYPRINT module for exporting PDFs. "
        "To install type: pip install weasyprint")
    sys.exit(1)

class WebNinjaBrowser(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLaunchLoginPage = QtWidgets.QPushButton(self.centralwidget)
        self.btnLaunchLoginPage.setGeometry(QtCore.QRect(60, 70, 113, 32))
        self.btnLaunchLoginPage.setObjectName("btnLaunchLoginPage")
        self.btnFinishLoginPage = QtWidgets.QPushButton(self.centralwidget)
        self.btnFinishLoginPage.setGeometry(QtCore.QRect(60, 120, 113, 32))
        self.btnFinishLoginPage.setObjectName("btnFinishLoginPage")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(190, 40, 301, 291))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnLaunchLoginPage.clicked.connect(self.launchLoginPage)
        self.btnFinishLoginPage.clicked.connect(self.confirmLoginComplete)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLaunchLoginPage.setText(_translate("MainWindow", "Go to Login"))
        self.btnFinishLoginPage.setText(_translate("MainWindow", "Login Done"))

    def launchLoginPage(self):
        sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
        cef.Initialize(settings={"windowless_rendering_enabled": True})

        # parentWindowHandle = 0

        windowInfo = cef.WindowInfo()
        # windowInfo.SetAsOffscreen(parentWindowHandle)

        browser = cef.CreateBrowserSync(
            window_info=windowInfo,
            url="http://www.qichacha.com/user_login"
        )

        browser.SetClientHandler(WebNinja.LoadHandler())
        browser.SetClientHandler(WebNinja.RenderHandler())

        browser.SendFocusEvent(True)
        # You must call WasResized at least once to let know CEF that
        # viewport size is available and that OnPaint may be called.
        browser.WasResized()

        cef.MessageLoop()

    def confirmLoginComplete(self):
        pass

