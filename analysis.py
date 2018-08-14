# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/analysis'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sqlite3
import sql
from functions import num_rows

class Ui_Analysis(object):
    def setupUi(self, Analysis):
        Analysis.setObjectName("Analysis")
        Analysis.resize(822, 640)
        self.gridLayout = QtWidgets.QGridLayout(Analysis)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Analysis)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, -590, 789, 1210))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_10 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:3px;\n"
"max-height:250px;\n"
"min-height:200px;")
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lblSuppliers = QtWidgets.QLabel(self.groupBox_10)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblSuppliers.setFont(font)
        self.lblSuppliers.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);")
        self.lblSuppliers.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblSuppliers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblSuppliers.setScaledContents(True)
        self.lblSuppliers.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSuppliers.setObjectName("lblSuppliers")
        self.gridLayout_7.addWidget(self.lblSuppliers, 0, 0, 2, 1)
        self.lblEmployees = QtWidgets.QLabel(self.groupBox_10)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblEmployees.setFont(font)
        self.lblEmployees.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.lblEmployees.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblEmployees.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblEmployees.setScaledContents(True)
        self.lblEmployees.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEmployees.setObjectName("lblEmployees")
        self.gridLayout_7.addWidget(self.lblEmployees, 0, 2, 2, 1)
        self.lblCustomers = QtWidgets.QLabel(self.groupBox_10)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCustomers.setFont(font)
        self.lblCustomers.setStyleSheet("color:#fff;\n"
"background-color: rgb(85, 0, 127);")
        self.lblCustomers.setScaledContents(True)
        self.lblCustomers.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCustomers.setWordWrap(True)
        self.lblCustomers.setObjectName("lblCustomers")
        self.gridLayout_7.addWidget(self.lblCustomers, 0, 4, 2, 1)
        self.lblCustomers.raise_()
        self.lblSuppliers.raise_()
        self.lblEmployees.raise_()
        self.gridLayout_3.addWidget(self.groupBox_10, 6, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:3px;\n"
"max-height:250px;\n"
"min-height:200px;")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_5.setContentsMargins(10, 20, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblInStock = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblInStock.setFont(font)
        self.lblInStock.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(171, 171, 0);")
        self.lblInStock.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblInStock.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblInStock.setScaledContents(True)
        self.lblInStock.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInStock.setObjectName("lblInStock")
        self.gridLayout_5.addWidget(self.lblInStock, 1, 0, 1, 1)
        self.lblOutStock = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblOutStock.setFont(font)
        self.lblOutStock.setStyleSheet("color:#fff;\n"
"background-color: rgb(170, 0, 0);")
        self.lblOutStock.setScaledContents(True)
        self.lblOutStock.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutStock.setWordWrap(True)
        self.lblOutStock.setObjectName("lblOutStock")
        self.gridLayout_5.addWidget(self.lblOutStock, 1, 1, 1, 1)
        self.lblTotalProducts = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTotalProducts.setFont(font)
        self.lblTotalProducts.setStyleSheet("color:#fff;\n"
"background-color: rgb(170, 0, 127);")
        self.lblTotalProducts.setScaledContents(True)
        self.lblTotalProducts.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTotalProducts.setWordWrap(True)
        self.lblTotalProducts.setObjectName("lblTotalProducts")
        self.gridLayout_5.addWidget(self.lblTotalProducts, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_7, 2, 0, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:3px;\n"
"min-height:200px;")
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_8.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lblDebtors = QtWidgets.QLabel(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblDebtors.setFont(font)
        self.lblDebtors.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 127);")
        self.lblDebtors.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblDebtors.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblDebtors.setScaledContents(True)
        self.lblDebtors.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDebtors.setObjectName("lblDebtors")
        self.gridLayout_8.addWidget(self.lblDebtors, 0, 0, 2, 2)
        self.lblCreditors = QtWidgets.QLabel(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCreditors.setFont(font)
        self.lblCreditors.setStyleSheet("color:#fff;\n"
"background-color: rgb(0, 0, 0);")
        self.lblCreditors.setScaledContents(True)
        self.lblCreditors.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCreditors.setWordWrap(True)
        self.lblCreditors.setObjectName("lblCreditors")
        self.gridLayout_8.addWidget(self.lblCreditors, 0, 2, 2, 2)
        self.lblCategories = QtWidgets.QLabel(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCategories.setFont(font)
        self.lblCategories.setStyleSheet("color:#fff;\n"
"background-color: rgb(85, 85, 0);")
        self.lblCategories.setScaledContents(True)
        self.lblCategories.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCategories.setWordWrap(True)
        self.lblCategories.setObjectName("lblCategories")
        self.gridLayout_8.addWidget(self.lblCategories, 0, 4, 2, 2)
        self.gridLayout_3.addWidget(self.groupBox_11, 4, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:3px;\n"
"max-height:250px;\n"
"min-height:200px;")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lblLoss = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblLoss.setFont(font)
        self.lblLoss.setStyleSheet("color:#fff;\n"
"background-color: rgb(255, 0, 0);")
        self.lblLoss.setScaledContents(True)
        self.lblLoss.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLoss.setWordWrap(True)
        self.lblLoss.setObjectName("lblLoss")
        self.gridLayout_6.addWidget(self.lblLoss, 0, 2, 2, 2)
        self.lblProfit = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblProfit.setFont(font)
        self.lblProfit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 0);")
        self.lblProfit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblProfit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblProfit.setScaledContents(True)
        self.lblProfit.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProfit.setObjectName("lblProfit")
        self.gridLayout_6.addWidget(self.lblProfit, 0, 0, 2, 2)
        self.lblTotalSales = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTotalSales.setFont(font)
        self.lblTotalSales.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.lblTotalSales.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTotalSales.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblTotalSales.setScaledContents(True)
        self.lblTotalSales.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTotalSales.setObjectName("lblTotalSales")
        self.gridLayout_6.addWidget(self.lblTotalSales, 0, 4, 2, 2)
        self.lblTotalSales.raise_()
        self.lblProfit.raise_()
        self.lblLoss.raise_()
        self.gridLayout_3.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:3px;\n"
"max-height:250px;\n"
"min-height:200px;")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setContentsMargins(10, 20, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblOutwards = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblOutwards.setFont(font)
        self.lblOutwards.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.lblOutwards.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblOutwards.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblOutwards.setScaledContents(True)
        self.lblOutwards.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutwards.setObjectName("lblOutwards")
        self.gridLayout_2.addWidget(self.lblOutwards, 1, 0, 1, 1)
        self.lblInwards = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblInwards.setFont(font)
        self.lblInwards.setStyleSheet("color:#fff;\n"
"background-color: rgb(255, 0, 127);")
        self.lblInwards.setScaledContents(True)
        self.lblInwards.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInwards.setWordWrap(True)
        self.lblInwards.setObjectName("lblInwards")
        self.gridLayout_2.addWidget(self.lblInwards, 1, 1, 1, 1)
        self.lblTotalReturns = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTotalReturns.setFont(font)
        self.lblTotalReturns.setStyleSheet("color:#fff;\n"
"background-color: rgb(107, 71, 0);")
        self.lblTotalReturns.setScaledContents(True)
        self.lblTotalReturns.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTotalReturns.setWordWrap(True)
        self.lblTotalReturns.setObjectName("lblTotalReturns")
        self.gridLayout_2.addWidget(self.lblTotalReturns, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_6, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        Analysis.setStyleSheet(
            "QLabel{"
            "font-size:22px;"
            "}"
        )
        self.retranslateUi(Analysis)
        QtCore.QMetaObject.connectSlotsByName(Analysis)

    def retranslateUi(self, Analysis):
        _translate = QtCore.QCoreApplication.translate
        Analysis.setWindowTitle(_translate("Analysis", "Store analysis"))
        self.groupBox_10.setTitle(_translate("Analysis", "Suppliers, Staff and Customers"))
        self.groupBox_11.setTitle(_translate("Analysis", "Debtors, Creditors, Categories"))
        self.groupBox_5.setTitle(_translate("Analysis", "Profit, loss and sales"))
        self.groupBox_6.setTitle(_translate("Analysis", "Returns"))
        self.lblCreditors.setText(str(get_total("creditors")) + "\n\nCreditors")
        self.lblCustomers.setText(str(get_total("customers")) + "\n\nCustomers")
        self.lblEmployees.setText(str(get_total("users")) + "\n\nUsers")
        self.lblOutwards.setText(str(get_constraint_total("returns", "return_type", "Outward")) + "\n\nOutward")
        self.lblInwards.setText(str(get_constraint_total("returns", "return_type", "Inward")) + "\n\nInward")
        self.lblTotalReturns.setText(str(get_total("returns")) + "\n\nTotal")
        self.lblTotalReturns.setText(str(get_total("returns")) + "\n\nTotal Returns")
        self.lblTotalSales.setText(str(get_total("sales")) + "\n\nSales")
        self.lblCategories.setText(str(get_total("categories")) + "\n\nCategories")
        self.lblDebtors.setText(str(get_total("debtors")) + "\n\nDebtors")
        self.lblSuppliers.setText(str(get_total("suppliers")) + "\n\nSuppliers")
        self.lblInStock.setText(str(get_greater_total("products", "quantity", "0")) + "\n\nIn Stock")
        self.lblOutStock.setText(str(get_lesser_total("products", "quantity", "1")) + "\n\nOut of Stock")
        self.lblTotalProducts.setText(str(get_total("products")) + "\n\nProducts")
        outcome = get_profit()
        if outcome > 0:
            profit = str(outcome)
            loss = str(0)
        else:
            loss = str(outcome)
            profit = str(0)

        self.lblProfit.setText(profit + "\n\nTotal Profit")
        self.lblLoss.setText(loss + "\n\nTotal Loss")

def get_total(table):
    if sql.connectDB():
        query = QtSql.QSqlQuery()
        query.exec_("SELECT id FROM {0}".format(str(table)))
        if num_rows(query) == -1:
            rows = 0
        else:
            rows = num_rows(query)
        return rows


def get_greater_total(table, constraint, value):
    if sql.connectDB():
        query = QtSql.QSqlQuery()
        query.exec_("SELECT * FROM {0} WHERE {1} > {2}".format(str(table),str(constraint), value))
        if num_rows(query) == -1:
            rows = 0
        else:
            rows = num_rows(query)
        return rows


def get_lesser_total(table, constraint, value):
    if sql.connectDB():
        query = QtSql.QSqlQuery()
        query.exec_("SELECT * FROM {0} WHERE {1} < {2}".format(str(table),str(constraint), value))
        if num_rows(query) == -1:
            rows = 0
        else:
            rows = num_rows(query)
        return rows


def get_constraint_total(table, key, value):
    if sql.connectDB():
        query = QtSql.QSqlQuery()
        query.exec_("SELECT * FROM {0} WHERE {1} = '{2}'".format(str(table), str(key), str(value)))
        if num_rows(query) == -1:
            rows = 0
        else:
            rows = num_rows(query)
        return rows

def get_outward():
    if sql.connectDB():
        query = QtSql.QSqlQuery()
        query.exec_("SELECT * FROM returns WHERE return_type = 'Outward'")
        if not num_rows(query):
            rows = 0
        else:
            rows = num_rows(query)
        return rows


def get_profit():
    connection = sqlite3.connect("ims.db")
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT sum(amount_paid), sum(quantity) FROM sales")
        rows = cursor.fetchall()
        if len(rows) > 0:
            cursor.execute("select sum(real_price) from products")
            row = cursor.fetchall()
            total = round(float(rows[0][0]) - (int(row[0][0])), 2)
            return total

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Analysis = QtWidgets.QDialog()
    ui = Ui_Analysis()
    ui.setupUi(Analysis)
    Analysis.show()
    sys.exit(app.exec_())
