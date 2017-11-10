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

# try:
#     from weasyprint import HTML, CSS
# except:
#     print("[WebNinja] Error: WebNinja needs WEASYPRINT module for exporting PDFs. "
#         "To install type: pip install weasyprint")
#     sys.exit(1)

class WebNinjaBrowser(object):
    browser = None

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
        self.tbvLinkOptionTable = QtWidgets.QTableView(self.centralwidget)
        self.tbvLinkOptionTable.setGeometry(QtCore.QRect(190, 40, 301, 291))
        self.tbvLinkOptionTable.setObjectName("tbvLinkOptionTable")
        self.txtLinkCsvAddress = QtWidgets.QTextEdit(self.centralwidget)
        self.txtLinkCsvAddress.setGeometry(QtCore.QRect(30, 210, 104, 31))
        self.txtLinkCsvAddress.setObjectName("txtLinkCsvAddress")
        self.btnUploadLinkCsv = QtWidgets.QPushButton(self.centralwidget)
        self.btnUploadLinkCsv.setGeometry(QtCore.QRect(30, 260, 93, 28))
        self.btnUploadLinkCsv.setObjectName("btnUploadLinkCsv")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnFinishLoginPage.clicked.connect(self.confirmLoginComplete)
        self.btnUploadLinkCsv.clicked.connect(self.uploadLinkCsv)
        self.btnLaunchLoginPage.clicked.connect(self.launchLoginPage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLaunchLoginPage.setText(_translate("MainWindow", "Go to Login"))
        self.btnFinishLoginPage.setText(_translate("MainWindow", "Login Done"))
        self.btnUploadLinkCsv.setText(_translate("MainWindow", "PushButton"))

    def launchLoginPage(self):
        sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
        cef.Initialize(settings={"windowless_rendering_enabled": True})

        # parentWindowHandle = 0

        windowInfo = cef.WindowInfo()
        # windowInfo.SetAsOffscreen(parentWindowHandle)

        self.browser = cef.CreateBrowserSync(
            window_info=windowInfo,
            url="http://www.qichacha.com/user_login"
        )

        # browser.SetClientHandler(WebNinja.LoadHandler())
        # browser.SetClientHandler(WebNinja.RenderHandler())

        self.browser.SendFocusEvent(True)
        # You must call WasResized at least once to let know CEF that
        # viewport size is available and that OnPaint may be called.
        self.browser.WasResized()

        cef.MessageLoop()

    def confirmLoginComplete(self):
        print("testing...")
        link = "http://www.qichacha.com/firm_CN_1223aabb6d71b8c5399d0dd1d7a5473e.html"
        # WebNinjaScrpaer.testBrowseNext(self.browser, link)
        self.browser.LoadUrl(link)
        print("testing...")

    def uploadLinkCsv(self):

        address = self.txtLinkCsvAddress.toPlainText()
        print(address)
        links = []

        with open(address, 'w') as inputFile:
            links = inputFile.readlines()