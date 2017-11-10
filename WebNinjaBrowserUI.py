# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from WebNinjaScraper import *

class Ui_MainWindow(object):

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
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def launchLoginPage(self):
        self.browser = WebNinjaScraper.startTestBrowsing()
        return

    def confirmLoginComplete(self):
        print("testing...")
        link = "http://www.qichacha.com/firm_CN_1223aabb6d71b8c5399d0dd1d7a5473e.html"
        # WebNinjaScrpaer.testBrowseNext(self.browser, link)
        self.browser.LoadUrl(link)
        print("testing...")
