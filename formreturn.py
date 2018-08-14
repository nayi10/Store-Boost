# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formreturn.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
from time import strftime, gmtime

class Ui_FormReturns(object):
    def setupUi(self, FormReturns):
        FormReturns.setObjectName("FormReturns")
        FormReturns.resize(610, 540)
        self.groupBox = QtWidgets.QGroupBox(FormReturns)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 551, 491))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 17))
        self.label.setObjectName("label")
        self.productName = QtWidgets.QLineEdit(self.groupBox)
        self.productName.setGeometry(QtCore.QRect(130, 35, 231, 27))
        self.productName.setObjectName("productName")
        self.productCode = QtWidgets.QLineEdit(self.groupBox)
        self.productCode.setGeometry(QtCore.QRect(427, 34, 113, 27))
        self.productCode.setObjectName("productCode")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(380, 40, 41, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 131, 17))
        self.label_3.setObjectName("label_3")
        self.returnee = QtWidgets.QLineEdit(self.groupBox)
        self.returnee.setGeometry(QtCore.QRect(160, 86, 381, 27))
        self.returnee.setObjectName("returnee")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 91, 17))
        self.label_4.setObjectName("label_4")
        self.returnType = QtWidgets.QComboBox(self.groupBox)
        self.returnType.setGeometry(QtCore.QRect(110, 136, 301, 27))
        self.returnType.setObjectName("returnType")
        self.returnType.addItem("")
        self.returnType.addItem("")
        self.label_price = QtWidgets.QLabel(self.groupBox)
        self.label_price.setGeometry(QtCore.QRect(10, 190, 100, 17))
        self.label_price.setObjectName("label_price")
        self.price = QtWidgets.QLineEdit(self.groupBox)
        self.price.setGeometry(110, 185, 430, 27)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 68, 17))
        self.label_6.setObjectName("label_6")
        self.quantity = QtWidgets.QLineEdit(self.groupBox)
        self.quantity.setGeometry(QtCore.QRect(80, 245, 111, 27))
        self.quantity.setObjectName("quantity")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(210, 250, 101, 17))
        self.label_7.setObjectName("label_7")
        self.dateReturned = QtWidgets.QDateEdit(self.groupBox)
        self.dateReturned.setGeometry(QtCore.QRect(320, 245, 220, 27))
        self.dateReturned.setDate(QtCore.QDate.currentDate())
        self.dateReturned.setObjectName("dateReturned")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 300, 131, 17))
        self.label_8.setObjectName("label_8")
        self.reason = QtWidgets.QTextEdit(self.groupBox)
        self.reason.setGeometry(QtCore.QRect(10, 320, 531, 80))
        self.reason.setObjectName("reason")
        self.btnSave = QtWidgets.QPushButton(self.groupBox)
        self.btnSave.setGeometry(QtCore.QRect(440, 420, 99, 35))
        self.btnSave.setObjectName("btnSave")
        self.btnClose = QtWidgets.QPushButton(self.groupBox)
        self.btnClose.setGeometry(QtCore.QRect(10, 420, 121, 35))
        self.btnClose.setObjectName("btnClose")
        sql.connectDB()
        completer = QtWidgets.QCompleter()
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        qery = QtSql.QSqlQuery()
        qery.exec_("select distinct product_name from products")
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(qery)
        self.productName.setCompleter(completer)
        completer.setModel(modal)
        complet = QtWidgets.QCompleter()
        complet.setFilterMode(QtCore.Qt.MatchContains)
        complet.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        complet.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        query = QtSql.QSqlQuery()
        query.exec_("select distinct product_code from products")
        model = QtSql.QSqlQueryModel()
        model.setQuery(query)
        self.productCode.setCompleter(complet)
        complet.setModel(model)

        completor = QtWidgets.QCompleter()
        completor.setFilterMode(QtCore.Qt.MatchContains)
        completor.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completor.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        qry = QtSql.QSqlQuery()
        qry.exec_("select distinct name from customers")
        modl = QtSql.QSqlQueryModel()
        modl.setQuery(qry)
        self.returnee.setCompleter(completor)
        completor.setModel(modl)
        self.retranslateUi(FormReturns)
        self.btnClose.clicked.connect(FormReturns.close)
        QtCore.QMetaObject.connectSlotsByName(FormReturns)

    def retranslateUi(self, FormReturns):
        _translate = QtCore.QCoreApplication.translate
        FormReturns.setWindowTitle(_translate("FormReturns", "New return"))
        self.groupBox.setTitle(_translate("FormReturns", "Add a new return"))
        self.label.setText(_translate("FormReturns", "Product Name:"))
        self.label_3.setText(_translate("FormReturns", "Name of Returnee:"))
        self.label_4.setText(_translate("FormReturns", "Return Type:"))
        self.returnType.setItemText(0, _translate("FormReturns", "Inward"))
        self.returnType.setItemText(1, _translate("FormReturns", "Outward"))
        self.label_price.setText(_translate("FormReturns", "Product Price:"))
        self.label_6.setText(_translate("FormReturns", "Quantity:"))
        self.label_7.setText(_translate("FormReturns", "Date returned:"))
        self.label_8.setText(_translate("FormReturns", "Reason for return:"))
        self.btnSave.setText(_translate("FormReturns", "Save Data"))
        self.btnClose.setText(_translate("FormReturns", "Close"))
        self.label_2.setText(_translate("FormReturns", "Code:"))


    def validate(self):
        error = 0
        if self.productCode.text() == '' or self.productCode.text().isspace():
            error = 1
        if self.returnee.text() == '' or self.returnee.text().isspace():
            error = 2
        if self.returnType.currentText() == '' or self.returnType.currentText().isspace():
            error = 3
        if self.productName.text() == '' or self.productName.text().isspace():
            error = 4
        if self.quantity.text() == '' or self.quantity.text().isspace():
            error = 6
        if self.reason.toPlainText() == '' or self.reason.toPlainText().isspace():
            error = 7
        if self.dateReturned.text() == '' or self.dateReturned.text().isspace():
            error = 8

        if (self.productCode.text() == '' or self.productCode.text().isspace()) and (self.returnee.text() == '' or
            self.returnee.text().isspace()) and (self.productName.text() == '' or self.productName.text().isspace()) and \
            (self.returnType.currentText() == '' or self.returnType.currentText().isspace()) and (
                self.dateReturned.text() == '' or self.dateReturned.text().isspace()) and \
            (self.reason.toPlainText() == '' or self.reason.toPlainText().isspace()) and (
            self.quantity.text() == '' or self.quantity.text().isspace()):
            error = 9

        if error == 0:
            self.insert_data()
        else:
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("There are blank fields"),
                                           QtWidgets.qApp.tr("\nPlease all fields are required!"),
                                           QtWidgets.QMessageBox.Ok)

    def insert_data(self):
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO returns(product_code,product_name,returnee,return_type,price,qty,date_returned,"
                          "reason) VALUES(?,?,?,?,?,?,?,?)")
            query.bindValue(0, self.productCode.text())
            query.bindValue(1, self.productName.text())
            query.bindValue(2, self.returnee.text())
            query.bindValue(3, self.returnType.currentText())
            query.bindValue(4, self.price.text())
            query.bindValue(5, self.quantity.text())
            query.bindValue(6, self.dateReturned.text())
            query.bindValue(7, self.reason.toPlainText())
            if query.exec_():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Save Successful"),
                                                  QtWidgets.qApp.tr("\nReturn information has been saved"),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Successful"),
                                                  QtWidgets.qApp.tr("Data could not be saved successfully" + query.lastError().text()),
                                                  QtWidgets.QMessageBox.Ok)

    def display_item(self):
        return ("Hello world")

    def watch_for_events(self):
        self.db_watcher = QtCore.QFileSystemWatcher()
        path = self.db_watcher.addPath("ims.db")
        # QtCore.QObject.connect(self.db_watcher, QtCore.SIGNAL("fileChanged(QString)"), self.display_item)
        # self.db_watcher.fileChanged.connect(self.display_item())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormReturns = QtWidgets.QDialog()
    ui = Ui_FormReturns()
    ui.setupUi(FormReturns)
    ui.btnSave.clicked.connect(ui.validate)
    ui.watch_for_events()
    FormReturns.show()
    sys.exit(app.exec_())