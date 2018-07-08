# from PyQt5 import QtWidgets
# # from mainwindow import Ui_MainWindow
#
# class Login(QtWidgets.QDialog):
#     def __init__(self, parent=None):
#         super(Login, self).__init__(parent)
#         self.textName = QtWidgets.QLineEdit(self)
#         self.textPass = QtWidgets.QLineEdit(self)
#         self.buttonLogin = QtWidgets.QPushButton('Login', self)
#         self.buttonLogin.clicked.connect(self.handleLogin)
#         layout = QtWidgets.QVBoxLayout(self)
#         layout.addWidget(self.textName)
#         layout.addWidget(self.textPass)
#         layout.addWidget(self.buttonLogin)
#
#     def handleLogin(self):
#         if (self.textName.text() == 'foo' and
#             self.textPass.text() == 'bar'):
#             self.accept()
#         else:
#             QtWidgets.QMessageBox.warning(
#                 self, 'Error', 'Bad user or password')
#
# class Window(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super(Window, self).__init__(parent)
#         # self.ui = Ui_MainWindow()
#         # self.ui.setupUi(self)
#
# if __name__ == '__main__':
#
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     login = Login()
#
#     if login.exec_() == QtWidgets.QDialog.Accepted:
#         window = Window()
#         window.show()
#         sys.exit(app.exec_())

import sys
from PyQt5 import QtWidgets, QtSql
from PyQt5.QtGui import *
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import *

import shutil
import os


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent = None):

        QtWidgets.QMainWindow.__init__(self, parent)

        self.model = QStandardItemModel(8, 4)
        table = QtWidgets.QTableView()
        table.setModel(self.model)

        actionMenu = QtWidgets.QMenu(self.tr("&Actions"), self)
        fillAction = actionMenu.addAction(self.tr("&Fill Selection"))
        clearAction = actionMenu.addAction(self.tr("&Clear Selection"))
        selectAllAction = actionMenu.addAction(self.tr("&Select All"))
        self.menuBar().addMenu(actionMenu)

        fillAction.triggered.connect(self.fillSelection)
        clearAction.triggered.connect(self.clearSelection)
        selectAllAction.triggered.connect(self.selectAll)

        self.selectionModel = table.selectionModel()

        self.statusBar()
        self.setCentralWidget(table)

        self.setWindowTitle(self.tr("Selected Items in a Table Model"))

    def fillSelection(self):

        indexes = self.selectionModel.selectedIndexes()

        for index in indexes:
           text = u"(%i,%i)" % (index.row(), index.column())
           self.model.setData(index, text)

    def clearSelection(self):

        indexes = self.selectionModel.selectedIndexes()

        for index in indexes:
           self.model.setData(index, "")

    def selectAll(self):

        parent = QModelIndex()

        topLeft = self.model.index(0, 0, parent)
        bottomRight = self.model.index(
                         self.model.rowCount(parent) - 1,
                         self.model.columnCount(parent) - 1, parent)

        selection = QtSql.QSqlTableModel.QItemSelection(topLeft, bottomRight)
        self.selectionModel.select(selection, QModelIndex.QItemSelectionModel.Select)

def movF():
    source = '/path/to/source_folder'
    dest1 = '/path/to/dest_folder'

    files = os.listdir(source)

    for f in files:
        shutil.move(source + f, dest1)

if __name__ == "__main__":

   app = QtWidgets.QApplication(sys.argv)
   window = Window()
   window.show()
   sys.exit(app.exec_())