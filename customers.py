# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customers.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_Customers(object):
    def setupUi(self, Customers):
        Customers.setObjectName("Customers")
        Customers.resize(1199, 614)
        self.tableView = QtWidgets.QTableView(Customers)
        self.tableView.setGeometry(QtCore.QRect(40, 90, 1121, 461))
        self.tableView.setObjectName("tableView")
        self.groupBox_2 = QtWidgets.QGroupBox(Customers)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 10, 1121, 61))
        self.groupBox_2.setStyleSheet("border:1px solid #ccc;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnDelete = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDelete.setGeometry(QtCore.QRect(590, 19, 82, 33))
        self.btnDelete.setObjectName("btnDelete")
        self.btnEdit = QtWidgets.QPushButton(self.groupBox_2)
        self.btnEdit.setGeometry(QtCore.QRect(720, 10, 121, 41))
        self.btnEdit.setObjectName("btnEdit")
        self.btnNew = QtWidgets.QPushButton(self.groupBox_2)
        self.btnNew.setGeometry(QtCore.QRect(860, 10, 121, 41))
        self.btnNew.setObjectName("btnNew")
        self.btnCancel = QtWidgets.QPushButton(self.groupBox_2)
        self.btnCancel.setGeometry(QtCore.QRect(1000, 10, 100, 41))
        self.btnFilter = QtWidgets.QPushButton(self.groupBox_2)
        self.btnFilter.setGeometry(QtCore.QRect(242, 20, 81, 31))
        self.btnFilter.setObjectName("btnFilter")
        self.selectName = QtWidgets.QComboBox(self.groupBox_2)
        self.selectName.setGeometry(QtCore.QRect(340, 20, 251, 31))
        self.selectName.setObjectName("selectName")
        self.customerName = QtWidgets.QComboBox(Customers)
        self.customerName.setGeometry(QtCore.QRect(70, 30, 211, 31))
        self.customerName.setObjectName("customerName")
        self.customerName.addItem("")
        self.customerName.addItem("")
        self.customerName.addItem("")
        self.customerName.addItem("")
        self.customerName.addItem("")
        self.lbl = QtWidgets.QLabel(Customers)
        self.lbl.setGeometry(QtCore.QRect(40, 565, 90, 31))
        self.lbl.setObjectName("lbl")
        self.search = QtWidgets.QLineEdit(Customers)
        self.search.setGeometry(QtCore.QRect(131, 565, 500, 31))
        self.search.setObjectName("search")
        self.search.setPlaceholderText("Enter customer name, phone, region, email or address to search")
        self.retranslateUi(Customers)
        self.btnCancel.clicked.connect(Customers.close)
        self.btnDelete.clicked.connect(self.delete_record)
        self.search.textChanged.connect(lambda: self.search_customer())
        sql.connectDB()
        complet = QtWidgets.QCompleter()
        complet.setFilterMode(QtCore.Qt.MatchContains)
        complet.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        complet.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        qery = QtSql.QSqlQuery()
        qery.exec_("select * from customers")
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(qery)
        self.search.setCompleter(complet)
        complet.setModel(modal)
        QtCore.QMetaObject.connectSlotsByName(Customers)
        self.showView()
        self.update_view()

    def update_view(self):
        model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        query.exec_("select distinct name from customers")
        model.setQuery(query)
        if model.rowCount() > 0:
            self.btnDelete.setEnabled(True)
            self.selectName.setModel(model)
        else:
            self.btnDelete.setDisabled(True)

    def retranslateUi(self, Customers):
        _translate = QtCore.QCoreApplication.translate
        Customers.setWindowTitle(_translate("Customers", "All customers"))
        self.groupBox_2.setTitle(_translate("Customers", "Filter by:"))
        self.btnDelete.setText(_translate("Customers", "Delete"))
        self.btnEdit.setText(_translate("Customers", "Edit Customer"))
        self.btnNew.setText(_translate("Customers", "New Customer"))
        self.btnCancel.setText(_translate("Customers", "Cancel"))
        self.btnFilter.setText(_translate("Customers", "Filter"))
        self.customerName.setItemText(0, _translate("Customers", "Name"))
        self.customerName.setItemText(1, _translate("Customers", "City"))
        self.customerName.setItemText(2, _translate("Customers", "Phone"))
        self.customerName.setItemText(3, _translate("Customers", "Email"))
        self.customerName.setItemText(4, _translate("Customers", "Region"))
        self.lbl.setText(_translate("Customers", "Search by:"))

    def delete_record(self):
        if sql.connectDB():
            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete?"), QtWidgets.qApp.tr("Are "
                        "you sure you want to delete <b>" + self.selectName.currentText() + "</b> from customers?"),
                                                     QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if confirm == QtWidgets.QMessageBox.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("delete from customers where name = ?")
                query.bindValue(0, self.selectName.currentText())
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

        qry.prepare("UPDATE customers SET customer_name = ?, phone = ?, city = ?, region = ?, gender = ?, address = ?"
            "post_office = ?, email = ?, date_registered = ?, remarks = ? WHERE customer_name = ?")

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

    def filter_customers(self):
        filter_prop = self.customerName.currentText()

        model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        query.exec_("select * from customers order by {0}".format(str(filter_prop.lower())))
        model.setQuery(query)
        if model.rowCount() >  0:
            model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
            model.setHeaderData(2, QtCore.Qt.Horizontal, "Phone")
            model.setHeaderData(3, QtCore.Qt.Horizontal, "City")
            model.setHeaderData(4, QtCore.Qt.Horizontal, "Region")
            model.setHeaderData(5, QtCore.Qt.Horizontal, "Gender")
            model.setHeaderData(6, QtCore.Qt.Horizontal, "Address")
            model.setHeaderData(7, QtCore.Qt.Horizontal, "Post")
            model.setHeaderData(8, QtCore.Qt.Horizontal, "Email")
            model.setHeaderData(9, QtCore.Qt.Horizontal, "Registered Date")
            model.setHeaderData(10, QtCore.Qt.Horizontal, "Remarks")
            self.tableView.setModel(model)
            self.tableView.setMinimumWidth(1110)
            self.tableView.horizontalHeader().setDefaultSectionSize(130)
            self.tableView.horizontalHeader().setMinimumHeight(40)
            self.tableView.setColumnHidden(0, True)
            self.tableView.show()

    def search_customer(self):
        filter_prop = self.customerName.currentText()

        model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        query.exec_("select * from customers where name like '%{0}%' or phone like '%{0}%' or address like '%{0}%' or "
                    "city like '%{0}%' or region like '%{0}%' or email like '%{0}%' or post_office like '%{0}%'".format(
            str(self.search.text())))
        model.setQuery(query)
        if model.rowCount() > 0:
            model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
            model.setHeaderData(2, QtCore.Qt.Horizontal, "Phone")
            model.setHeaderData(3, QtCore.Qt.Horizontal, "City")
            model.setHeaderData(4, QtCore.Qt.Horizontal, "Region")
            model.setHeaderData(5, QtCore.Qt.Horizontal, "Gender")
            model.setHeaderData(6, QtCore.Qt.Horizontal, "Address")
            model.setHeaderData(7, QtCore.Qt.Horizontal, "Post")
            model.setHeaderData(8, QtCore.Qt.Horizontal, "Email")
            model.setHeaderData(9, QtCore.Qt.Horizontal, "Registered Date")
            model.setHeaderData(10, QtCore.Qt.Horizontal, "Remarks")
            self.tableView.setModel(model)
            self.tableView.setMinimumWidth(1110)
            self.tableView.horizontalHeader().setDefaultSectionSize(130)
            self.tableView.horizontalHeader().setMinimumHeight(40)
            self.tableView.setColumnHidden(0, True)
            self.tableView.show()

    def showView(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        model.setTable("customers")
        model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Phone")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "City")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Region")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Gender")
        model.setHeaderData(6, QtCore.Qt.Horizontal, "Address")
        model.setHeaderData(7, QtCore.Qt.Horizontal, "Post")
        model.setHeaderData(8, QtCore.Qt.Horizontal, "Email")
        model.setHeaderData(9, QtCore.Qt.Horizontal, "Registered Date")
        model.setHeaderData(10, QtCore.Qt.Horizontal, "Remarks")
        self.tableView.setModel(model)
        model.select()
        self.tableView.setMinimumWidth(1110)
        self.tableView.horizontalHeader().setDefaultSectionSize(130)
        self.tableView.horizontalHeader().setMinimumHeight(40)
        self.tableView.setColumnHidden(0, True)
        self.tableView.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Customers = QtWidgets.QDialog()
    ui = Ui_Customers()
    ui.setupUi(Customers)
    Customers.show()
    sys.exit(app.exec_())

