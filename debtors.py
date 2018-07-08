# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debtors.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_Debtors(object):
    def setupUi(self, Debtors):
        Debtors.setObjectName("Debtors")
        Debtors.resize(929, 584)
        self.groupBox = QtWidgets.QGroupBox(Debtors)
        self.groupBox.setGeometry(QtCore.QRect(40, -10, 851, 91))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btnSearch = QtWidgets.QPushButton(self.groupBox)
        self.btnSearch.setGeometry(QtCore.QRect(370, 40, 99, 31))
        self.btnSearch.setObjectName("btnSearch")
        self.btnEdit = QtWidgets.QPushButton(self.groupBox)
        self.btnEdit.setGeometry(QtCore.QRect(620, 40, 111, 31))
        self.btnEdit.setStyleSheet("")
        self.btnEdit.setObjectName("btnEdit")
        self.search = QtWidgets.QLineEdit(self.groupBox)
        self.search.setGeometry(QtCore.QRect(20, 40, 351, 31))
        self.search.setObjectName("search")
        self.btnDelete = QtWidgets.QPushButton(self.groupBox)
        self.btnDelete.setGeometry(QtCore.QRect(750, 40, 81, 31))
        self.btnDelete.setStyleSheet("")
        self.btnDelete.setObjectName("btnDelete")
        self.btnNewDebtor = QtWidgets.QPushButton(self.groupBox)
        self.btnNewDebtor.setGeometry(QtCore.QRect(480, 40, 121, 31))
        self.btnNewDebtor.setStyleSheet("")
        self.btnNewDebtor.setObjectName("btnNewDebtor")
        self.debtorView = QtWidgets.QTableView(Debtors)
        self.debtorView.setGeometry(QtCore.QRect(40, 80, 851, 441))
        self.debtorView.setObjectName("debtorView")
        self.btnClose = QtWidgets.QPushButton(Debtors)
        self.btnClose.setGeometry(QtCore.QRect(790, 530, 99, 41))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(Debtors)
        self.btnClose.clicked.connect(Debtors.close)
        QtCore.QMetaObject.connectSlotsByName(Debtors)

    def retranslateUi(self, Debtors):
        _translate = QtCore.QCoreApplication.translate
        Debtors.setWindowTitle(_translate("Debtors", "Ahasaniya Enterprise | Debtors"))
        self.btnSearch.setText(_translate("Debtors", "Search"))
        self.btnEdit.setText(_translate("Debtors", "Edit Debtor"))
        self.btnDelete.setText(_translate("Debtors", "Delete"))
        self.btnNewDebtor.setText(_translate("Debtors", "New Debtor"))
        self.btnClose.setText(_translate("Debtors", "Close"))

    def display_debtors(self):
        sql.connectDB()
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("debts")
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Phone")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "City")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Area")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Address")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Product")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Paid")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Owed")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Total")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Quantity")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal, "Due")
        self.model.select()
        self.debtorView.setModel(self.model)
        self.debtorView.horizontalHeader().setMinimumHeight(40)
        self.debtorView.horizontalHeader().setStyleSheet("background-color:#222;color:#dadada;")
        self.debtorView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.debtorView.setColumnHidden(0, True)
        self.debtorView.show()

    def deleteSelected(self):
        self.selected_row = self.debtorView.selectionModel()

    def get_debtor(self):

        if self.search.text() == '' or self.search.text().isspace():
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Enter search query"), QtWidgets.qApp.tr(
                "Please enter search criterion to search!"), QtWidgets.QMessageBox.Ok)
        else:
            qry = QtSql.QSqlQuery()
            qry.prepare("select * from debts where customer_name LIKE '%{0}%' or product_name LIKE '%{0}%' or "
                        "city LIKE '%{0}%' or area LIKE '%{0}%' or address LIKE '%{0}%' or due_date LIKE '%{0}%'".format(
                str(self.search.text())))
            # qry.bindValue(0, str(self.search.text()))
            if qry.exec_():
                my_model = QtSql.QSqlQueryModel()
                my_model.setQuery(qry)
                my_model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
                my_model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
                my_model.setHeaderData(2, QtCore.Qt.Horizontal, "Phone")
                my_model.setHeaderData(3, QtCore.Qt.Horizontal, "City")
                my_model.setHeaderData(4, QtCore.Qt.Horizontal, "Area")
                my_model.setHeaderData(5, QtCore.Qt.Horizontal, "Address")
                my_model.setHeaderData(6, QtCore.Qt.Horizontal, "Product")
                my_model.setHeaderData(7, QtCore.Qt.Horizontal, "Paid")
                my_model.setHeaderData(8, QtCore.Qt.Horizontal, "Owed")
                my_model.setHeaderData(9, QtCore.Qt.Horizontal, "Total")
                my_model.setHeaderData(10, QtCore.Qt.Horizontal, "Quantity")
                my_model.setHeaderData(11, QtCore.Qt.Horizontal, "Due Date")
                self.debtorView.setModel(my_model)
                self.debtorView.setColumnHidden(0, True)
                self.debtorView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.debtorView.show()