# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creditors.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_Creditors(object):
    def setupUi(self, Creditors):
        Creditors.setObjectName("Creditors")
        Creditors.resize(931, 585)
        Creditors.setMaximumSize(QtCore.QSize(931, 585))
        self.groupBox = QtWidgets.QGroupBox(Creditors)
        self.groupBox.setGeometry(QtCore.QRect(40, -10, 851, 91))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btnSearch = QtWidgets.QPushButton(self.groupBox)
        self.btnSearch.setGeometry(QtCore.QRect(370, 40, 99, 31))
        self.btnSearch.setObjectName("btnSearch")
        self.btnEdit = QtWidgets.QPushButton(self.groupBox)
        self.btnEdit.setGeometry(QtCore.QRect(630, 40, 111, 31))
        self.btnEdit.setStyleSheet("")
        self.btnEdit.setObjectName("btnEdit")
        self.search_query = QtWidgets.QLineEdit(self.groupBox)
        self.search_query.setGeometry(QtCore.QRect(20, 40, 351, 31))
        self.search_query.setObjectName("search")
        self.btnDelete = QtWidgets.QPushButton(self.groupBox)
        self.btnDelete.setGeometry(QtCore.QRect(750, 40, 81, 31))
        self.btnDelete.setStyleSheet("")
        self.btnDelete.setObjectName("btnDelete")
        self.btnNewCreditor = QtWidgets.QPushButton(self.groupBox)
        self.btnNewCreditor.setGeometry(QtCore.QRect(480, 40, 121, 31))
        self.btnNewCreditor.setStyleSheet("")
        self.btnNewCreditor.setObjectName("btnNewCreditor")
        self.creditorView = QtWidgets.QTableView(Creditors)
        self.creditorView.setGeometry(QtCore.QRect(40, 80, 851, 441))
        self.creditorView.setObjectName("creditorView")
        self.btnClose = QtWidgets.QPushButton(Creditors)
        self.btnClose.setGeometry(QtCore.QRect(790, 530, 99, 41))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(Creditors)
        self.btnClose.clicked.connect(Creditors.close)
        QtCore.QMetaObject.connectSlotsByName(Creditors)

    def retranslateUi(self, Creditors):
        _translate = QtCore.QCoreApplication.translate
        Creditors.setWindowTitle(_translate("Creditors", "Creditors"))
        self.btnSearch.setText(_translate("Creditors", "Search"))
        self.btnEdit.setText(_translate("Creditors", "Edit Creditor"))
        self.btnDelete.setText(_translate("Creditors", "Delete"))
        self.btnNewCreditor.setText(_translate("Creditors", "New Creditor"))
        self.btnClose.setText(_translate("Creditors", "Close"))


    def display_creditors(self):
        sql.connectDB()
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("creditors")
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Phone")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Product")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Amount Paid")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Amount Owed")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Total")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Quantity")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Due Date")
        self.model.select()
        self.creditorView.setModel(self.model)
        self.creditorView.horizontalHeader().setMinimumHeight(40)
        self.creditorView.horizontalHeader().setStyleSheet("background-color:#222;color:#dadada;")
        self.creditorView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.creditorView.horizontalHeader().setDefaultSectionSize(120)
        self.creditorView.setColumnHidden(0, True)
        self.creditorView.show()

    def get_creditor(self):

        if self.search_query.text() == '' or self.search_query.text().isspace():
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Enter search query"), QtWidgets.qApp.tr(
                "Please enter search criterion to search!"), QtWidgets.QMessageBox.Ok)
        else:
            qry = QtSql.QSqlQuery()
            qry.prepare("select * from creditors where creditor_name LIKE '%{0}%' or product_name LIKE '%{0}%' or "
                        "due_date LIKE '%{0}%'".format(str(self.search_query.text())))

            if qry.exec_():
                self.model = QtSql.QSqlQueryModel()
                self.model.setQuery(qry)
                self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
                self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
                self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Phone")
                self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Product")
                self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Amount Paid")
                self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Amount Owed")
                self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Total")
                self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Quantity")
                self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Due")
                self.model.select()
                self.creditorView.setModel(self.model)
                self.creditorView.horizontalHeader().setMinimumHeight(40)
                self.creditorView.horizontalHeader().setStyleSheet("background-color:#222;color:#dadada;")
                self.creditorView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.creditorView.setColumnHidden(0, True)
                self.creditorView.show()
                self.creditorView.setModel(self.model)
                self.creditorView.setColumnHidden(0, True)
                self.creditorView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.creditorView.show()
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Creditors = QtWidgets.QDialog()
    ui = Ui_Creditors()
    ui.setupUi(Creditors)
    ui.display_creditors()
    Creditors.show()
    sys.exit(app.exec_())

