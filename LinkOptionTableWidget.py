import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class LinkOptionTableWidget(QtWidgets.QTableWidget):

    def __init__(self, data, parent = None):
        super().__init__(data)

    def buttonClicked(self):
        buttonClicked = self.sender()
        index = self.indexAt(buttonClicked.pos())
        print(index.row())
        self.removeRow(index.row())