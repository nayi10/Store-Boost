# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/users.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
import sqlite3

class Ui_Users(object):
    def setupUi(self, Users):
        Users.setObjectName("Users")
        Users.resize(863, 570)
        Users.setMaximumSize(QtCore.QSize(863, 570))
        self.widgetUsers = QtWidgets.QTableView(Users)
        self.widgetUsers.setGeometry(QtCore.QRect(170, 100, 671, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.widgetUsers.sizePolicy().hasHeightForWidth())
        self.widgetUsers.setSizePolicy(sizePolicy)
        self.widgetUsers.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widgetUsers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widgetUsers.setLineWidth(1)
        self.widgetUsers.setMidLineWidth(0)
        self.widgetUsers.setAlternatingRowColors(True)
        self.widgetUsers.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.widgetUsers.setIconSize(QtCore.QSize(0, 0))
        self.widgetUsers.setShowGrid(False)
        self.widgetUsers.setGridStyle(QtCore.Qt.CustomDashLine)
        self.widgetUsers.setSortingEnabled(True)
        self.widgetUsers.setObjectName("widgetUsers")
        self.groupBox_3 = QtWidgets.QGroupBox(Users)
        self.groupBox_3.setGeometry(QtCore.QRect(430, 0, 411, 71))
        self.groupBox_3.setStyleSheet("")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnRemove = QtWidgets.QPushButton(self.groupBox_3)
        self.btnRemove.setGeometry(QtCore.QRect(250, 30, 71, 31))
        self.btnRemove.setObjectName("btnRemove")
        self.btnEdit = QtWidgets.QPushButton(self.groupBox_3)
        self.btnEdit.setGeometry(QtCore.QRect(330, 30, 71, 31))
        self.btnEdit.setObjectName("btnEdit")
        self.select_user = QtWidgets.QComboBox(self.groupBox_3)
        self.select_user.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.select_user.setObjectName("select_user")
        self.groupBox_2 = QtWidgets.QGroupBox(Users)
        self.groupBox_2.setGeometry(QtCore.QRect(90, -2, 311, 71))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.search_users = QtWidgets.QLineEdit(self.groupBox_2)
        self.search_users.setGeometry(QtCore.QRect(10, 30, 221, 31))
        self.search_users.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly)
        self.search_users.setObjectName("search_users")
        self.btnSearch = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSearch.setGeometry(QtCore.QRect(236, 30, 61, 31))
        self.btnSearch.setObjectName("btnSearch")
        self.btnClose = QtWidgets.QPushButton(Users)
        self.btnClose.setGeometry(QtCore.QRect(758, 524, 81, 31))
        self.btnClose.setObjectName("btnClose")
        self.name = QtWidgets.QLineEdit(Users)
        self.name.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.name.setObjectName("name")
        self.username = QtWidgets.QLineEdit(Users)
        self.username.setGeometry(QtCore.QRect(20, 160, 131, 31))
        self.username.setObjectName("username")
        self.email = QtWidgets.QLineEdit(Users)
        self.email.setGeometry(QtCore.QRect(20, 280, 131, 31))
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(Users)
        self.password.setGeometry(QtCore.QRect(20, 220, 131, 31))
        self.password.setObjectName("password")
        self.phone = QtWidgets.QLineEdit(Users)
        self.phone.setGeometry(QtCore.QRect(20, 340, 131, 31))
        self.phone.setObjectName("phone")
        self.btnUpdate = QtWidgets.QPushButton(Users)
        self.btnUpdate.setGeometry(QtCore.QRect(20, 523, 131, 31))
        self.btnUpdate.setObjectName("btnUpdate")
        self.status = QtWidgets.QComboBox(Users)
        self.status.setGeometry(QtCore.QRect(20, 460, 131, 31))
        self.status.setObjectName("status")
        self.label = QtWidgets.QLabel(Users)
        self.label.setGeometry(QtCore.QRect(20, 80, 68, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Users)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 71, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Users)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 71, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Users)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 41, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Users)
        self.label_5.setGeometry(QtCore.QRect(20, 317, 68, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Users)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 81, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Users)
        self.label_7.setGeometry(QtCore.QRect(20, 440, 68, 17))
        self.label_7.setObjectName("label_7")
        self.user_type = QtWidgets.QComboBox(Users)
        self.user_type.setGeometry(QtCore.QRect(20, 400, 131, 31))
        self.user_type.setObjectName("user_type")

        self.retranslateUi(Users)
        self.btnClose.clicked.connect(Users.close)
        self.btnUpdate.clicked.connect(lambda: self.update_records())
        self.search_users.textChanged.connect(lambda: self.search())
        self.btnRemove.clicked.connect(lambda: self.delete_record())
        self.btnEdit.clicked.connect(lambda: self.populate_fileds())
        self.btnSearch.clicked.connect(lambda: self.search())
        sql.connectDB()
        model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        query.exec_("select * from users")
        if query:
            model.setQuery(query)
            self.select_user.setModel(model)
            self.select_user.setModelColumn(3)
        self.show_users()
        QtCore.QMetaObject.connectSlotsByName(Users)

    def retranslateUi(self, Users):
        _translate = QtCore.QCoreApplication.translate
        Users.setWindowTitle(_translate("Users", "All users"))
        self.btnRemove.setText(_translate("Users", "Delete"))
        self.btnEdit.setText(_translate("Users", "Edit"))
        self.groupBox_2.setTitle(_translate("Users", "Search by:"))
        self.btnSearch.setText(_translate("Users", "Search"))
        self.btnClose.setText(_translate("Users", "Close"))
        self.btnUpdate.setText(_translate("Users", "Update Employee"))
        self.label.setText(_translate("Users", "Name:"))
        self.label_2.setText(_translate("Users", "Username:"))
        self.label_3.setText(_translate("Users", "Password:"))
        self.label_4.setText(_translate("Users", "Email:"))
        self.label_5.setText(_translate("Users", "Phone:"))
        self.label_6.setText(_translate("Users", "User type:"))
        self.label_7.setText(_translate("Users", "Status:"))


    def show_users(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        model.setTable("users")
        model.select()
        model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Full Name")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Password")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Email")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Phone")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Username")
        model.setHeaderData(6, QtCore.Qt.Horizontal, "Type")
        model.setHeaderData(7, QtCore.Qt.Horizontal, "Status")
        self.widgetUsers.setModel(model)
        self.widgetUsers.setColumnHidden(0, True)
        self.widgetUsers.setColumnHidden(2, True)
        self.widgetUsers.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.widgetUsers.show()

    def update_view(self):
        model = QtSql.QSqlQueryModel()
        sql.connectDB()
        query = QtSql.QSqlQuery()
        query.exec_("select * from users")
        if query:
            model.setQuery(query)
            self.select_user.setModel(model)
            self.select_user.setModelColumn(3)
            model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            model.setHeaderData(1, QtCore.Qt.Horizontal, "Full Name")
            model.setHeaderData(2, QtCore.Qt.Horizontal, "Password")
            model.setHeaderData(4, QtCore.Qt.Horizontal, "Email")
            model.setHeaderData(5, QtCore.Qt.Horizontal, "Phone")
            model.setHeaderData(3, QtCore.Qt.Horizontal, "Username")
            model.setHeaderData(6, QtCore.Qt.Horizontal, "Type")
            model.setHeaderData(7, QtCore.Qt.Horizontal, "Status")
            self.widgetUsers.setModel(model)
            self.widgetUsers.setColumnHidden(0, True)
            self.widgetUsers.setColumnHidden(2, True)
            self.widgetUsers.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

    def populate_fileds(self):
        connection = sqlite3.connect("ims.db")
        if connection:
            self.cursor = connection.cursor()
            self.cursor.execute("select * from users where username = '{0}'".format(
                str(self.select_user.currentText())))
            rows = self.cursor.fetchall()

            if rows:
                if str(rows[0][6]) == "Admin":
                    other = "Employee"
                else:
                    other = "Admin"

                if str(rows[0][7]) == "Active":
                    state = "Inactive"
                else:
                    state = "Active"

                self.btnUpdate.setEnabled(True)
                self.name.setText(rows[0][1])
                self.password.setText(rows[0][2])
                self.username.setText(str(rows[0][3]))
                self.email.setText(str(rows[0][4]))
                self.phone.setText(str(rows[0][5]))
                self.user_type.addItem("")
                self.user_type.addItem("")
                self.user_type.setItemText(0, str(rows[0][6]))
                self.user_type.setItemText(1, other)
                self.status.addItem("")
                self.status.addItem("")
                self.status.setItemText(0, str(rows[0][7]))
                self.status.setItemText(1, state)
                self.btnUpdate.setEnabled(True)
            else:
                self.btnUpdate.setDisabled(True)

    def delete_record(self):
        if sql.connectDB():
            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete?"), QtWidgets.qApp.tr("Are "
                        "you sure you want to delete this user?"), QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if confirm == QtWidgets.QMessageBox.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("delete from users where username = ?")
                query.bindValue(0, self.select_user.currentText())
                if query.exec_():
                    self.update_view()
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("User deleted!"),
                                                      QtWidgets.qApp.tr("User has been deleted"),
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("User not deleted!"),
                                               QtWidgets.qApp.tr("User couldn't be deleted"),
                                               QtWidgets.QMessageBox.Ok)

    def search(self):
        sql.connectDB()
        if not self.search_users.text() == '' or not self.search_users.text().isspace():
            qry = QtSql.QSqlQuery()
            qry.prepare("select * from users where name LIKE '%{0}%' or username LIKE '%{0}%' or phone LIKE '%{0}%'"
                        " or email LIKE '%{0}%'".format(str(self.search_users.text())))
            if qry.exec_():
                model = QtSql.QSqlQueryModel()
                model.setQuery(qry)
                model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
                model.setHeaderData(1, QtCore.Qt.Horizontal, "Full Name")
                model.setHeaderData(2, QtCore.Qt.Horizontal, "Password")
                model.setHeaderData(4, QtCore.Qt.Horizontal, "Email")
                model.setHeaderData(5, QtCore.Qt.Horizontal, "Phone")
                model.setHeaderData(3, QtCore.Qt.Horizontal, "Username")
                model.setHeaderData(6, QtCore.Qt.Horizontal, "Type")
                model.setHeaderData(7, QtCore.Qt.Horizontal, "Status")
                self.widgetUsers.setModel(model)
                self.widgetUsers.setColumnHidden(0, True)
                self.widgetUsers.setColumnHidden(2, True)
                self.widgetUsers.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.widgetUsers.show()

    def update_records(self):
        sql.connectDB()
        qry = QtSql.QSqlQuery()

        qry.prepare("UPDATE users SET name = ?, phone = ?, username = ?, password = ?, email = ?,"
            "user_type = ?, status = ? WHERE username = ?")

        qry.bindValue(0, self.name.text())
        qry.bindValue(1, self.phone.text())
        qry.bindValue(2, self.username.text())
        qry.bindValue(3, self.password.text())
        qry.bindValue(4, self.email.text())
        qry.bindValue(5, self.user_type.currentText())
        qry.bindValue(6, self.status.currentText())
        qry.bindValue(7, self.select_user.currentText())

        if qry.exec_():
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Updated Successfully"),
                                              QtWidgets.qApp.tr("\nUser information has been successfully updated"),
                                              QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Updated"),
                                              QtWidgets.qApp.tr("Data update not successful"),
                                              QtWidgets.QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Users = QtWidgets.QFrame()
    ui = Ui_Users()
    ui.setupUi(Users)
    Users.show()
    sys.exit(app.exec_())

