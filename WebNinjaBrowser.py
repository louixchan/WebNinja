# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
import os
import platform
import re
import subprocess
import sys
import time
import WebNinja
import csv
# from LinkOptionTableWidget import *
import numpy

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

# class WebNinjaBrowser(object):
#     browser = None
#
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 700)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.gpbLeftMenu = QtWidgets.QGroupBox(self.centralwidget)
#         self.gpbLeftMenu.setGeometry(QtCore.QRect(0, 0, 50, 700))
#         self.gpbLeftMenu.setTitle("")
#         self.gpbLeftMenu.setObjectName("gpbLeftMenu")
#         self.lblLogo = QtWidgets.QLabel(self.gpbLeftMenu)
#         self.lblLogo.setGeometry(QtCore.QRect(0, 0, 50, 50))
#         self.lblLogo.setText("")
#         self.lblLogo.setObjectName("lblLogo")
#         self.gpbTasksTab = QtWidgets.QGroupBox(self.centralwidget)
#         self.gpbTasksTab.setGeometry(QtCore.QRect(50, 0, 750, 700))
#         self.gpbTasksTab.setTitle("")
#         self.gpbTasksTab.setObjectName("gpbTasksTab")
#         self.tbwLinkOption = QtWidgets.QTableWidget(self.gpbTasksTab)
#         self.tbwLinkOption.setGeometry(QtCore.QRect(50, 230, 651, 381))
#         self.tbwLinkOption.setObjectName("tbwLinkOption")
#         self.tbwLinkOption.setColumnCount(0)
#         self.tbwLinkOption.setRowCount(0)
#         self.btnAllScreenshot = QtWidgets.QPushButton(self.gpbTasksTab)
#         self.btnAllScreenshot.setGeometry(QtCore.QRect(600, 150, 113, 32))
#         self.btnAllScreenshot.setObjectName("btnAllScreenshot")
#         self.txtLinkCsvAddress = QtWidgets.QTextEdit(self.gpbTasksTab)
#         self.txtLinkCsvAddress.setGeometry(QtCore.QRect(110, 190, 104, 31))
#         self.txtLinkCsvAddress.setObjectName("txtLinkCsvAddress")
#         self.btnFinishLoginPage = QtWidgets.QPushButton(self.gpbTasksTab)
#         self.btnFinishLoginPage.setGeometry(QtCore.QRect(230, 170, 112, 15))
#         self.btnFinishLoginPage.setObjectName("btnFinishLoginPage")
#         self.btnAllPdf = QtWidgets.QPushButton(self.gpbTasksTab)
#         self.btnAllPdf.setGeometry(QtCore.QRect(490, 150, 113, 32))
#         self.btnAllPdf.setObjectName("btnAllPdf")
#         self.btnAllHtml = QtWidgets.QPushButton(self.gpbTasksTab)
#         self.btnAllHtml.setGeometry(QtCore.QRect(380, 150, 113, 32))
#         self.btnAllHtml.setObjectName("btnAllHtml")
#         self.btnUploadLinkCsv = QtWidgets.QPushButton(self.gpbTasksTab)
#         self.btnUploadLinkCsv.setGeometry(QtCore.QRect(120, 150, 93, 28))
#         self.btnUploadLinkCsv.setObjectName("btnUploadLinkCsv")
#         self.btnLaunchLoginPage = QtWidgets.QPushButton(self.gpbTasksTab)
#         self.btnLaunchLoginPage.setGeometry(QtCore.QRect(230, 200, 112, 32))
#         self.btnLaunchLoginPage.setObjectName("btnLaunchLoginPage")
#         self.btnBrowserFile = QtWidgets.QPushButton(self.gpbTasksTab)
#         self.btnBrowserFile.setGeometry(QtCore.QRect(380, 190, 112, 15))
#         self.btnBrowserFile.setObjectName("btnBrowserFile")
#         self.gpbTasksHeader = QtWidgets.QGroupBox(self.gpbTasksTab)
#         self.gpbTasksHeader.setGeometry(QtCore.QRect(0, 0, 750, 100))
#         self.gpbTasksHeader.setTitle("")
#         self.gpbTasksHeader.setObjectName("gpbTasksHeader")
#         self.gpbTasksTab.raise_()
#         self.gpbLeftMenu.raise_()
#         self.txtLinkCsvAddress.raise_()
#         self.btnUploadLinkCsv.raise_()
#         self.tbwLinkOption.raise_()
#         self.btnAllHtml.raise_()
#         self.btnAllPdf.raise_()
#         self.btnAllScreenshot.raise_()
#         self.btnFinishLoginPage.raise_()
#         self.btnBrowserFile.raise_()
#         self.btnLaunchLoginPage.raise_()
#
#         self.btnHome = QtWidgets.QPushButton(self.gpbLeftMenu)
#         self.btnHome.setGeometry(QtCore.QRect(0, 50, 50, 50))
#         self.btnHome.setObjectName("btnHome")
#         self.btnTasks = QtWidgets.QPushButton(self.gpbLeftMenu)
#         self.btnTasks.setGeometry(QtCore.QRect(0, 100, 50, 50))
#         self.btnTasks.setObjectName("btnTasks")
#         self.btnBrowse = QtWidgets.QPushButton(self.gpbLeftMenu)
#         self.btnBrowse.setGeometry(QtCore.QRect(0, 150, 50, 50))
#         self.btnBrowse.setObjectName("btnBrowse")
#         self.btnSettings = QtWidgets.QPushButton(self.gpbLeftMenu)
#         self.btnSettings.setGeometry(QtCore.QRect(0, 200, 50, 50))
#         self.btnSettings.setObjectName("btnSettings")
#
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         with open("stylesheet.css", "r") as fh:
#             MainWindow.setStyleSheet(fh.read())
#
#         self.retranslateUi(MainWindow)
#         self.btnFinishLoginPage.clicked.connect(self.confirmLoginComplete)
#         self.btnUploadLinkCsv.clicked.connect(self.uploadLinkCsv)
#         self.btnLaunchLoginPage.clicked.connect(self.launchLoginPage)
#         self.btnBrowserFile.clicked.connect(self.launchFileDialog)
#         self.btnAllHtml.clicked.connect(self.setAllHtml)
#         self.btnAllPdf.clicked.connect(self.setAllPdf)
#         self.btnAllScreenshot.clicked.connect(self.setAllScreenshot)
#         self.btnHome.clicked.connect(self.selectHomeTab)
#         self.btnTasks.clicked.connect(self.selectTasksTab)
#         self.btnBrowse.clicked.connect(self.selectBrowseTab)
#         self.btnSettings.clicked.connect(self.selectSettingsTab)
#         self.tbwLinkOption.setColumnCount(6)
#         self.tbwLinkOption.setHorizontalHeaderLabels(['Link', 'Export Name', 'HTML', 'PDF', 'PNG', ''])
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#         self.tbwLinkOption.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
#         # self.tbwLinkOption.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
#         # self.tbwLinkOption.setFocusPolicy(QtCore.Qt.NoFocus)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.btnUploadLinkCsv.setText(_translate("MainWindow", "PushButton"))
#         self.btnAllHtml.setText(_translate("MainWindow", "All HTML"))
#         self.btnAllPdf.setText(_translate("MainWindow", "All PDF"))
#         self.btnAllScreenshot.setText(_translate("MainWindow", "All Screenshot"))
#         self.btnFinishLoginPage.setText(_translate("MainWindow", "Login Done"))
#         self.btnBrowserFile.setText(_translate("MainWindow", "PushButton"))
#         self.btnLaunchLoginPage.setText(_translate("MainWindow", "Go to Login"))
#
#     def launchLoginPage(self):
#         sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
#         cef.Initialize(settings={"windowless_rendering_enabled": True})
#         windowInfo = cef.WindowInfo()
#
#         self.browser = cef.CreateBrowserSync(
#             window_info=windowInfo,
#             url="http://www.qichacha.com/user_login"
#         )
#         self.browser.SendFocusEvent(True)
#         self.browser.WasResized()
#
#         cef.MessageLoop()
#
#     def confirmLoginComplete(self):
#         print("testing...")
#         link = "http://www.qichacha.com/firm_CN_1223aabb6d71b8c5399d0dd1d7a5473e.html"
#         # WebNinjaScrpaer.testBrowseNext(self.browser, link)
#         self.browser.LoadUrl(link)
#         print("testing...")
#
#     def uploadLinkCsv(self):
#
#         address = self.txtLinkCsvAddress.toPlainText()
#         print(address)
#         links = []
#
#         with open(address, 'r') as inputFile:
#             links = inputFile.readlines()
#
#             n = self.tbwLinkOption.rowCount()
#             self.tbwLinkOption.setRowCount(
#                 self.tbwLinkOption.rowCount() + len(links))
#
#             for link in links:
#                 item = QtWidgets.QTableWidgetItem(link)
#                 # item.setText(link)
#                 checkbox = QCheckBox()
#                 self.tbwLinkOption.setItem(n, 0, item)
#                 self.tbwLinkOption.setCellWidget(n, 1, checkbox)
#                 n = n + 1
#
#     def launchFileDialog(self):
#
#         dialog = QFileDialog()
#         dialog.setFileMode(QFileDialog.AnyFile)
#         filenames = []
#
#         if dialog.exec_():
#             filenames = dialog.selectedFiles()
#             # f = open(filenames[0], 'r')
#
#             with open(filenames[0], 'r') as inputFile:
#                 links = csv.reader(inputFile, delimiter=',')
#
#                 n = self.tbwLinkOption.rowCount()
#                 # self.tbwLinkOption.setRowCount(
#                 #     self.tbwLinkOption.rowCount() + len(links))
#
#                 for row in links:
#                     print(row)
#                     self.tbwLinkOption.setRowCount(n + 1)
#                     item = QtWidgets.QTableWidgetItem(row[0])
#                     btn = QPushButton()
#                     self.tbwLinkOption.setItem(n, 0, QtWidgets.QTableWidgetItem(row[0]))
#                     self.tbwLinkOption.setItem(n, 1, QtWidgets.QTableWidgetItem(row[1]))
#                     checkbox = QCheckBox()
#                     checkbox.setChecked(row[2] == '1')
#                     self.tbwLinkOption.setCellWidget(n, 2, checkbox)
#                     checkbox = QCheckBox()
#                     checkbox.setChecked(row[3] == '1')
#                     self.tbwLinkOption.setCellWidget(n, 3, checkbox)
#                     checkbox = QCheckBox()
#                     checkbox.setChecked(row[4] == '1')
#                     self.tbwLinkOption.setCellWidget(n, 4, checkbox)
#                     self.tbwLinkOption.setCellWidget(n, 5, btn)
#                     btn.clicked.connect(self.tbwLinkOption.buttonClicked)
#                     n = n + 1
#
#     def deleteLinkOptionRow(self):
#         clickme = QApplication.focusWidget()
#         index = self.tbwLinkOption.indexAt(clickme.pos())
#         print(clickme.pos())
#         if index.isValid():
#             print(index.row())
#
#     def setAllHtml(self):
#
#         rowCount = self.tbwLinkOption.rowCount()
#         for row in numpy.arange(rowCount):
#             self.tbwLinkOption.cellWidget(row, 2).setChecked(True)
#
#     def setAllPdf(self):
#
#         rowCount = self.tbwLinkOption.rowCount()
#         for row in numpy.arange(rowCount):
#             self.tbwLinkOption.cellWidget(row, 3).setChecked(True)
#
#     def setAllScreenshot(self):
#
#         rowCount = self.tbwLinkOption.rowCount()
#         for row in numpy.arange(rowCount):
#             self.tbwLinkOption.cellWidget(row, 4).setChecked(True)
#
#     def setNoHtml(self):
#
#         rowCount = self.tbwLinkOption.rowCount()
#         for row in numpy.arange(rowCount):
#             self.tbwLinkOption.cellWidget(row, 2).setChecked(False)
#
#     def setNoPdf(self):
#
#         rowCount = self.tbwLinkOption.rowCount()
#         for row in numpy.arange(rowCount):
#             self.tbwLinkOption.cellWidget(row, 3).setChecked(False)
#
#     def setNoScreenshot(self):
#
#         rowCount = self.tbwLinkOption.rowCount()
#         for row in numpy.arange(rowCount):
#             self.tbwLinkOption.cellWidget(row, 4).setChecked(False)
#
#     def resetLeftMenu(self, home, tasks, browse, setting):
#
#         if home:
#             self.btnHome.setStyleSheet("background-image: url('home-icon.png')")
#
#         if tasks:
#             self.btnTasks.setStyleSheet("background-image: url('tasks-icon.png')")
#
#         if browse:
#             self.btnBrowse.setStyleSheet("background-image: url('browse-icon.png')")
#
#         if setting:
#             self.btnSettings.setStyleSheet("background-image: url('settings-icon.png')")
#
#     def selectHomeTab(self):
#
#         self.btnHome.setStyleSheet("background-image: url('home-icon-selected.png')")
#         self.resetLeftMenu(False, True, True, True)
#
#     def selectTasksTab(self):
#
#         self.btnTasks.setStyleSheet("background-image: url('tasks-icon-selected.png')")
#         self.resetLeftMenu(True, False, True, True)
#
#     def selectBrowseTab(self):
#
#         self.btnBrowse.setStyleSheet("background-image: url('browse-icon-selected.png')")
#         self.resetLeftMenu(True, True, False, True)
#
#     def selectSettingsTab(self):
#
#         self.btnSettings.setStyleSheet("background-image: url('settings-icon-selected.png')")
#         self.resetLeftMenu(True, True, True, False)