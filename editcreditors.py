# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editcreditors.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
import sqlite3

class Ui_EditCreditors(object):
    def setupUi(self, EditCreditors):
        EditCreditors.setObjectName("EditCreditors")
        EditCreditors.resize(793, 625)
        EditCreditors.setMaximumSize(QtCore.QSize(1024, 627))
        self.btnGroup = QtWidgets.QGroupBox(EditCreditors)
        self.btnGroup.setGeometry(QtCore.QRect(500, 40, 261, 531))
        self.btnGroup.setStyleSheet("padding-top:15px;\n"
"")
        self.btnGroup.setObjectName("btnGroup")
        self.btnUpdate = QtWidgets.QPushButton(self.btnGroup)
        self.btnUpdate.setGeometry(QtCore.QRect(100, 210, 141, 41))
        self.btnUpdate.setStyleSheet("padding:0;")
        self.btnUpdate.setObjectName("btnUpdate")
        self.select_creditor = QtWidgets.QComboBox(self.btnGroup)
        self.select_creditor.setGeometry(QtCore.QRect(20, 30, 151, 31))
        self.select_creditor.setStyleSheet("padding:0;")
        self.select_creditor.setObjectName("select_creditor")
        self.btnEdit = QtWidgets.QPushButton(self.btnGroup)
        self.btnEdit.setGeometry(QtCore.QRect(170, 30, 71, 31))
        self.btnEdit.setStyleSheet("padding:0;")
        self.btnEdit.setObjectName("btnEdit")
        self.btnDelete = QtWidgets.QPushButton(self.btnGroup)
        self.btnDelete.setGeometry(QtCore.QRect(100, 150, 141, 41))
        self.btnDelete.setStyleSheet("padding:0;")
        self.btnDelete.setObjectName("btnDelete")
        self.btnNew = QtWidgets.QPushButton(self.btnGroup)
        self.btnNew.setGeometry(QtCore.QRect(100, 90, 141, 41))
        self.btnNew.setStyleSheet("padding:0;")
        self.btnNew.setObjectName("btnNew")
        self.btnClose = QtWidgets.QPushButton(self.btnGroup)
        self.btnClose.setGeometry(QtCore.QRect(100, 270, 141, 41))
        self.btnClose.setStyleSheet("padding:0;")
        self.btnClose.setObjectName("btnClose")
        self.formGroupBox = QtWidgets.QGroupBox(EditCreditors)
        self.formGroupBox.setGeometry(QtCore.QRect(30, 40, 461, 531))
        self.formGroupBox.setTitle("")
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(-1, 14, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formGroupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.creditor_name = QtWidgets.QLineEdit(self.formGroupBox)
        self.creditor_name.setObjectName("creditor_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.creditor_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label_2 = QtWidgets.QLabel(self.formGroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.phone = QtWidgets.QLineEdit(self.formGroupBox)
        self.phone.setObjectName("phone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.phone)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.formGroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.product_name = QtWidgets.QLineEdit(self.formGroupBox)
        self.product_name.setObjectName("product_name")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.product_name)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.formGroupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.amountPaid = QtWidgets.QLineEdit(self.formGroupBox)
        self.amountPaid.setObjectName("amountPaid")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.amountPaid)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.label_5 = QtWidgets.QLabel(self.formGroupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.amountOwed = QtWidgets.QLineEdit(self.formGroupBox)
        self.amountOwed.setObjectName("amountOwed")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.amountOwed)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.label_6 = QtWidgets.QLabel(self.formGroupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.total = QtWidgets.QLineEdit(self.formGroupBox)
        self.total.setObjectName("total")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.total)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.label_7 = QtWidgets.QLabel(self.formGroupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.quantity = QtWidgets.QLineEdit(self.formGroupBox)
        self.quantity.setObjectName("quantity")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.quantity)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(15, QtWidgets.QFormLayout.LabelRole, spacerItem6)
        self.label_8 = QtWidgets.QLabel(self.formGroupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.dueDate = QtWidgets.QLineEdit(self.formGroupBox)
        self.dueDate.setObjectName("dueDate")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.dueDate)
        self.label_10 = QtWidgets.QLabel(EditCreditors)
        self.label_10.setGeometry(QtCore.QRect(-13, 0, 811, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.btnUpdate.setDisabled(True)
        self.retranslateUi(EditCreditors)
        self.btnClose.clicked.connect(EditCreditors.close)
        self.btnEdit.clicked.connect(self.populate_fileds)
        self.btnUpdate.clicked.connect(self.update_records)
        self.btnDelete.clicked.connect(self.delete_record)
        QtCore.QMetaObject.connectSlotsByName(EditCreditors)
        self.update_view()

    def retranslateUi(self, EditCreditors):
        _translate = QtCore.QCoreApplication.translate
        EditCreditors.setWindowTitle(_translate("EditCreditors", "Creditors"))
        self.btnGroup.setTitle(_translate("EditCreditors", "Select creditor"))
        self.btnUpdate.setText(_translate("EditCreditors", "Update Selected"))
        self.btnEdit.setText(_translate("EditCreditors", "Edit"))
        self.btnDelete.setText(_translate("EditCreditors", "Delete Selected"))
        self.btnNew.setText(_translate("EditCreditors", "New Creditor"))
        self.btnClose.setText(_translate("EditCreditors", "Close"))
        self.label.setText(_translate("EditCreditors", "Name:"))
        self.label_2.setText(_translate("EditCreditors", "Phone:"))
        self.label_3.setText(_translate("EditCreditors", "Product:"))
        self.label_4.setText(_translate("EditCreditors", "Amount Paid:"))
        self.label_5.setText(_translate("EditCreditors", "Amount Owed:"))
        self.label_6.setText(_translate("EditCreditors", "Total:"))
        self.label_7.setText(_translate("EditCreditors", "Quantity:"))
        self.label_8.setText(_translate("EditCreditors", "Due Date:"))
        self.label_10.setText(_translate("EditCreditors", "Edit Creditor Information"))

    def update_view(self):
        self.formGroupBox.setDisabled(True)
        model = QtSql.QSqlQueryModel()
        sql.connectDB()
        query = QtSql.QSqlQuery()
        query.exec_("select distinct creditor_name from creditors")
        if query:
            model.setQuery(query)
            self.select_creditor.setStyleSheet("padding:2px 0 2px 5px;")
            self.select_creditor.setModel(model)

    def populate_fileds(self):
        connection = sqlite3.connect("ims.db")
        if connection:
            self.cursor = connection.cursor()
            self.cursor.execute("select * from creditors where creditor_name = '{0}'".format(
                str(self.select_creditor.currentText())))
            rows = self.cursor.fetchall()

            if rows:
                self.formGroupBox.setEnabled(True)
                self.btnUpdate.setEnabled(True)
                self.creditor_name.setText(rows[0][1])
                self.phone.setText(rows[0][2])
                self.product_name.setText(str(rows[0][3]))
                self.amountPaid.setText(str(rows[0][4]))
                self.amountOwed.setText(str(rows[0][5]))
                self.total.setText(str(rows[0][6]))
                self.quantity.setText(str(rows[0][7]))
                self.dueDate.setText(str(rows[0][8]))
                self.btnUpdate.setEnabled(True)
            else:
                self.formGroupBox.setDisabled(True)
                self.btnUpdate.setDisabled(True)

    def delete_record(self):
        if sql.connectDB():
            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete?"), QtWidgets.qApp.tr("Are "
                        "you sure you want to delete <b>" + self.select_creditor.currentText() + "</b> from creditors"),
                                                     QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if confirm == QtWidgets.QMessageBox.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("delete from creditors where creditor_name = ?")
                query.bindValue(0, self.select_creditor.currentText())
                if query.exec_():
                    self.update_view()
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Creditor deleted!"),
                                                      QtWidgets.qApp.tr("Creditor has been deleted"),
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Creditor not deleted!"),
                                               QtWidgets.qApp.tr("Creditor couldn't be deleted"),
                                               QtWidgets.QMessageBox.Ok)

    def update_records(self):
        sql.connectDB()
        qry = QtSql.QSqlQuery()

        name = (str(self.select_creditor.currentText()))
        qry.prepare("UPDATE creditors SET creditor_name = ?, phone = ?, product_name = ?, amount_paid = ?, amount_owed = ?,"
            "total = ?, quantity = ?, due_date = ? WHERE creditor_name = ?")

        qry.bindValue(0, self.creditor_name.text())
        qry.bindValue(1, self.phone.text())
        qry.bindValue(2, self.product_name.text())
        qry.bindValue(3, self.amountPaid.text())
        qry.bindValue(4, self.amountOwed.text())
        qry.bindValue(5, self.total.text())
        qry.bindValue(6, self.quantity.text())
        qry.bindValue(7, self.dueDate.text())
        qry.bindValue(8, name)
        qry.exec_()
        if qry:
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Updated Successfully"),
                                              QtWidgets.qApp.tr("\nCreditor information has been successfully updated"),
                                              QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Updated"),
                                              QtWidgets.qApp.tr("Data update not successful: " + qry.lastError().text()),
                                              QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditCreditors = QtWidgets.QDialog()
    ui = Ui_EditCreditors()
    ui.setupUi(EditCreditors)
    EditCreditors.show()
    sys.exit(app.exec_())

