# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formcreditor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_DialogCreditor(object):
    def setupUi(self, DialogCreditor):
        DialogCreditor.setObjectName("DialogCreditor")
        DialogCreditor.resize(474, 432)
        self.label_2 = QtWidgets.QLabel(DialogCreditor)
        self.label_2.setGeometry(QtCore.QRect(30, 56, 44, 27))
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(DialogCreditor)
        self.name.setGeometry(QtCore.QRect(80, 56, 146, 27))
        self.name.setObjectName("name")
        self.lblPhone = QtWidgets.QLabel(DialogCreditor)
        self.lblPhone.setGeometry(QtCore.QRect(240, 56, 48, 27))
        self.lblPhone.setObjectName("lblPhone")
        self.phone = QtWidgets.QLineEdit(DialogCreditor)
        self.phone.setGeometry(QtCore.QRect(290, 56, 151, 27))
        self.phone.setObjectName("phone")
        self.productName = QtWidgets.QLineEdit(DialogCreditor)
        self.productName.setGeometry(QtCore.QRect(140, 110, 301, 27))
        self.productName.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.productName.setObjectName("productName")
        self.lblAmountPaid = QtWidgets.QLabel(DialogCreditor)
        self.lblAmountPaid.setGeometry(QtCore.QRect(30, 170, 92, 27))
        self.lblAmountPaid.setToolTip("")
        self.lblAmountPaid.setProperty("toolTipDuration", 2)
        self.lblAmountPaid.setObjectName("lblAmountPaid")
        self.amountPaid = QtWidgets.QLineEdit(DialogCreditor)
        self.amountPaid.setGeometry(QtCore.QRect(130, 170, 311, 27))
        self.amountPaid.setObjectName("amountPaid")
        self.lblAmount = QtWidgets.QLabel(DialogCreditor)
        self.lblAmount.setGeometry(QtCore.QRect(30, 230, 103, 27))
        self.lblAmount.setObjectName("lblAmount")
        self.amountOwed = QtWidgets.QLineEdit(DialogCreditor)
        self.amountOwed.setGeometry(QtCore.QRect(160, 230, 281, 27))
        self.amountOwed.setObjectName("amountOwed")
        self.lblTotal = QtWidgets.QLabel(DialogCreditor)
        self.lblTotal.setGeometry(QtCore.QRect(30, 286, 38, 27))
        self.lblTotal.setObjectName("lblTotal")
        self.total = QtWidgets.QLineEdit(DialogCreditor)
        self.total.setGeometry(QtCore.QRect(80, 286, 145, 27))
        self.total.setObjectName("total")
        self.quantity = QtWidgets.QLineEdit(DialogCreditor)
        self.quantity.setGeometry(QtCore.QRect(320, 286, 119, 27))
        self.quantity.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.quantity.setObjectName("quantity")
        self.dueDate = QtWidgets.QDateEdit(DialogCreditor)
        self.dueDate.setGeometry(QtCore.QRect(100, 340, 341, 27))
        self.dueDate.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dueDate.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.dueDate.setMinimumDate(QtCore.QDate(2018, 6, 20))
        self.dueDate.setCalendarPopup(True)
        self.dueDate.setObjectName("dueDate")
        self.label = QtWidgets.QLabel(DialogCreditor)
        self.label.setGeometry(QtCore.QRect(-10, -4, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(DialogCreditor)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 102, 27))
        self.label_3.setObjectName("label_3")
        self.lblQuantity_2 = QtWidgets.QLabel(DialogCreditor)
        self.lblQuantity_2.setGeometry(QtCore.QRect(240, 286, 64, 27))
        self.lblQuantity_2.setObjectName("lblQuantity_2")
        self.btnCancel = QtWidgets.QPushButton(DialogCreditor)
        self.btnCancel.setGeometry(QtCore.QRect(50, 381, 99, 31))
        self.btnCancel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnCancel.setObjectName("btnCancel")
        self.lblDueDate = QtWidgets.QLabel(DialogCreditor)
        self.lblDueDate.setGeometry(QtCore.QRect(30, 336, 53, 27))
        self.lblDueDate.setObjectName("lblDueDate")
        self.btnSave = QtWidgets.QPushButton(DialogCreditor)
        self.btnSave.setGeometry(QtCore.QRect(360, 381, 81, 31))
        self.btnSave.setStyleSheet("background-color: rgb(0, 0, 175);\n"
"color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 0, 255);\n"
"selection-background-color: rgb(0, 0, 232);")
        self.btnSave.setObjectName("btnSave")
        sql.connectDB()
        complet = QtWidgets.QCompleter()
        complet.setFilterMode(QtCore.Qt.MatchContains)
        complet.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        complet.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        qery = QtSql.QSqlQuery()
        qery.exec_("select product_name from products")
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(qery)
        self.productName.setCompleter(complet)
        complet.setModel(modal)

        completer = QtWidgets.QCompleter()
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        query = QtSql.QSqlQuery()
        query.exec_("select name, phone from customers")
        modl = QtSql.QSqlQueryModel()
        modl.setQuery(query)
        self.name.setCompleter(completer)
        completer.setModel(modl)
        completer.setCompletionColumn(0)

        completor = QtWidgets.QCompleter()
        completor.setFilterMode(QtCore.Qt.MatchContains)
        completor.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completor.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.phone.setCompleter(completor)
        completor.setModel(modl)
        completor.setCompletionColumn(1)
        self.retranslateUi(DialogCreditor)
        QtCore.QMetaObject.connectSlotsByName(DialogCreditor)

    def retranslateUi(self, DialogCreditor):
        _translate = QtCore.QCoreApplication.translate
        DialogCreditor.setWindowTitle(_translate("DialogCreditor", "New creditor details"))
        self.label_2.setText(_translate("DialogCreditor", "Name:"))
        self.lblAmount.setText(_translate("DialogCreditor", "Amount Owed:"))
        self.lblTotal.setText(_translate("DialogCreditor", "Total:"))
        self.lblPhone.setText(_translate("DialogCreditor", "Phone:"))
        self.label.setText(_translate("DialogCreditor", "Creditor Information"))
        self.lblAmountPaid.setText(_translate("DialogCreditor", "Amount Paid:"))
        self.label_3.setText(_translate("DialogCreditor", "Product Name:"))
        self.lblQuantity_2.setText(_translate("DialogCreditor", "Quantity:"))
        self.btnCancel.setText(_translate("DialogCreditor", "Cancel"))
        self.lblDueDate.setText(_translate("DialogCreditor", "Due on:"))
        self.btnSave.setText(_translate("DialogCreditor", "Save"))

    def validate(self):
        error = 0
        if self.name.text() == '' or self.name.text().isspace():
            error = 1

        if self.productName.text() == '' or self.productName.text().isspace():
            error = 4
        if self.phone.text() == '' or self.phone.text().isspace():
            error = 5

        if self.amountOwed.text() == '' or self.amountOwed.text().isspace():
            error = 6
        if self.amountPaid.text() == '' or self.amountPaid.text().isspace():
            error = 7
        if self.total.text() == '' or self.total.text().isspace():
            error = 8
        if self.quantity.text() == '' or self.quantity.text().isspace():
            error = 9
        if self.dueDate.text() == '' or self.dueDate.text().isspace():
            error = 11

        if (self.name.text() == '' or self.name.text().isspace()) and (self.productName.text() == '' or
            self.productName.text().isspace()) and (self.phone.text() == '' or self.phone.text().isspace()) and (
                self.dueDate.text() == '' or self.dueDate.text().isspace()) and (self.quantity.text() == '' or
                self.quantity.text().isspace()) and (self.total.text() == '' or self.total.text().isspace()) and (
                self.amountPaid.text() == '' or self.amountPaid.text().isspace()) and(
            self.amountOwed.text() == '' or self.amountOwed.text().isspace()):
            error = 12

        if error == 0:
            self.insert_data()
        else:
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("There are blank fields"),
                                           QtWidgets.qApp.tr("\nPlease some fields are blank!, "
                                                             "fill them to continue"),
                                           QtWidgets.QMessageBox.Ok)

    def insert_data(self):
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO creditors(creditor_name,phone,product_name,amount_paid, amount_owed,total, quantity,"
                          "due_date) VALUES(?,?,?,?,?,?,?,?)")
            query.bindValue(0, self.name.text())
            query.bindValue(1, self.phone.text())
            query.bindValue(2, self.productName.text())
            query.bindValue(3, self.amountPaid.text())
            query.bindValue(4, self.amountOwed.text())
            query.bindValue(5, self.total.text())
            query.bindValue(6, self.quantity.text())
            query.bindValue(7, self.dueDate.text())
            if query.exec_():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Save Successful"),
                                                  QtWidgets.qApp.tr("\nCreditor has been created"),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Successful"),
                                                  QtWidgets.qApp.tr("Data could not be saved successfully"),
                                                  QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cred = QtWidgets.QDialog()
    ui = Ui_DialogCreditor()
    ui.setupUi(Cred)
    Cred.show()
    sys.exit(app.exec_())