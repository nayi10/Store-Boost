# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newregistration.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
from functions import *

class Ui_frmRegistration(object):
    def setupUi(self, frmRegistration):
        frmRegistration.setObjectName("frmRegistration")
        frmRegistration.resize(465, 430)
        frmRegistration.setMaximumSize(QtCore.QSize(465, 430))
        frmRegistration.setStyleSheet("background-color: rgb(255, 255, 255);")
        frmRegistration.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frmRegistration.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_11 = QtWidgets.QLabel(frmRegistration)
        self.label_11.setGeometry(QtCore.QRect(30, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.groupBox = QtWidgets.QGroupBox(frmRegistration)
        self.groupBox.setGeometry(QtCore.QRect(30, 50, 401, 351))
        self.groupBox.setStyleSheet("border:1px solid #999;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.verticalGroupBox.setGeometry(QtCore.QRect(10, 10, 111, 281))
        self.verticalGroupBox.setStyleSheet("border:0;")
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_5.setStyleSheet("border:0;")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_6.setStyleSheet("border:0;")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_8.setStyleSheet("border:0;")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_7.setStyleSheet("border:0;")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_10 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_10.setStyleSheet("border:0;")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_9.setStyleSheet("border:0;")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_4 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_4.setStyleSheet("border:0;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(120, 10, 231, 281))
        self.verticalGroupBox_2.setStyleSheet("border:0;")
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.name = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.name.setStyleSheet("border:1px solid #999;")
        self.name.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.name.setMaxLength(255)
        self.name.setObjectName("name")
        self.verticalLayout_3.addWidget(self.name)
        self.password = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.password.setStyleSheet("border:1px solid #999;")
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout_3.addWidget(self.password)
        self.email = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.email.setStyleSheet("border:1px solid #999;")
        self.email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email.setObjectName("email")
        self.verticalLayout_3.addWidget(self.email)
        self.phone = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.phone.setStyleSheet("border:1px solid #999;")
        self.phone.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.phone.setObjectName("phone")
        self.verticalLayout_3.addWidget(self.phone)
        self.username = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.username.setStyleSheet("border:1px solid #999;")
        self.username.setObjectName("username")
        self.verticalLayout_3.addWidget(self.username)
        self.userType = QtWidgets.QComboBox(self.verticalGroupBox_2)
        self.userType.setStyleSheet("border:1px solid #999;")
        self.userType.setObjectName("userType")
        self.userType.addItem("")
        self.userType.addItem("")
        self.verticalLayout_3.addWidget(self.userType)
        self.status = QtWidgets.QComboBox(self.verticalGroupBox_2)
        self.status.setStyleSheet("border:1px solid #999;")
        self.status.setObjectName("status")
        self.status.addItem("")
        self.status.addItem("")
        self.verticalLayout_3.addWidget(self.status)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 290, 251, 51))
        self.groupBox_2.setStyleSheet("border:0;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnRegister = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRegister.setGeometry(QtCore.QRect(20, 10, 99, 31))
        self.btnRegister.setStyleSheet("border:1px solid #999")
        self.btnRegister.setObjectName("btnRegister")
        self.btnCancel = QtWidgets.QPushButton(self.groupBox_2)
        self.btnCancel.setGeometry(QtCore.QRect(130, 10, 99, 31))
        self.btnCancel.setStyleSheet("border:1px solid #999;")
        self.btnCancel.setFlat(False)
        self.btnCancel.setObjectName("btnCancel")

        self.retranslateUi(frmRegistration)
        QtCore.QMetaObject.connectSlotsByName(frmRegistration)

    def retranslateUi(self, frmRegistration):
        _translate = QtCore.QCoreApplication.translate
        frmRegistration.setWindowTitle(_translate("frmRegistration", "User Registration"))
        self.label_11.setText(_translate("frmRegistration", "Registration"))
        self.label_5.setText(_translate("frmRegistration", "Name:"))
        self.label_6.setText(_translate("frmRegistration", "Password:"))
        self.label_8.setText(_translate("frmRegistration", "Email:"))
        self.label_7.setText(_translate("frmRegistration", "Contact:"))
        self.label_10.setText(_translate("frmRegistration", "Username:"))
        self.label_9.setText(_translate("frmRegistration", "User Type:"))
        self.label_4.setText(_translate("frmRegistration", "Status:"))
        self.userType.setItemText(0, _translate("frmRegistration", "Employee"))
        self.userType.setItemText(1, _translate("frmRegistration", "Admin"))
        self.status.setItemText(0, _translate("frmRegistration", "Active"))
        self.status.setItemText(1, _translate("frmRegistration", "Inactive"))
        self.btnRegister.setText(_translate("frmRegistration", "Register"))
        self.btnCancel.setText(_translate("frmRegistration", "Cancel"))

def mainWindow(qwid):
    if sql.connectDB():
        query = QtSql.QSqlQuery()
        query.exec_("SELECT * from users")
        frmRegistration = QtWidgets.QFrame(qwid)
        u = Ui_frmRegistration()
        u.setupUi(frmRegistration)
        signup = QtWidgets.QFrame()
        typ = u.userType.currentText()
        status = u.status.currentText()

        def add_user():
            error = 0
            if u.name.text() == '' or u.name.text().isspace():
                error = 1
            if u.username.text() == '' or u.username.text().isspace():
                error = 2
            if u.password.text() == '' or u.password.text().isspace():
                error = 3
            if u.email.text() == '' or u.email.text().isspace():
                error = 4
            if u.phone.text() == '' or u.phone.text().isspace():
                error = 5

            if (u.name.text() == '' or u.name.text().isspace()) and (u.username.text() == '' or
                                                                     u.username.text().isspace()) and (
                    u.email.text() == '' or u.email.text().isspace()) and (u.password.text() == '' or
                                                                           u.password.text().isspace()) and (
                    u.phone.text() == '' or u.phone.text().isspace()):
                error = 6


            if error == 0:
                insert_data()
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Correct Errors!"),
                                                  QtWidgets.qApp.tr("Please enter all details "),
                                                  QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)


        def insert_data():
            query.prepare("INSERT INTO users(name,password,username,email,phone,user_type,status) "
                          "VALUES(?,?,?,?,?,?,?)")
            query.bindValue(0, u.name.text())
            query.bindValue(1, u.password.text())
            query.bindValue(2, u.username.text())
            query.bindValue(3, u.email.text())
            query.bindValue(4, u.phone.text())
            query.bindValue(5, typ)
            query.bindValue(6, status)
            if query.exec_():
                u.phone.setText("")
                u.password.setText("")
                u.name.setText("")
                u.email.setText("")
                u.username.setText("")
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Successful"),
                                                  QtWidgets.qApp.tr("The user's details have been saved\n"),
                                                  QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Not Successful"),
                                                  QtWidgets.qApp.tr("The user could not be registered successfully"),
                                                  QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

        frmRegistration.setGeometry(450, 100, 750, 500)
        frmRegistration.setMaximumWidth(750)
        frmRegistration.setWindowTitle("Register now")
        u.btnRegister.setStyleSheet("background-color:#768355;color:#fff;")
        u.btnCancel.clicked.connect(quit)
        u.btnRegister.clicked.connect(add_user)
        frmRegistration.show()
