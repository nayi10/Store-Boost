# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
from functions import num_rows

class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(496, 498)
        Registration.setMaximumSize(QtCore.QSize(496, 504))
        Registration.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:7px solid rgb(0, 85, 127);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Registration)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Registration)
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
                                "    height: 28px;\n"
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
"    height: 28px;\n"
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
"    height: 28px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email.setObjectName("email")
        self.gridLayout_4.addWidget(self.email, 2, 0, 1, 1)
        self.phone = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.phone.setStyleSheet("QLineEdit{\n"
"    height: 28px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.phone.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.phone.setObjectName("phone")
        self.gridLayout_4.addWidget(self.phone, 3, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.username.setStyleSheet("QLineEdit{\n"
"    height: 28px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.username.setObjectName("username")
        self.gridLayout_4.addWidget(self.username, 4, 0, 1, 1)
        self.userType = QtWidgets.QComboBox(self.verticalGroupBox_2)
        self.userType.setStyleSheet("QComboBox{\n"
"    height: 28px;\n"
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
"    height: 28px;\n"
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
        self.lblUserType.setStyleSheet("border:0;\n"
"margin-top:-10px;")
        self.lblUserType.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblUserType.setObjectName("lblUserType")
        self.gridLayout_5.addWidget(self.lblUserType, 5, 0, 1, 1)
        self.lblStatus = QtWidgets.QLabel(self.verticalGroupBox)
        self.lblStatus.setStyleSheet("border:0;\n"
"margin-top: -15px;")
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
        self.lblError.raise_()
        self.verticalGroupBox_2.raise_()
        self.btnRegister.raise_()
        self.btnCancel.raise_()
        self.verticalGroupBox.raise_()
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Registration)
        self.btnCancel.clicked.connect(Registration.close)
        self.btnRegister.clicked.connect(lambda: self.new_user())
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "User registration"))
        self.userType.setItemText(0, _translate("Registration", "Admin"))
        self.userType.setItemText(1, _translate("Registration", "Employee"))
        self.status.setItemText(0, _translate("Registration", "Active"))
        self.status.setItemText(1, _translate("Registration", "Inactive"))
        self.lblName.setText(_translate("Registration", "Name:"))
        self.lblPassword.setText(_translate("Registration", "Password:"))
        self.lblEmail.setText(_translate("Registration", "Email:"))
        self.lblPhone.setText(_translate("Registration", "Contact:"))
        self.lblUsername.setText(_translate("Registration", "Username:"))
        self.lblUserType.setText(_translate("Registration", "User Type:"))
        self.lblStatus.setText(_translate("Registration", "Status:"))
        self.btnRegister.setText(_translate("Registration", "Register"))
        self.btnCancel.setText(_translate("Registration", "Cancel"))


    
    def new_user(self):
        if sql.connectDB():
            query = QtSql.QSqlQuery()
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

            if (self.name.text() == '' or self.name.text().isspace()) and (self.username.text() == '' or
                   self.username.text().isspace()) and (self.email.text() == '' or self.email.text().isspace()) and (
                    self.password.text() == '' or self.phone.text() == '' or self.phone.text().isspace()):
                error = 6

            query.prepare("SELECT * from users where username = ? and user_type = ? or phone = ? or email = ?")
            query.bindValue(0, self.username.text())
            query.bindValue(1, self.userType.currentText())
            query.bindValue(2, self.phone.text())
            query.bindValue(3, self.email.text())
            query.exec_()
            if num_rows(query) > 0:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("User exits already"),
                                                  QtWidgets.qApp.tr("\nThe user already exists in the system!"),
                                                  QtWidgets.QMessageBox.Ok)
            else:

                if error == 0:
                    query.prepare("INSERT INTO users(name,password,username,email,phone,user_type,status) "
                          "VALUES(?,?,?,?,?,?,?)")
                    query.bindValue(0, self.name.text())
                    query.bindValue(1, self.password.text())
                    query.bindValue(2, self.username.text())
                    query.bindValue(3, self.email.text())
                    query.bindValue(4, self.phone.text())
                    query.bindValue(5, self.userType.currentText())
                    query.bindValue(6, self.status.currentText())
                    if query.exec_():
                        self.phone.setText("")
                        self.password.setText("")
                        self.name.setText("")
                        self.email.setText("")
                        self.username.setText("")
                        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Successful"),
                                                          QtWidgets.qApp.tr("\nThe user's details have been saved"),
                                                          QtWidgets.QMessageBox.Ok)
                    else:
                        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Not Successful"),
                                                          QtWidgets.qApp.tr("\nThe user could not be registered successfully"),
                                                          QtWidgets.QMessageBox.Ok)

                else:
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Correct Errors!"),
                                                      QtWidgets.qApp.tr("\nPlease enter all required fields "),
                                                      QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QDialog()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())

