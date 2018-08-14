# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contacts.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
import sqlite3
from functions import num_rows
class Ui_Contacts(object):
    def setupUi(self, Contacts):
        Contacts.setObjectName("Dialog")
        Contacts.resize(637, 590)
        self.contactView = QtWidgets.QTableView(Contacts)
        self.contactView.setGeometry(QtCore.QRect(27, 271, 580, 251))
        self.contactView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.contactView.setGridStyle(QtCore.Qt.SolidLine)
        self.contactView.setSortingEnabled(True)
        self.contactView.setObjectName("tableView")
        self.contactView.horizontalHeader().setHighlightSections(True)
        self.contactView.horizontalHeader().setMinimumSectionSize(284)
        self.contactView.verticalHeader().setHighlightSections(False)
        self.label_4 = QtWidgets.QLabel(Contacts)
        self.label_4.setGeometry(QtCore.QRect(0, -9, 651, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(Contacts)
        self.groupBox.setGeometry(QtCore.QRect(30, 180, 581, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.searchName = QtWidgets.QLineEdit(self.groupBox)
        self.searchName.setGeometry(QtCore.QRect(140, 33, 211, 27))
        self.searchName.setPlaceholderText("")
        self.searchName.setObjectName("searchName")
        self.btnSearch = QtWidgets.QPushButton(self.groupBox)
        self.btnSearch.setGeometry(QtCore.QRect(370, 30, 81, 31))
        self.btnSearch.setObjectName("btnSearch")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(0, 40, 121, 17))
        self.label_3.setStyleSheet("border:0;")
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Contacts)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 52, 571, 121))
        self.groupBox_2.setMaximumSize(QtCore.QSize(581, 16777215))
        self.groupBox_2.setStyleSheet("border:1px solid #999;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 371, 91))
        self.groupBox_3.setMaximumSize(QtCore.QSize(371, 16777215))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.contactPhone = QtWidgets.QLineEdit(self.groupBox_3)
        self.contactPhone.setGeometry(QtCore.QRect(150, 50, 201, 27))
        self.contactPhone.setPlaceholderText("")
        self.contactPhone.setObjectName("contactPhone")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.label.setStyleSheet("border:0;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.label_2.setStyleSheet("border:0;")
        self.label_2.setObjectName("label_2")
        self.contactName = QtWidgets.QLineEdit(self.groupBox_3)
        self.contactName.setGeometry(QtCore.QRect(150, 10, 201, 27))
        self.contactName.setPlaceholderText("")
        self.btnSave = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSave.setGeometry(QtCore.QRect(420, 60, 99, 41))
        self.btnSave.setObjectName("btnSave")
        self.btnSave.raise_()
        self.btnUpdate = QtWidgets.QPushButton(self.groupBox_2)
        self.btnUpdate.setGeometry(QtCore.QRect(420, 15, 99, 41))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnUpdate.raise_()
        self.contactName.setObjectName("contactName")
        self.btnSave = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSave.setGeometry(QtCore.QRect(420, 60, 99, 41))
        self.btnSave.setObjectName("btnSave")
        self.btnSave.raise_()
        self.groupBox_3.raise_()
        self.selectContact = QtWidgets.QComboBox(Contacts)
        self.selectContact.setGeometry(QtCore.QRect(27, 535, 280, 35))
        self.selectContact.setObjectName("selectContact")
        self.btnEdit = QtWidgets.QPushButton(Contacts)
        self.btnEdit.setGeometry(QtCore.QRect(310, 535, 120, 35))
        self.btnEdit.setObjectName("btnEdit")
        self.btnDelete = QtWidgets.QPushButton(Contacts)
        self.btnDelete.setGeometry(QtCore.QRect(430, 535, 81, 35))
        self.btnDelete.setObjectName("btnDelete")
        self.btnClose = QtWidgets.QPushButton(Contacts)
        self.btnClose.setGeometry(QtCore.QRect(527, 531, 81, 41))
        self.btnClose.setObjectName("btnClose")
        self.update_view()

        self.retranslateUi(Contacts)
        QtCore.QMetaObject.connectSlotsByName(Contacts)

    def retranslateUi(self, Contacts):
        _translate = QtCore.QCoreApplication.translate
        Contacts.setWindowTitle(_translate("Dialog", "All contacts - Ahasaniya Enterprise"))
        self.btnDelete.setText(_translate("Dialog", "Delete"))
        self.label_4.setText(_translate("Dialog", "Contact Entry"))
        self.btnEdit.setText(_translate("Dialog", "Edit selected"))
        self.btnClose.setText(_translate("Dialog", "Close"))
        self.groupBox.setTitle(_translate("Dialog", "Actions"))
        self.label_3.setText(_translate("Dialog", "Search by Contact:"))
        self.btnSearch.setText(_translate("Dialog", "Search"))
        self.label.setText(_translate("Dialog", "Contact Person:"))
        self.label_2.setText(_translate("Dialog", "Contact No:"))
        self.btnUpdate.setText(_translate("Dialog", "Update"))
        self.btnSave.setText(_translate("Dialog", "Save"))

    def update_view(self):
        sql.connectDB()
        self.model = QtSql.QSqlQueryModel()
        self.query = QtSql.QSqlQuery()
        self.query.exec_("select distinct contact_name from contacts")
        self.model.setQuery(self.query)
        self.selectContact.setModel(self.model)

    def populate_fields(self):
        connection = sqlite3.connect("ims.db")
        if connection:
            self.cursor = connection.cursor()
            self.cursor.execute("select * from contacts where contact_name = '{0}'".format(
                str(self.selectContact.currentText())))
            rows = self.cursor.fetchall()

            if rows:
                self.btnUpdate.setEnabled(True)
                self.contactName.setText(rows[0][1])
                self.contactPhone.setText(rows[0][2])
            else:
                self.btnUpdate.setDisabled(True)

    def update_fields(self):
        sql.connectDB()
        q = QtSql.QSqlQuery()
        q.prepare("update contacts set contact_name = ?, contact_phone = ? where contact_name = ?")
        q.bindValue(0, self.contactName.text())
        q.bindValue(1, self.contactPhone.text())
        q.bindValue(2, self.selectContact.currentText())
        if q.exec_():
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Contact updated"), QtWidgets.qApp.tr("Contact "
                                              "has been updated successfully"), QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Contact not updated"),QtWidgets.qApp.tr(
                "Contact could not be updated!"), QtWidgets.QMessageBox.Ok)

    def search_contacts(self):

        if self.searchName.text() == '' or self.searchName.text().isspace():
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Enter search query"), QtWidgets.qApp.tr(
                "Please enter search criterion to search!"), QtWidgets.QMessageBox.Ok)
        else:
            qry = QtSql.QSqlQuery()
            qry.prepare("select * from contacts where contact_name LIKE '%{0}%' or contact_phone LIKE '%{0}%' or "
                        "date_added LIKE '%{0}%'".format(str(self.searchName.text())))
            # qry.bindValue(0, str(self.search.text()))
            if qry.exec_():
                model = QtSql.QSqlQueryModel()
                model.setQuery(qry)
                model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
                model.setHeaderData(1, QtCore.Qt.Horizontal, "Contact Name")
                model.setHeaderData(2, QtCore.Qt.Horizontal, "Phone Number")
                model.setHeaderData(3, QtCore.Qt.Horizontal, "Date Saved")
                self.contactView.setModel(model)
                self.contactView.horizontalHeader().setDefaultSectionSize(200)
                self.contactView.horizontalHeader().setMinimumHeight(40)
                self.contactView.setColumnHidden(0, True)
                self.contactView.show()

    def delete_contact(self):
        if sql.connectDB():
            if not self.selectContact.currentText() == "" or not self.selectContact.currentText().isspace():
                ask = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Confirm deletion!"),
                                               QtWidgets.qApp.tr("Are you sure you want to delete this contact?"),
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
                if ask == QtWidgets.QMessageBox.Yes:
                    qry = QtSql.QSqlQuery()
                    qry.prepare("delete from contacts where contact_name = ?")
                    qry.bindValue(0, self.selectContact.currentText())
                    if qry.exec_():
                        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Contact successfully deleted!"),
                                                          QtWidgets.qApp.tr("Contact has been deleted successfully!"),
                                                          QtWidgets.QMessageBox.Ok)

    def saveNow(self):
        if sql.connectDB():
            query = QtSql.QSqlQuery()

            error = 0
            if self.contactName.text() == "" or self.contactName.text().isspace():
                error = 1

            if self.contactPhone.text() == "" or self.contactPhone.text().isspace():
                error = 2

            if error > 0:
                QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Error! All fields required!!"),
                                               QtWidgets.qApp.tr("Contact name and Phone are required!"),
                                               QtWidgets.QMessageBox.Close)

            else:
                qery = QtSql.QSqlQuery()
                qery.prepare("select contact_name from contacts where contact_phone = ?")
                qery.bindValue(0, self.contactPhone.text())
                qery.exec_()
                if num_rows(qery) == 0:

                    day = QtCore.QDate.currentDate().toString()
                    query.prepare("insert into contacts(contact_name, contact_phone, date_added) values(?,?,?)")
                    query.bindValue(0, str(self.contactName.text()))
                    query.bindValue(1, str(self.contactPhone.text()))
                    query.bindValue(2, day)
                    query.exec_()
                    if query.numRowsAffected():
                        self.contactName.setText("")
                        self.contactPhone.setText("")
                        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Contact added!"),
                                                      QtWidgets.qApp.tr("Contact has been added!"),
                                                      QtWidgets.QMessageBox.Close)
                else:
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Contact exists!"),
                                              QtWidgets.qApp.tr("The contact already exists in the system"),
                                              QtWidgets.QMessageBox.Close)

    def showContacts(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        model.setTable("contacts")
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Contact Name")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Phone Number")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Date Saved")
        model.select()
        self.contactView.setModel(model)
        self.contactView.horizontalHeader().setDefaultSectionSize(200)
        self.contactView.horizontalHeader().setMinimumHeight(40)
        self.contactView.setColumnHidden(0, True)
        self.contactView.show()
