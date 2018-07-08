# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contacts.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_Contacts(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 590)
        self.contactView = QtWidgets.QTableView(Dialog)
        self.contactView.setGeometry(QtCore.QRect(27, 271, 580, 251))
        self.contactView.setStyleSheet("border:2px solid #dcdcdc;")
        self.contactView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.contactView.setGridStyle(QtCore.Qt.SolidLine)
        self.contactView.setSortingEnabled(True)
        self.contactView.setObjectName("tableView")
        self.contactView.horizontalHeader().setHighlightSections(True)
        self.contactView.horizontalHeader().setMinimumSectionSize(284)
        self.contactView.verticalHeader().setHighlightSections(False)
        self.btnDelete = QtWidgets.QPushButton(Dialog)
        self.btnDelete.setGeometry(QtCore.QRect(527, 531, 81, 41))
        self.btnDelete.setObjectName("btnDelete")
        self.label_4 = QtWidgets.QLabel(Dialog)
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
        self.btnUpdate = QtWidgets.QPushButton(Dialog)
        self.btnUpdate.setGeometry(QtCore.QRect(420, 531, 82, 41))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnClose = QtWidgets.QPushButton(Dialog)
        self.btnClose.setGeometry(QtCore.QRect(320, 531, 81, 41))
        self.btnClose.setObjectName("btnClose")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 180, 581, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.searchName = QtWidgets.QLineEdit(self.groupBox)
        self.searchName.setGeometry(QtCore.QRect(140, 33, 211, 27))
        self.searchName.setStyleSheet("border:1px solid #999;\n"
"border-radius:0;")
        self.searchName.setPlaceholderText("")
        self.searchName.setObjectName("searchName")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(0, 40, 121, 17))
        self.label_3.setStyleSheet("border:0;")
        self.label_3.setObjectName("label_3")
        self.btnSearch = QtWidgets.QPushButton(self.groupBox)
        self.btnSearch.setGeometry(QtCore.QRect(370, 30, 81, 31))
        self.btnSearch.setObjectName("btnSearch")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
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
        self.contactName.setObjectName("contactName")
        self.btnSave = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSave.setGeometry(QtCore.QRect(420, 60, 99, 41))
        self.btnSave.setObjectName("btnSave")
        self.btnSave.raise_()
        self.groupBox_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnDelete.setText(_translate("Dialog", "Delete"))
        self.label_4.setText(_translate("Dialog", "Contact Entry"))
        self.btnUpdate.setText(_translate("Dialog", "Update"))
        self.btnClose.setText(_translate("Dialog", "Close"))
        self.groupBox.setTitle(_translate("Dialog", "Actions"))
        self.label_3.setText(_translate("Dialog", "Search by Contact:"))
        self.btnSearch.setText(_translate("Dialog", "Search"))
        self.label.setText(_translate("Dialog", "Contact Person:"))
        self.label_2.setText(_translate("Dialog", "Contact No:"))
        self.btnSave.setText(_translate("Dialog", "Save"))

    def saveNow(self):
        import sql
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
        self.contactView.horizontalHeader().setStyleSheet("background-color:#444;color:#fff;")
        self.contactView.setColumnHidden(0, True)
        self.contactView.show()
