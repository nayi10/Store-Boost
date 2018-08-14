# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdebtors.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
import sqlite3

class Ui_EditDebtors(object):
    def setupUi(self, EditDebtors):
        EditDebtors.setObjectName("EditDebtors")
        EditDebtors.resize(1068, 656)
        self.gridLayout_4 = QtWidgets.QGridLayout(EditDebtors)
        self.gridLayout_4.setContentsMargins(28, -1, 28, 15)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.debtorView = QtWidgets.QTableView(EditDebtors)
        self.debtorView.setObjectName("debtorView")
        self.debtorView.horizontalHeader().setCascadingSectionResizes(True)
        self.debtorView.horizontalHeader().setDefaultSectionSize(130)
        self.debtorView.horizontalHeader().setSortIndicatorShown(True)
        self.debtorView.horizontalHeader().setStretchLastSection(True)
        self.debtorView.verticalHeader().setCascadingSectionResizes(True)
        self.debtorView.verticalHeader().setDefaultSectionSize(35)
        self.debtorView.verticalHeader().setSortIndicatorShown(False)
        self.debtorView.verticalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.debtorView, 1, 2, 1, 3)
        self.group = QtWidgets.QGroupBox(EditDebtors)
        self.group.setStyleSheet("")
        self.group.setTitle("")
        self.group.setObjectName("group")
        self.gridLayout = QtWidgets.QGridLayout(self.group)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSearch = QtWidgets.QPushButton(self.group)
        self.btnSearch.setObjectName("btnSearch")
        self.gridLayout.addWidget(self.btnSearch, 0, 1, 1, 1)
        self.btnNewDebtor = QtWidgets.QPushButton(self.group)
        self.btnNewDebtor.setStyleSheet("")
        self.btnNewDebtor.setObjectName("btnNewDebtor")
        self.gridLayout.addWidget(self.btnNewDebtor, 0, 3, 1, 1)
        self.search = QtWidgets.QLineEdit(self.group)
        self.search.setMaxLength(327)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 0, 0, 1, 1)
        self.btnClose = QtWidgets.QPushButton(self.group)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")
        self.gridLayout.addWidget(self.btnClose, 0, 5, 1, 1)
        self.gridLayout_4.addWidget(self.group, 0, 2, 1, 3)
        self.formGroupBox = QtWidgets.QGroupBox(EditDebtors)
        self.formGroupBox.setTitle("")
        self.formGroupBox.setObjectName("formGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.formGroupBox)
        self.gridLayout_2.setContentsMargins(1, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.phone = QtWidgets.QLineEdit(self.formGroupBox)
        self.phone.setObjectName("phone")
        self.gridLayout_2.addWidget(self.phone, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formGroupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.formGroupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.formGroupBox)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.formGroupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 10, 0, 1, 1)
        self.product = QtWidgets.QLineEdit(self.formGroupBox)
        self.product.setObjectName("product")
        self.gridLayout_2.addWidget(self.product, 11, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.formGroupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 12, 0, 1, 1)
        self.amountOwed = QtWidgets.QLineEdit(self.formGroupBox)
        self.amountOwed.setObjectName("amountOwed")
        self.gridLayout_2.addWidget(self.amountOwed, 15, 0, 1, 1)
        self.amountPaid = QtWidgets.QLineEdit(self.formGroupBox)
        self.amountPaid.setObjectName("amountPaid")
        self.gridLayout_2.addWidget(self.amountPaid, 13, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.formGroupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 14, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.formGroupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.city = QtWidgets.QLineEdit(self.formGroupBox)
        self.city.setObjectName("city")
        self.gridLayout_2.addWidget(self.city, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.formGroupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 6, 0, 1, 1)
        self.area = QtWidgets.QLineEdit(self.formGroupBox)
        self.area.setObjectName("area")
        self.gridLayout_2.addWidget(self.area, 7, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.formGroupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 8, 0, 1, 1)
        self.address = QtWidgets.QTextEdit(self.formGroupBox)
        self.address.setMaximumSize(QtCore.QSize(192, 80))
        self.address.setObjectName("address")
        self.gridLayout_2.addWidget(self.address, 9, 0, 1, 1)
        self.quantity = QtWidgets.QLineEdit(self.formGroupBox)
        self.quantity.setObjectName("quantity")
        self.gridLayout_2.addWidget(self.quantity, 19, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.formGroupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 18, 0, 1, 1)
        self.total = QtWidgets.QLineEdit(self.formGroupBox)
        self.total.setObjectName("total")
        self.gridLayout_2.addWidget(self.total, 17, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.formGroupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 16, 0, 1, 1)
        self.gridLayout_4.addWidget(self.formGroupBox, 0, 0, 4, 2)
        self.horizontalGroupBox = QtWidgets.QGroupBox(EditDebtors)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.horizontalGroupBox)
        self.gridLayout_3.setContentsMargins(16, -1, 21, 11)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.select_debtors = QtWidgets.QComboBox(self.horizontalGroupBox)
        self.select_debtors.setStyleSheet("width:150px;")
        self.select_debtors.setObjectName("select_debtors")
        self.gridLayout_3.addWidget(self.select_debtors, 0, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.horizontalGroupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 4, 1, 1)
        self.dueDate = QtWidgets.QLineEdit(self.horizontalGroupBox)
        self.dueDate.setStyleSheet("width:120px;")
        self.dueDate.setObjectName("dueDate")
        self.gridLayout_3.addWidget(self.dueDate, 0, 5, 1, 1)
        self.btnUpdate = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.btnUpdate.setStyleSheet("")
        self.btnUpdate.setObjectName("btnUpdate")
        self.gridLayout_3.addWidget(self.btnUpdate, 0, 6, 1, 1)
        self.btnEdit = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.btnEdit.setObjectName("btnEdit")
        self.gridLayout_3.addWidget(self.btnEdit, 0, 8, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.btnDelete.setStyleSheet("")
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout_3.addWidget(self.btnDelete, 0, 9, 1, 1)
        self.gridLayout_4.addWidget(self.horizontalGroupBox, 3, 3, 1, 1)
        self.btnEdit.setDisabled(True)
        self.select_debtors.setDisabled(True)
        self.btnSearch.clicked.connect(lambda: self.get_debtor())
        self.btnUpdate.clicked.connect(lambda: self.validate())
        self.btnEdit.clicked.connect(lambda:self.populate_fields())
        self.display_debtors()

        sql.connectDB()
        model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        query.exec_("select distinct customer_name from debts")
        model.setQuery(query)
        if model.rowCount() > 0:
            self.select_debtors.setModel(model)
            self.select_debtors.setEnabled(True)
            self.btnEdit.setEnabled(True)

        self.retranslateUi(EditDebtors)
        self.btnClose.clicked.connect(EditDebtors.close)
        QtCore.QMetaObject.connectSlotsByName(EditDebtors)

    def retranslateUi(self, EditDebtors):
        _translate = QtCore.QCoreApplication.translate
        EditDebtors.setWindowTitle(_translate("EditDebtors", "Edit debtor information"))
        self.btnSearch.setText(_translate("EditDebtors", "Search"))
        self.btnNewDebtor.setText(_translate("EditDebtors", "New Debtor"))
        self.btnClose.setText(_translate("EditDebtors", "Cancel"))
        self.label_2.setText(_translate("EditDebtors", "Phone:"))
        self.label_9.setText(_translate("EditDebtors", "City:"))
        self.label_3.setText(_translate("EditDebtors", "Product:"))
        self.label_4.setText(_translate("EditDebtors", "Amount Paid:"))
        self.label_5.setText(_translate("EditDebtors", "Amount Owed:"))
        self.label.setText(_translate("EditDebtors", "Name:"))
        self.label_10.setText(_translate("EditDebtors", "Area:"))
        self.label_11.setText(_translate("EditDebtors", "Address:"))
        self.label_7.setText(_translate("EditDebtors", "Quantity:"))
        self.label_6.setText(_translate("EditDebtors", "Total:"))
        self.label_8.setText(_translate("EditDebtors", "Due Date:"))
        self.btnUpdate.setText(_translate("EditDebtors", "Update"))
        self.btnEdit.setText(_translate("EditDebtors", "Edit Selected"))
        self.btnDelete.setText(_translate("EditDebtors", "Delete"))

    def delete_record(self):
        if sql.connectDB():
            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete?"),
             QtWidgets.qApp.tr("Are you sure you want to delete <b>" + self.select_debtors.currentText() +
                               "</b> from creditors"), QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if confirm == QtWidgets.QMessageBox.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("delete from debts where customer_name = ?")
                query.bindValue(0, self.select_debtors.currentText())
                if query.exec_():
                    self.update_view()
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Debtor deleted!"),
                                                      QtWidgets.qApp.tr("Debtor has been deleted"),
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Debtor not deleted!"),
                                                   QtWidgets.qApp.tr("Debtor couldn't be deleted"),
                                                   QtWidgets.QMessageBox.Ok)

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
        self.model.setHeaderData(11, QtCore.Qt.Horizontal, "Due Date")
        self.model.select()
        self.debtorView.setModel(self.model)
        self.debtorView.horizontalHeader().setMinimumHeight(40)
        self.debtorView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.debtorView.setColumnHidden(0, True)
        self.debtorView.show()

    def validate(self):
        error = 0
        if self.name.text() == '' or self.name.text().isspace():
            error = 1
        if self.city.text() == '' or self.city.text().isspace():
            error = 2
        if self.area.text() == '' or self.area.text().isspace():
            error = 3
        if self.product.text() == '' or self.product.text().isspace():
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

        if (self.name.text() == '' or self.name.text().isspace()) and (self.city.text() == '' or
                                                                       self.city.text().isspace()) and (
                self.product.text() == '' or self.product.text().isspace()) and \
                (self.area.text() == '' or self.area.text().isspace()) and (self.phone.text() == '' or
                                                                            self.phone.text().isspace()) and (
                self.dueDate.text() == '' or self.dueDate.text().isspace()) and \
                (self.address.toPlainText() == '' or self.address.toPlainText().isspace()) and (
                self.quantity.text() == '' or self.quantity.text().isspace()) and (self.total.text() == '' or
                                                                                   self.total.text().isspace()) and (
                self.amountPaid.text() == '' or self.amountPaid.text().isspace()) and (
                self.amountOwed.text() == '' or self.amountOwed.text().isspace()):
            error = 12

        if error == 0:
            self.update_data()
        else:
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("There are blank fields"),
                                           QtWidgets.qApp.tr(
                                               "\nPlease all fields are required, make sure to fill them"),
                                           QtWidgets.QMessageBox.Ok)

    def populate_fields(self):
        if self.select_debtors.currentText() != "":
            name = self.select_debtors.currentText()
            qry = QtSql.QSqlQuery()
            qry.prepare("select * from debts where customer_name = ?")
            qry.bindValue(0, name)
            qry.exec_()
            while qry.next():
                self.name.setText(str(qry.value(1)))
                self.phone.setText(str(qry.value(2)))
                self.city.setText(str(qry.value(3)))
                self.area.setText(str(qry.value(4)))
                self.address.setText(str(qry.value(5)))
                self.product.setText(str(qry.value(6)))
                self.amountPaid.setText(str(qry.value(7)))
                self.amountOwed.setText(str(qry.value(8)))
                self.total.setText(str(qry.value(9)))
                self.quantity.setText(str(qry.value(10)))
                self.dueDate.setText(str(qry.value(11)))

    def update_data(self):
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE debts SET customer_name = ?,phone = ?,city = ?,area = ?,address = ?,product_name = ?,"
                          "amount_paid = ?, amount_owed = ?, total = ?, quantity = ?, due_date = ? WHERE customer_name = ?")
            query.bindValue(0, self.name.text())
            query.bindValue(1, self.phone.text())
            query.bindValue(2, self.city.text())
            query.bindValue(3, self.area.text())
            query.bindValue(4, self.address.toPlainText())
            query.bindValue(5, self.product.text())
            query.bindValue(6, self.amountPaid.text())
            query.bindValue(7, self.amountOwed.text())
            query.bindValue(8, self.total.text())
            query.bindValue(9, self.quantity.text())
            query.bindValue(10, self.dueDate.text())
            query.bindValue(11, self.select_debtors.currentText())
            if query.exec_():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Updated Successfully"),
                                                  QtWidgets.qApp.tr("\nDebtor information has been updated"),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Updated Successfully"),
                                                  QtWidgets.qApp.tr("Data update not successful"),
                                                  QtWidgets.QMessageBox.Ok)

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_EditDebtors()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

