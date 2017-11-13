# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gpbLeftMenu = QtWidgets.QGroupBox(self.centralwidget)
        self.gpbLeftMenu.setGeometry(QtCore.QRect(0, 0, 200, 700))
        self.gpbLeftMenu.setTitle("")
        self.gpbLeftMenu.setObjectName("gpbLeftMenu")
        self.lblLogo = QtWidgets.QLabel(self.gpbLeftMenu)
        self.lblLogo.setGeometry(QtCore.QRect(0, 0, 200, 100))
        self.lblLogo.setText("")
        self.lblLogo.setObjectName("lblLogo")
        self.gpbTasksTab = QtWidgets.QGroupBox(self.centralwidget)
        self.gpbTasksTab.setGeometry(QtCore.QRect(50, 0, 750, 700))
        self.gpbTasksTab.setTitle("")
        self.gpbTasksTab.setObjectName("gpbTasksTab")
        self.tbwLinkOption = QtWidgets.QTableWidget(self.gpbTasksTab)
        self.tbwLinkOption.setGeometry(QtCore.QRect(50, 230, 651, 381))
        self.tbwLinkOption.setObjectName("tbwLinkOption")
        self.tbwLinkOption.setColumnCount(0)
        self.tbwLinkOption.setRowCount(0)
        self.btnAllScreenshot = QtWidgets.QPushButton(self.gpbTasksTab)
        self.btnAllScreenshot.setGeometry(QtCore.QRect(600, 150, 113, 32))
        self.btnAllScreenshot.setObjectName("btnAllScreenshot")
        self.txtLinkCsvAddress = QtWidgets.QTextEdit(self.gpbTasksTab)
        self.txtLinkCsvAddress.setGeometry(QtCore.QRect(110, 190, 104, 31))
        self.txtLinkCsvAddress.setObjectName("txtLinkCsvAddress")
        self.btnFinishLoginPage = QtWidgets.QPushButton(self.gpbTasksTab)
        self.btnFinishLoginPage.setGeometry(QtCore.QRect(230, 170, 112, 15))
        self.btnFinishLoginPage.setObjectName("btnFinishLoginPage")
        self.btnAllPdf = QtWidgets.QPushButton(self.gpbTasksTab)
        self.btnAllPdf.setGeometry(QtCore.QRect(490, 150, 113, 32))
        self.btnAllPdf.setObjectName("btnAllPdf")
        self.btnAllHtml = QtWidgets.QPushButton(self.gpbTasksTab)
        self.btnAllHtml.setGeometry(QtCore.QRect(380, 150, 113, 32))
        self.btnAllHtml.setObjectName("btnAllHtml")
        self.btnUploadLinkCsv = QtWidgets.QPushButton(self.gpbTasksTab)
        self.btnUploadLinkCsv.setGeometry(QtCore.QRect(120, 150, 93, 28))
        self.btnUploadLinkCsv.setObjectName("btnUploadLinkCsv")
        self.btnLaunchLoginPage = QtWidgets.QPushButton(self.gpbTasksTab)
        self.btnLaunchLoginPage.setGeometry(QtCore.QRect(230, 200, 112, 32))
        self.btnLaunchLoginPage.setObjectName("btnLaunchLoginPage")
        self.btnBrowserFile = QtWidgets.QPushButton(self.gpbTasksTab)
        self.btnBrowserFile.setGeometry(QtCore.QRect(380, 190, 112, 15))
        self.btnBrowserFile.setObjectName("btnBrowserFile")
        self.gpbTasksHeader = QtWidgets.QGroupBox(self.gpbTasksTab)
        self.gpbTasksHeader.setGeometry(QtCore.QRect(0, 0, 750, 100))
        self.gpbTasksHeader.setTitle("")
        self.gpbTasksHeader.setObjectName("gpbTasksHeader")
        self.gpbTasksTab.raise_()
        self.gpbLeftMenu.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnFinishLoginPage.clicked.connect(MainWindow.confirmLoginComplete)
        self.btnUploadLinkCsv.clicked.connect(MainWindow.uploadLinkCsv)
        self.btnLaunchLoginPage.clicked.connect(MainWindow.launchLoginPage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAllScreenshot.setText(_translate("MainWindow", "All Screenshot"))
        self.btnFinishLoginPage.setText(_translate("MainWindow", "Login Done"))
        self.btnAllPdf.setText(_translate("MainWindow", "All PDF"))
        self.btnAllHtml.setText(_translate("MainWindow", "All HTML"))
        self.btnUploadLinkCsv.setText(_translate("MainWindow", "Upload Link Csv"))
        self.btnLaunchLoginPage.setText(_translate("MainWindow", "Go to Login"))
        self.btnBrowserFile.setText(_translate("MainWindow", "Browse File"))

