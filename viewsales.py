# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/viewsales.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sqlite3
import sql
from time import strftime, gmtime
from functions import num_rows

class Ui_ViewSales(object):
    def setupUi(self, ViewSales):
        ViewSales.setObjectName("ViewSales")
        ViewSales.resize(839, 613)
        self.gridLayout_2 = QtWidgets.QGridLayout(ViewSales)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(ViewSales)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.specificDay = QtWidgets.QLineEdit(self.groupBox)
        self.specificDay.setStyleSheet("width:90px;\n"
"min-height:23px;")
        self.specificDay.setObjectName("specificDay")
        self.gridLayout.addWidget(self.specificDay, 1, 1, 1, 1)
        self.btnLoad = QtWidgets.QPushButton(self.groupBox)
        self.btnLoad.setStyleSheet("max-width:90px;\n"
"min-height:20px;")
        self.btnLoad.setObjectName("btnLoad")
        self.gridLayout.addWidget(self.btnLoad, 1, 2, 1, 1)
        self.btnToday = QtWidgets.QPushButton(self.groupBox)
        self.btnToday.setStyleSheet("max-width:90px;\n"
"min-height:20px;")
        self.btnToday.setObjectName("btnToday")
        self.gridLayout.addWidget(self.btnToday, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(ViewSales)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("max-width:120px;")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.btlTotal = QtWidgets.QLabel(ViewSales)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btlTotal.setFont(font)
        self.btlTotal.setStyleSheet("color: rgb(0, 85, 0);")
        self.btlTotal.setText("")
        self.btlTotal.setObjectName("btlTotal")
        self.gridLayout_2.addWidget(self.btlTotal, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(ViewSales)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(ViewSales)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 85, 0);\n"
"max-width:45px;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 1)
        self.lblAmount = QtWidgets.QLabel(ViewSales)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblAmount.setFont(font)
        self.lblAmount.setStyleSheet("color: rgb(0, 85, 0);")
        self.lblAmount.setObjectName("lblAmount")
        self.gridLayout_2.addWidget(self.lblAmount, 1, 4, 1, 1)
        self.allSalesView = QtWidgets.QTableView(ViewSales)
        self.allSalesView.setObjectName("allSalesView")
        self.gridLayout_2.addWidget(self.allSalesView, 2, 0, 1, 5)
        self.btnClose = QtWidgets.QPushButton(ViewSales)
        self.btnClose.setObjectName("btnClose")
        self.gridLayout_2.addWidget(self.btnClose, 3, 4, 1, 1)

        self.retranslateUi(ViewSales)
        self.btnClose.clicked.connect(ViewSales.close)
        self.update_view()
        self.btnToday.clicked.connect(lambda: self.select_sales_today())
        self.btnLoad.clicked.connect(lambda: self.select_on_date())
        QtCore.QMetaObject.connectSlotsByName(ViewSales)

    def retranslateUi(self, ViewSales):
        _translate = QtCore.QCoreApplication.translate
        ViewSales.setWindowTitle(_translate("ViewSales", "View sales by date"))
        self.groupBox.setTitle(_translate("ViewSales", "View Sales"))
        self.btnToday.setText(_translate("ViewSales", "Today"))
        self.label.setText(_translate("ViewSales", "Date:"))
        self.btnLoad.setText(_translate("ViewSales", "Load"))
        self.label_2.setText(_translate("ViewSales", "Total Sales:"))
        self.label_3.setText(_translate("ViewSales", "Total Amount From Sales:"))
        self.label_4.setText(_translate("ViewSales", "GHC"))
        self.lblAmount.setText(_translate("ViewSales", "45.00"))
        self.btnClose.setText(_translate("ViewSales", "Close"))

    def update_view(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        con = sqlite3.connect("ims.db")
        cursor = con.cursor()
        cursor.execute("select sum(amount_paid) from sales")
        rows = cursor.fetchall()
        if len(rows) > 0:
            self.lblAmount.setText(str(rows[0][0]))
        else:
            self.lblAmount.setText("0")

        model.setTable("sales")
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Product Name")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Quantity")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Amount Paid")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Date")
        model.select()
        self.btlTotal.setText(str(model.rowCount()))
        self.allSalesView.setModel(model)
        self.allSalesView.horizontalHeader().setMinimumHeight(40)
        self.allSalesView.horizontalHeader().setDefaultSectionSize(180)
        self.allSalesView.setColumnHidden(0, True)
        self.allSalesView.setColumnHidden(6, True)
        self.allSalesView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.allSalesView.setShowGrid(True)
        self.allSalesView.show()

    def select_sales_today(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        q = QtSql.QSqlQuery()
        today = strftime("%d/%m/%Y", gmtime())

        q.prepare("select * from sales where date_bought = ?")
        q.bindValue(0, today)
        if q.exec_():
            con = sqlite3.connect("ims.db")
            cursor = con.cursor()
            cursor.execute("select sum(amount_paid) from sales where date_bought = '{0}'".format(today))
            row = cursor.fetchall()
            if row[0][0] == None:
                self.lblAmount.setText(str(0))
            else:
                self.lblAmount.setText(str(row[0][0]))

            model.setQuery(q)
            model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            model.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
            model.setHeaderData(2, QtCore.Qt.Horizontal, "Product Name")
            model.setHeaderData(4, QtCore.Qt.Horizontal, "Quantity")
            model.setHeaderData(3, QtCore.Qt.Horizontal, "Amount Paid")
            model.setHeaderData(5, QtCore.Qt.Horizontal, "Date")
            self.allSalesView.setModel(model)
            self.btlTotal.setText(str(model.rowCount()))
            self.allSalesView.horizontalHeader().setMinimumHeight(40)
            self.allSalesView.horizontalHeader().setDefaultSectionSize(180)
            self.allSalesView.setColumnHidden(0, True)
            self.allSalesView.setColumnHidden(6, True)
            self.allSalesView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            self.allSalesView.setShowGrid(True)
            self.allSalesView.show()

    def select_on_date(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        q = QtSql.QSqlQuery()
        i_date = self.specificDay.text()
        q.prepare("select * from sales where date_bought = ?")
        q.bindValue(0, i_date)
        if q.exec_():
            con = sqlite3.connect("ims.db")
            cursor = con.cursor()
            cursor.execute("select sum(amount_paid) from sales where date_bought = '{0}'".format(i_date))
            row = cursor.fetchall()
            if row[0][0] == None:
                self.lblAmount.setText(str(0))
            else:
                self.lblAmount.setText(str(row[0][0]))

            model.setQuery(q)
            model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            model.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
            model.setHeaderData(2, QtCore.Qt.Horizontal, "Product Name")
            model.setHeaderData(4, QtCore.Qt.Horizontal, "Quantity")
            model.setHeaderData(3, QtCore.Qt.Horizontal, "Amount Paid")
            model.setHeaderData(5, QtCore.Qt.Horizontal, "Date")
            self.allSalesView.setModel(model)
            self.btlTotal.setText(str(model.rowCount()))
            self.allSalesView.horizontalHeader().setMinimumHeight(40)
            self.allSalesView.horizontalHeader().setDefaultSectionSize(180)
            self.allSalesView.setColumnHidden(0, True)
            self.allSalesView.setColumnHidden(6, True)
            self.allSalesView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            self.allSalesView.setShowGrid(True)
            self.allSalesView.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ViewSales = QtWidgets.QDialog()
    ui = Ui_ViewSales()
    ui.setupUi(ViewSales)
    ViewSales.show()
    sys.exit(app.exec_())
