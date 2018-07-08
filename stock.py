# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_Stock(object):
    def setupUi(self, Stock):
        Stock.setObjectName("Stock")
        Stock.resize(395, 251)
        self.productName = QtWidgets.QComboBox(Stock)
        self.productName.setGeometry(QtCore.QRect(150, 16, 171, 27))
        self.productName.setObjectName("productName")
        self.label = QtWidgets.QLabel(Stock)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Stock)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 101, 17))
        self.label_2.setObjectName("label_2")
        self.txtQuantity = QtWidgets.QLabel(Stock)
        self.txtQuantity.setGeometry(QtCore.QRect(150, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtQuantity.setFont(font)
        self.txtQuantity.setObjectName("txtQuantity")
        self.label_3 = QtWidgets.QLabel(Stock)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 101, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Stock)
        self.lineEdit.setGeometry(QtCore.QRect(140, 116, 211, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.btnUpdate = QtWidgets.QPushButton(Stock)
        self.btnUpdate.setGeometry(QtCore.QRect(190, 190, 121, 41))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnClose = QtWidgets.QPushButton(Stock)
        self.btnClose.setGeometry(QtCore.QRect(60, 190, 99, 41))
        self.btnClose.setObjectName("btnClose")
        self.lblError = QtWidgets.QLabel(Stock)
        self.lblError.setGeometry(QtCore.QRect(30, 160, 321, 17))
        self.lblError.setText("")
        self.lblError.setObjectName("lblError")
        self.btnRefresh = QtWidgets.QPushButton(Stock)
        self.btnRefresh.setGeometry(QtCore.QRect(320, 16, 30, 28))
        self.btnRefresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/Apply_16x16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon)
        self.btnRefresh.setIconSize(QtCore.QSize(20, 20))
        self.btnRefresh.setObjectName("btnRefresh")

        self.retranslateUi(Stock)
        QtCore.QMetaObject.connectSlotsByName(Stock)

    def retranslateUi(self, Stock):
        _translate = QtCore.QCoreApplication.translate
        Stock.setWindowTitle(_translate("Stock", "New Stock"))
        self.label.setText(_translate("Stock", "Select Product:"))
        self.label_2.setText(_translate("Stock", "Old Quantity:"))
        self.txtQuantity.setText(_translate("Stock", "0"))
        self.label_3.setText(_translate("Stock", "New Quantity:"))
        self.btnUpdate.setText(_translate("Stock", "Update Stock"))
        self.btnClose.setText(_translate("Stock", "Close"))

    def selectStock(self):
        if sql.connectDB():
            model = QtSql.QSqlQueryModel()
            query = QtSql.QSqlQuery()
            query.exec_("select product_name from products")
            model.setQuery(query)
            self.productName.setModel(model)

    def details(self):
        model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        query.exec_("select product_price from products")
        model.setQuery(query)
        self.txtQuantity.setText(str(query.result()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stock = QtWidgets.QDialog()
    ui = Ui_Stock()
    ui.setupUi(Stock)
    ui.btnRefresh.clicked.connect(ui.details)
    ui.selectStock()
    Stock.show()
    sys.exit(app.exec_())

