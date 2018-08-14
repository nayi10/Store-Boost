# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editcustomer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
import sqlite3

class Ui_EditCustomer(object):
    def setupUi(self, EditCustomer):
        EditCustomer.setObjectName("EditCustomer")
        EditCustomer.resize(773, 611)
        self.btnLoad = QtWidgets.QPushButton(EditCustomer)
        self.btnLoad.setGeometry(QtCore.QRect(530, 12, 111, 34))
        self.btnLoad.setObjectName("btnLoad")
        self.customerChoose = QtWidgets.QComboBox(EditCustomer)
        self.customerChoose.setGeometry(QtCore.QRect(170, 14, 351, 31))
        self.customerChoose.setObjectName("customerChoose")
        self.label = QtWidgets.QLabel(EditCustomer)
        self.label.setGeometry(QtCore.QRect(50, 20, 111, 21))
        self.label.setObjectName("label")
        self.btnCancel = QtWidgets.QPushButton(EditCustomer)
        self.btnCancel.setGeometry(QtCore.QRect(660, 10, 81, 42))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.groupCustomer = QtWidgets.QGroupBox(EditCustomer)
        self.groupCustomer.setGeometry(QtCore.QRect(30, 60, 711, 521))
        self.groupCustomer.setStyleSheet("border:1px solid #ccc;")
        self.groupCustomer.setTitle("")
        self.groupCustomer.setObjectName("groupCustomer")
        self.label_2 = QtWidgets.QLabel(self.groupCustomer)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 51, 17))
        self.label_2.setStyleSheet("border:0;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupCustomer)
        self.label_3.setGeometry(QtCore.QRect(380, 23, 61, 17))
        self.label_3.setStyleSheet("border:0;")
        self.label_3.setObjectName("label_3")
        self.phone = QtWidgets.QLineEdit(self.groupCustomer)
        self.phone.setGeometry(QtCore.QRect(450, 19, 231, 28))
        self.phone.setObjectName("phone")
        self.label_4 = QtWidgets.QLabel(self.groupCustomer)
        self.label_4.setGeometry(QtCore.QRect(20, 74, 41, 17))
        self.label_4.setStyleSheet("border:0;")
        self.label_4.setObjectName("label_4")
        self.city = QtWidgets.QLineEdit(self.groupCustomer)
        self.city.setGeometry(QtCore.QRect(60, 70, 241, 27))
        self.city.setObjectName("city")
        self.label_5 = QtWidgets.QLabel(self.groupCustomer)
        self.label_5.setGeometry(QtCore.QRect(330, 77, 51, 17))
        self.label_5.setStyleSheet("border:0;")
        self.label_5.setObjectName("label_5")
        self.region = QtWidgets.QLineEdit(self.groupCustomer)
        self.region.setGeometry(QtCore.QRect(390, 73, 291, 27))
        self.region.setObjectName("region")
        self.label_6 = QtWidgets.QLabel(self.groupCustomer)
        self.label_6.setGeometry(QtCore.QRect(20, 136, 61, 17))
        self.label_6.setStyleSheet("border:0;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupCustomer)
        self.label_7.setGeometry(QtCore.QRect(390, 130, 67, 17))
        self.label_7.setStyleSheet("border:0;")
        self.label_7.setObjectName("label_7")
        self.address = QtWidgets.QTextEdit(self.groupCustomer)
        self.address.setGeometry(QtCore.QRect(390, 150, 291, 131))
        self.address.setObjectName("address")
        self.label_8 = QtWidgets.QLabel(self.groupCustomer)
        self.label_8.setGeometry(QtCore.QRect(20, 194, 111, 17))
        self.label_8.setStyleSheet("border:0;")
        self.label_8.setObjectName("label_8")
        self.postalAddress = QtWidgets.QLineEdit(self.groupCustomer)
        self.postalAddress.setGeometry(QtCore.QRect(130, 190, 221, 27))
        self.postalAddress.setObjectName("postalAddress")
        self.label_13 = QtWidgets.QLabel(self.groupCustomer)
        self.label_13.setGeometry(QtCore.QRect(20, 350, 71, 17))
        self.label_13.setStyleSheet("border:0;")
        self.label_13.setObjectName("label_13")
        self.remarks = QtWidgets.QTextEdit(self.groupCustomer)
        self.remarks.setGeometry(QtCore.QRect(20, 370, 661, 75))
        self.remarks.setObjectName("remarks")
        self.customerName = QtWidgets.QLineEdit(self.groupCustomer)
        self.customerName.setGeometry(QtCore.QRect(70, 16, 281, 27))
        self.customerName.setObjectName("customerName")
        self.btnUpdate = QtWidgets.QPushButton(self.groupCustomer)
        self.btnUpdate.setGeometry(QtCore.QRect(530, 460, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")

        self.btnDelete = QtWidgets.QPushButton(self.groupCustomer)
        self.btnDelete.setGeometry(QtCore.QRect(20, 460, 130, 41))
        self.btnDelete.setObjectName("btnDelete")
        self.email = QtWidgets.QLineEdit(self.groupCustomer)
        self.email.setGeometry(QtCore.QRect(70, 260, 301, 27))
        self.email.setObjectName("email")
        self.label_10 = QtWidgets.QLabel(self.groupCustomer)
        self.label_10.setGeometry(QtCore.QRect(20, 265, 41, 17))
        self.label_10.setStyleSheet("border:0;")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.groupCustomer)
        self.label_12.setGeometry(QtCore.QRect(20, 315, 91, 17))
        self.label_12.setStyleSheet("border:0;")
        self.label_12.setObjectName("label_12")
        self.dateAdded = QtWidgets.QLineEdit(self.groupCustomer)
        self.dateAdded.setGeometry(QtCore.QRect(110, 310, 571, 27))
        self.dateAdded.setObjectName("dateAdded")
        self.gender = QtWidgets.QLineEdit(self.groupCustomer)
        self.gender.setGeometry(QtCore.QRect(90, 130, 241, 27))
        self.gender.setObjectName("gender")
        self.update_view()
        self.groupCustomer.hide()

        self.retranslateUi(EditCustomer)
        self.btnCancel.clicked.connect(EditCustomer.close)
        QtCore.QMetaObject.connectSlotsByName(EditCustomer)

    def retranslateUi(self, EditCustomer):
        _translate = QtCore.QCoreApplication.translate
        EditCustomer.setWindowTitle(_translate("EditCustomer", "Edit customers"))
        self.btnLoad.setText(_translate("EditCustomer", "Load Details"))
        self.label.setText(_translate("EditCustomer", "Select Product:"))
        self.btnCancel.setText(_translate("EditCustomer", "Cancel"))
        self.label_2.setText(_translate("EditCustomer", "Name:"))
        self.label_3.setText(_translate("EditCustomer", "Contact:"))
        self.label_4.setText(_translate("EditCustomer", "City:"))
        self.label_5.setText(_translate("EditCustomer", "Region:"))
        self.label_6.setText(_translate("EditCustomer", "Gender:"))
        self.label_7.setText(_translate("EditCustomer", "Address:"))
        self.label_8.setText(_translate("EditCustomer", "Postal Address:"))
        self.label_13.setText(_translate("EditCustomer", "Remarks:"))
        self.btnUpdate.setText(_translate("EditCustomer", "Update Customer"))
        self.btnDelete.setText(_translate("EditCustomer", "Delete Customer"))
        self.label_10.setText(_translate("EditCustomer", "Email:"))
        self.label_12.setText(_translate("EditCustomer", "Date Added:"))

    def update_view(self):
        model = QtSql.QSqlQueryModel()
        sql.connectDB()
        query = QtSql.QSqlQuery()
        query.exec_("select distinct name from customers")
        if query:
            model.setQuery(query)
            self.customerChoose.setStyleSheet("padding:2px 0 2px 5px;")
            self.customerChoose.setModel(model)


    def populate_fileds(self):
        connection = sqlite3.connect("ims.db")
        if connection:
            self.cursor = connection.cursor()
            self.cursor.execute("select * from customers where name = '{0}'".format(
                str(self.customerChoose.currentText())))
            rows = self.cursor.fetchall()

            if rows:
                self.groupCustomer.show()
                self.btnUpdate.setEnabled(True)
                self.customerName.setText(rows[0][1])
                self.phone.setText(rows[0][2])
                self.city.setText(str(rows[0][3]))
                self.region.setText(str(rows[0][4]))
                self.gender.setText(str(rows[0][5]))
                self.address.setText(str(rows[0][6]))
                self.postalAddress.setText(str(rows[0][7]))
                self.email.setText(str(rows[0][8]))
                self.dateAdded.setText(str(rows[0][9]))
                self.remarks.setPlainText(str(rows[0][10]))
                self.update_view()
            else:
                self.groupCustomer.hide()
                self.btnUpdate.setDisabled(True)

    def delete_record(self):
        if sql.connectDB():
            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete?"), QtWidgets.qApp.tr("Are "
                        "you sure you want to delete <b>" + self.customerChoose.currentText() + "</b> from customers"),
                                                     QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if confirm == QtWidgets.QMessageBox.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("delete from customers where name = ?")
                query.bindValue(0, self.customerChoose.currentText())
                if query.exec_():
                    self.update_view()
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Customer deleted!"),
                                                      QtWidgets.qApp.tr("Customer has been deleted"),
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Customer not deleted!"),
                                               QtWidgets.qApp.tr("Customer couldn't be deleted"),
                                               QtWidgets.QMessageBox.Ok)

    def update_records(self):
        sql.connectDB()
        qry = QtSql.QSqlQuery()
        qry.prepare("UPDATE customers SET name = ?, phone = ?, city = ?, region = ?, gender = ?, address = ?,"
            "post_office = ?, email = ?, date_registered = ?, remarks = ? WHERE name = ?")

        qry.bindValue(0, self.customerName.text())
        qry.bindValue(1, self.phone.text())
        qry.bindValue(2, self.city.text())
        qry.bindValue(3, self.region.text())
        qry.bindValue(4, self.gender.text())
        qry.bindValue(5, self.address.toPlainText())
        qry.bindValue(6, self.postalAddress.text())
        qry.bindValue(7, self.email.text())
        qry.bindValue(8, self.dateAdded.text())
        qry.bindValue(9, self.remarks.toPlainText())
        qry.bindValue(10, self.customerChoose.currentText())
        qry.exec_()
        if qry:
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Updated Successfully"),
                                              QtWidgets.qApp.tr("\nCustomer information has been successfully updated"),
                                              QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Updated"),
                                              QtWidgets.qApp.tr("Data update not successful: " + qry.lastError().text()),
                                              QtWidgets.QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditCustomer = QtWidgets.QDialog()
    ui = Ui_EditCustomer()
    ui.setupUi(EditCustomer)
    ui.btnLoad.clicked.connect(lambda: ui.populate_fileds())
    ui.btnUpdate.clicked.connect(lambda: ui.update_records())
    ui.btnDelete.clicked.connect(lambda: ui.delete_record())
    EditCustomer.show()
    sys.exit(app.exec_())

