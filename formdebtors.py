# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formdebtors.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_FormDebtors(object):
    def setupUi(self, FormDebtors):
        FormDebtors.setObjectName("FormDebtors")
        FormDebtors.resize(452, 444)
        FormDebtors.setMaximumSize(QtCore.QSize(452, 444))
        self.label = QtWidgets.QLabel(FormDebtors)
        self.label.setGeometry(QtCore.QRect(0, 0, 471, 41))
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
        self.phone = QtWidgets.QLineEdit(FormDebtors)
        self.phone.setGeometry(QtCore.QRect(280, 60, 151, 27))
        self.phone.setObjectName("phone")
        self.lblAmountPaid = QtWidgets.QLabel(FormDebtors)
        self.lblAmountPaid.setGeometry(QtCore.QRect(20, 200, 92, 27))
        self.lblAmountPaid.setToolTip("")
        self.lblAmountPaid.setProperty("toolTipDuration", 2)
        self.lblAmountPaid.setObjectName("lblAmountPaid")
        self.lblPhone = QtWidgets.QLabel(FormDebtors)
        self.lblPhone.setGeometry(QtCore.QRect(230, 60, 48, 27))
        self.lblPhone.setObjectName("lblPhone")
        self.productName = QtWidgets.QLineEdit(FormDebtors)
        self.productName.setGeometry(QtCore.QRect(130, 150, 301, 27))
        self.productName.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.productName.setObjectName("productName")
        self.label_2 = QtWidgets.QLabel(FormDebtors)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 44, 27))
        self.label_2.setObjectName("label_2")
        self.lblTotal = QtWidgets.QLabel(FormDebtors)
        self.lblTotal.setGeometry(QtCore.QRect(20, 290, 38, 27))
        self.lblTotal.setObjectName("lblTotal")
        self.btnSave = QtWidgets.QPushButton(FormDebtors)
        self.btnSave.setGeometry(QtCore.QRect(350, 385, 81, 31))
        self.btnSave.setStyleSheet("background-color: rgb(0, 0, 175);\n"
"color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 0, 255);\n"
"selection-background-color: rgb(0, 0, 232);")
        self.btnSave.setObjectName("btnSave")
        self.label_3 = QtWidgets.QLabel(FormDebtors)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 102, 27))
        self.label_3.setObjectName("label_3")
        self.address = QtWidgets.QTextEdit(FormDebtors)
        self.address.setGeometry(QtCore.QRect(20, 344, 201, 71))
        self.address.setObjectName("address")
        self.lblAddress = QtWidgets.QLabel(FormDebtors)
        self.lblAddress.setGeometry(QtCore.QRect(20, 320, 59, 29))
        self.lblAddress.setObjectName("lblAddress")
        self.town = QtWidgets.QLineEdit(FormDebtors)
        self.town.setGeometry(QtCore.QRect(70, 100, 162, 27))
        self.town.setObjectName("town")
        self.dueDate = QtWidgets.QDateEdit(FormDebtors)
        self.dueDate.setGeometry(QtCore.QRect(300, 340, 130, 27))
        self.dueDate.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dueDate.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.dueDate.setMinimumDate(QtCore.QDate(2018, 6, 20))
        self.dueDate.setCalendarPopup(True)
        self.dueDate.setObjectName("dueDate")
        self.quantity = QtWidgets.QLineEdit(FormDebtors)
        self.quantity.setGeometry(QtCore.QRect(310, 290, 119, 27))
        self.quantity.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.quantity.setObjectName("quantity")
        self.lblcustomerTown_2 = QtWidgets.QLabel(FormDebtors)
        self.lblcustomerTown_2.setGeometry(QtCore.QRect(20, 100, 41, 27))
        self.lblcustomerTown_2.setObjectName("lblcustomerTown_2")
        self.lblQuantity_2 = QtWidgets.QLabel(FormDebtors)
        self.lblQuantity_2.setGeometry(QtCore.QRect(230, 290, 64, 27))
        self.lblQuantity_2.setObjectName("lblQuantity_2")
        self.amountPaid = QtWidgets.QLineEdit(FormDebtors)
        self.amountPaid.setGeometry(QtCore.QRect(120, 200, 311, 27))
        self.amountPaid.setObjectName("amountPaid")
        self.btnCancel = QtWidgets.QPushButton(FormDebtors)
        self.btnCancel.setGeometry(QtCore.QRect(230, 385, 99, 31))
        self.btnCancel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnCancel.setObjectName("btnCancel")
        self.lblArea = QtWidgets.QLabel(FormDebtors)
        self.lblArea.setGeometry(QtCore.QRect(240, 100, 36, 27))
        self.lblArea.setObjectName("lblArea")
        self.amountOwed = QtWidgets.QLineEdit(FormDebtors)
        self.amountOwed.setGeometry(QtCore.QRect(150, 240, 281, 27))
        self.amountOwed.setObjectName("amountOwed")
        self.lblAmount = QtWidgets.QLabel(FormDebtors)
        self.lblAmount.setGeometry(QtCore.QRect(20, 240, 103, 27))
        self.lblAmount.setObjectName("lblAmount")
        self.area = QtWidgets.QLineEdit(FormDebtors)
        self.area.setGeometry(QtCore.QRect(280, 100, 151, 27))
        self.area.setObjectName("area")
        self.name = QtWidgets.QLineEdit(FormDebtors)
        self.name.setGeometry(QtCore.QRect(70, 60, 146, 27))
        self.name.setObjectName("name")
        self.total = QtWidgets.QLineEdit(FormDebtors)
        self.total.setGeometry(QtCore.QRect(70, 290, 145, 27))
        self.total.setObjectName("total")
        self.lblDueDate = QtWidgets.QLabel(FormDebtors)
        self.lblDueDate.setGeometry(QtCore.QRect(240, 340, 53, 27))
        self.lblDueDate.setObjectName("lblDueDate")
        self.name.setTabOrder(self.name, self.phone)
        self.phone.setTabOrder(self.phone, self.town)
        self.town.setTabOrder(self.town, self.area)
        self.area.setTabOrder(self.area, self.productName)
        self.productName.setTabOrder(self.productName, self.amountPaid)
        self.amountPaid.setTabOrder(self.amountPaid, self.amountOwed)
        self.amountOwed.setTabOrder(self.amountOwed, self.total)
        self.total.setTabOrder(self.total, self.quantity)
        self.quantity.setTabOrder(self.quantity, self.address)
        self.address.setTabOrder(self.address, self.dueDate)
        self.dueDate.setTabOrder(self.dueDate, self.btnSave)
        self.btnSave.setTabOrder(self.btnSave, self.btnCancel)
        self.retranslateUi(FormDebtors)
        self.btnSave.clicked.connect(self.validate)
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
        query.exec_("select name, phone, address, city from customers")
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

        complet = QtWidgets.QCompleter()
        complet.setFilterMode(QtCore.Qt.MatchContains)
        complet.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        complet.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.town.setCompleter(complet)
        complet.setModel(modl)
        complet.setCompletionColumn(3)

        comp = QtWidgets.QCompleter()
        comp.setFilterMode(QtCore.Qt.MatchContains)
        comp.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        comp.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.area.setCompleter(comp)
        comp.setModel(modl)
        comp.setCompletionColumn(2)
        self.btnCancel.clicked.connect(FormDebtors.close)
        QtCore.QMetaObject.connectSlotsByName(FormDebtors)

    def retranslateUi(self, FormDebtors):
        _translate = QtCore.QCoreApplication.translate
        FormDebtors.setWindowTitle(_translate("FormDebtors", "New Debt"))
        self.label.setText(_translate("FormDebtors", "Debtor\'s Information"))
        self.lblAmountPaid.setText(_translate("FormDebtors", "Amount Paid:"))
        self.lblPhone.setText(_translate("FormDebtors", "Phone:"))
        self.label_2.setText(_translate("FormDebtors", "Name:"))
        self.lblTotal.setText(_translate("FormDebtors", "Total:"))
        self.btnSave.setText(_translate("FormDebtors", "Save"))
        self.label_3.setText(_translate("FormDebtors", "Product Name:"))
        self.lblAddress.setText(_translate("FormDebtors", "Address:"))
        self.lblcustomerTown_2.setText(_translate("FormDebtors", "Town:"))
        self.lblQuantity_2.setText(_translate("FormDebtors", "Quantity:"))
        self.btnCancel.setText(_translate("FormDebtors", "Cancel"))
        self.lblArea.setText(_translate("FormDebtors", "Area:"))
        self.lblAmount.setText(_translate("FormDebtors", "Amount Owed:"))
        self.lblDueDate.setText(_translate("FormDebtors", "Due on:"))
    
    def validate(self):
        error = 0
        if self.name.text() == '' or self.name.text().isspace():
            error = 1
        if self.town.text() == '' or self.town.text().isspace():
            error = 2
        if self.area.text() == '' or self.area.text().isspace():
            error = 3
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
        if self.address.toPlainText() == '' or self.address.toPlainText().isspace():
            error = 10
        if self.dueDate.text() == '' or self.dueDate.text().isspace():
            error = 11

        if (self.name.text() == '' or self.name.text().isspace()) and (self.town.text() == '' or
            self.town.text().isspace()) and (self.productName.text() == '' or self.productName.text().isspace()) and \
            (self.area.text() == '' or self.area.text().isspace()) and (self.phone.text() == '' or
            self.phone.text().isspace()) and (self.dueDate.text() == '' or self.dueDate.text().isspace()) and \
            (self.address.toPlainText() == '' or self.address.toPlainText().isspace()) and (
            self.quantity.text() == '' or self.quantity.text().isspace()) and (self.total.text() == '' or
            self.total.text().isspace()) and (self.amountPaid.text() == '' or self.amountPaid.text().isspace()) and(
            self.amountOwed.text() == '' or self.amountOwed.text().isspace()):
            error = 12

        if error == 0:
            self.insert_data()
        else:
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("There are blank fields"),
                                           QtWidgets.qApp.tr("\nPlease all fields are required!. "
                                                             "Make sure you fill all fields"),
                                           QtWidgets.QMessageBox.Ok)

    def insert_data(self):
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO debts(customer_name,phone,city,area,address,product_name,"
                          "amount_paid, amount_owed,total, quantity,due_date) VALUES(?,?,?,?,?,?,?,?,?,?,?)")
            query.bindValue(0, self.name.text())
            query.bindValue(1, self.phone.text())
            query.bindValue(2, self.town.text())
            query.bindValue(3, self.area.text())
            query.bindValue(4, self.address.toPlainText())
            query.bindValue(5, self.productName.text())
            query.bindValue(6, self.amountPaid.text())
            query.bindValue(7, self.amountOwed.text())
            query.bindValue(8, self.total.text())
            query.bindValue(9, self.quantity.text())
            query.bindValue(10, self.dueDate.text())
            if query.exec_():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Save Successful"),
                                                  QtWidgets.qApp.tr("\nYour debt information has been saved"),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Successful"),
                                                  QtWidgets.qApp.tr("Data could not be saved successfully"),
                                                  QtWidgets.QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Deb = QtWidgets.QDialog()
    ui = Ui_FormDebtors()
    ui.setupUi(Deb)
    Deb.show()
    sys.exit(app.exec_())