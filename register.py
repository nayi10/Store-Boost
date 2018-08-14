# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
from login import *

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(496, 498)
        Register.setMaximumSize(QtCore.QSize(496, 504))
        Register.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:7px solid rgb(0, 85, 127);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Register)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Register)
        self.groupBox.setStyleSheet("border:1px solid #999;\n"
"QLineEdit{\n"
"    padding:8px;\n"
"    height:40px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.verticalGroupBox_2.setStyleSheet("border:0;")
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.verticalGroupBox_2)
        self.gridLayout_4.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.name = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.name.setStyleSheet("QLineEdit{\n"
"    height: 26px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.name.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.name.setMaxLength(255)
        self.name.setObjectName("name")
        self.gridLayout_4.addWidget(self.name, 0, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.password.setStyleSheet("QLineEdit{\n"
"    height: 26px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout_4.addWidget(self.password, 1, 0, 1, 1)
        self.email = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.email.setStyleSheet("QLineEdit{\n"
"    height: 26px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email.setObjectName("email")
        self.gridLayout_4.addWidget(self.email, 2, 0, 1, 1)
        self.phone = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.phone.setStyleSheet("QLineEdit{\n"
"    height: 26px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.phone.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.phone.setObjectName("phone")
        self.gridLayout_4.addWidget(self.phone, 3, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.username.setStyleSheet("QLineEdit{\n"
"    height: 26px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.username.setObjectName("username")
        self.gridLayout_4.addWidget(self.username, 4, 0, 1, 1)
        self.userType = QtWidgets.QComboBox(self.verticalGroupBox_2)
        self.userType.setStyleSheet("QComboBox{\n"
"    height: 25px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.userType.setObjectName("userType")
        self.userType.addItem("")
        self.userType.addItem("")
        self.gridLayout_4.addWidget(self.userType, 5, 0, 1, 1)
        self.status = QtWidgets.QComboBox(self.verticalGroupBox_2)
        self.status.setStyleSheet("QComboBox{\n"
"    height: 25px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.status.setObjectName("status")
        self.status.addItem("")
        self.status.addItem("")
        self.gridLayout_4.addWidget(self.status, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.verticalGroupBox_2, 0, 2, 1, 1)
        self.verticalGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.verticalGroupBox.setStyleSheet("border:0;")
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.verticalGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblName = QtWidgets.QLabel(self.verticalGroupBox)
        self.lblName.setStyleSheet("border:0;")
        self.lblName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblName.setObjectName("lblName")
        self.gridLayout_5.addWidget(self.lblName, 0, 0, 1, 1)
        self.lblPassword = QtWidgets.QLabel(self.verticalGroupBox)
        self.lblPassword.setStyleSheet("border:0;")
        self.lblPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblPassword.setObjectName("lblPassword")
        self.gridLayout_5.addWidget(self.lblPassword, 1, 0, 1, 1)
        self.lblEmail = QtWidgets.QLabel(self.verticalGroupBox)
        self.lblEmail.setStyleSheet("border:0;")
        self.lblEmail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblEmail.setObjectName("lblEmail")
        self.gridLayout_5.addWidget(self.lblEmail, 2, 0, 1, 1)
        self.lblPhone = QtWidgets.QLabel(self.verticalGroupBox)
        self.lblPhone.setStyleSheet("border:0;")
        self.lblPhone.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblPhone.setObjectName("lblPhone")
        self.gridLayout_5.addWidget(self.lblPhone, 3, 0, 1, 1)
        self.lblUsername = QtWidgets.QLabel(self.verticalGroupBox)
        self.lblUsername.setStyleSheet("border:0;")
        self.lblUsername.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblUsername.setObjectName("lblUsername")
        self.gridLayout_5.addWidget(self.lblUsername, 4, 0, 1, 1)
        self.lblUserType = QtWidgets.QLabel(self.verticalGroupBox)
        self.lblUserType.setStyleSheet("border:0;")
        self.lblUserType.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblUserType.setObjectName("lblUserType")
        self.gridLayout_5.addWidget(self.lblUserType, 5, 0, 1, 1)
        self.lblStatus = QtWidgets.QLabel(self.verticalGroupBox)
        self.lblStatus.setStyleSheet("border:0;")
        self.lblStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblStatus.setIndent(0)
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout_5.addWidget(self.lblStatus, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.verticalGroupBox, 0, 0, 1, 1)
        self.btnRegister = QtWidgets.QPushButton(self.groupBox)
        self.btnRegister.setStyleSheet("padding:8px;\n"
"color:#000;\n"
"")
        self.btnRegister.setObjectName("btnRegister")
        self.gridLayout.addWidget(self.btnRegister, 1, 2, 1, 1)
        self.btnCancel = QtWidgets.QPushButton(self.groupBox)
        self.btnCancel.setStyleSheet("padding:8px;\n"
"color:#000;\n"
"")
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 1, 0, 1, 2)
        self.lblError = QtWidgets.QLabel(self.groupBox)
        self.lblError.setGeometry(QtCore.QRect(40, 280, 16, 17))
        self.lblError.setStyleSheet("border:0;\n"
"color:#f00;")
        self.lblError.setText("")
        self.lblError.setObjectName("lblError")
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.btnRegister.clicked.connect(self.add_user)
        self.retranslateUi(Register)
        self.btnCancel.clicked.connect(Register.close)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "User registration"))
        self.userType.setItemText(0, _translate("Register", "Admin"))
        self.userType.setItemText(1, _translate("Register", "Employee"))
        self.status.setItemText(0, _translate("Register", "Active"))
        self.status.setItemText(1, _translate("Register", "Inactive"))
        self.lblName.setText(_translate("Register", "Name:"))
        self.lblPassword.setText(_translate("Register", "Password:"))
        self.lblEmail.setText(_translate("Register", "Email:"))
        self.lblPhone.setText(_translate("Register", "Contact:"))
        self.lblUsername.setText(_translate("Register", "Username:"))
        self.lblUserType.setText(_translate("Register", "User Type:"))
        self.lblStatus.setText(_translate("Register", "Status:"))
        self.btnRegister.setText(_translate("Register", "Register"))
        self.btnCancel.setText(_translate("Register", "Cancel"))

    def login_window(self):
        self.login = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login)
        self.ui.btn_login.clicked.connect(self.ui.validateForm)
        self.login.show()

    def add_user(self):
        error = 0
        if self.name.text() == '' or self.name.text().isspace():
            error = 1
        if self.username.text() == '' or self.username.text().isspace():
            error = 2
        if self.password.text() == '' or self.password.text().isspace():
            error = 3
        if self.email.text() == '' or self.email.text().isspace():
            error = 4
        if self.phone.text() == '' or self.phone.text().isspace():
            error = 5

        if (self.name.text() == '' or self.name.text().isspace()) and (
                self.username.text() == '' or
                self.username.text().isspace()) and (
                self.email.text() == '' or self.email.text().isspace()) and (
                self.password.text() == '' or
                self.password.text().isspace()) and (
                self.phone.text() == '' or self.phone.text().isspace()):
            error = 6

        if error == 0:
            self.insert_data()
            self.login_window()

        else:
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Correct Errors!"),
                                              QtWidgets.qApp.tr("\nPlease all fields are required and must be filled!"),
                                              QtWidgets.QMessageBox.Ok)

    def insert_data(self):
        sql.connectDB()
        self.query = QtSql.QSqlQuery()
        self.query.prepare("SELECT * from users where username = ? and user_type = ? or phone = ? or email = ?")
        self.query.bindValue(0, self.username.text())
        self.query.bindValue(1, self.userType.currentText())
        self.query.bindValue(2, self.phone.text())
        self.query.bindValue(3, self.email.text())
        self.query.exec_()

        if num_rows(self.query) > 0:

            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("User exits already"),
                                              QtWidgets.qApp.tr("\nThe user already exists in the system!"),
                                              QtWidgets.QMessageBox.Ok)
        else:

            self.query.prepare("INSERT INTO users(name,password,username,email,phone,user_type,status) "
                          "VALUES(?,?,?,?,?,?,?)")
            self.query.bindValue(0, self.name.text())
            self.query.bindValue(1, self.password.text())
            self.query.bindValue(2, self.username.text())
            self.query.bindValue(3, self.email.text())
            self.query.bindValue(4, self.phone.text())
            self.query.bindValue(5, self.userType.currentText())
            self.query.bindValue(6, self.status.currentText())
            if self.query.exec_():
                self.phone.setText("")
                self.password.setText("")
                self.name.setText("")
                self.email.setText("")
                self.username.setText("")
                self.status.AdjustToContents
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Successful"),
                                                  QtWidgets.qApp.tr("The user's details have been saved\n"),
                                                  QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Not Successful"),
                                                  QtWidgets.qApp.tr(
                                                      "The user could not be registered successfully"),
                                                  QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

    def singup(self):
        if self.add_user():
            self.close_me()
            self.login_window()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())

