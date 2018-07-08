from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
from PyQt5.QtSql import QSqlQuery
from login import *
import sql
from register import *
from functions import num_rows


def main():
    if sql.connectDB():
        query = QSqlQuery()
        query.exec_("SELECT * from users")

        if num_rows(query) < 1:
            import sys
            app = QtWidgets.QApplication(sys.argv)
            signup = QtWidgets.QFrame()
            u = Ui_Register()
            u.setupUi(signup)
            name = u.name.text()
            username = u.username.text()
            email = u.email.text()
            password = u.password.text()
            phone = u.phone.text()
            typ = u.userType.currentText()
            status = u.status.currentText()

            def register_user():
                error = 0
                if u.name.text() == '' or u.name.text().isspace():
                    u.lblError.setText("Please enter name")
                    error = 1
                if u.username.text() == '' or u.username.text().isspace():
                    u.lblError.setText("Please enter username")
                    error = 2
                if u.password.text() == '' or u.password.text().isspace():
                    u.lblError.setText("Please enter password")
                    error = 3
                if u.email.text() == '' or u.email.text().isspace():
                    u.lblError.setText("Please enter email")
                    error = 4
                if u.phone.text() == '' or u.phone.text().isspace():
                    u.lblError.setText("Please enter phone number")
                    error = 5

                if (u.name.text() == '' or u.name.text().isspace()) and (u.username.text() == '' or
                                                                         u.username.text().isspace()) and (
                        u.email.text() == '' or u.email.text().isspace()) and (u.password.text() == '' or
                                                                               u.password.text().isspace()) and (
                        u.phone.text() == '' or u.phone.text().isspace()):
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Correct Errors!"),
                                                      QtWidgets.qApp.tr("Please enter all details "),
                                                      QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

                    u.lblError.setText("")

                if error == 0:
                    insert_data()

            def insert_data():
                query.prepare("INSERT INTO users(name,password,username,email,phone,user_type,status) "
                              "VALUES(?,?,?,?,?,?,?)")
                query.bindValue(0, u.name.text())
                query.bindValue(1, u.password.text())
                query.bindValue(2, u.username.text())
                query.bindValue(3, u.email.text())
                query.bindValue(4, u.phone.text())
                query.bindValue(5, u.userType.currentText())
                query.bindValue(6, u.status.currentText())
                if query.exec_():
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Successful"),
                                                      QtWidgets.qApp.tr("Your user details have been saved\n"
                                                                        "You can now login using your username and password"),
                                                      QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Not Successful"),
                                                      QtWidgets.qApp.tr("Registration could not be processed successfully"),
                                                      QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)


            signup.setGeometry(500, 150, 750, 500)
            signup.setMaximumWidth(750)
            signup.setWindowTitle("Register now")
            signup.show()
            u.btnCancel.clicked.connect(quit)
            u.btnRegister.clicked.connect(register_user)
            sys.exit(app.exec_())
        else:
            import sys
            app = QtWidgets.QApplication(sys.argv)
            Login = QtWidgets.QFrame()
            ui = Ui_Login()
            ui.setupUi(Login)

            def validateForm():
                error = 0
                if (ui.username.text().isspace() or ui.username.text() == '') and (ui.password.text().isspace() or ui.password.text() == ''):
                    ui.lbl_error.setText("Please enter your username and password.\n")
                    error = 1
                else:
                    if ui.username.text().isspace() or ui.username.text() == '':
                        ui.lbl_error.setText("Please enter your username")
                        error = 2
                    else:
                        username = ui.username.text()

                    if ui.password.text().isspace() or ui.password.text() == '':
                        ui.lbl_error.setText("Please enter your password")
                        error = 3
                    else:
                        ui.lbl_error.clear()
                        password = ui.password.text()

                    if error == 0:
                        query = QtSql.QSqlQuery()
                        query.prepare("SELECT * from users where username = ? and password = ?")
                        query.bindValue(0, username)
                        query.bindValue(1, password)
                        if num_rows(query) > 0:
                            Login.close()
                        else:
                            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not registered"),
                                QtWidgets.qApp.tr("There is no user with those details\n"
                                                  "Ensure you're registered before trying!\n"
                                                  "to login!"),
                                QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Close)

            Login.setGeometry(500,150,750,500)
            Login.setMaximumWidth(750)
            Login.setWindowTitle("Enter Your Details To Login")
            Login.show()
            ui.btn_cancel.clicked.connect(quit)
            ui.btn_login.clicked.connect(validateForm)
            sys.exit(app.exec_())

if __name__ == "__main__":
    main()