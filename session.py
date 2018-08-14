from PyQt5 import QtWidgets, QtCore

class NewSession(QtWidgets.QDialog):
    def setupUi(self, NewSession):
        NewSession.setObjectName("EditDebtors")
        NewSession.setWindowTitle("Login")
        self.setGeometry(560, 120, 200, 330)
        self.btnNewLogin = QtWidgets.QPushButton(NewSession)
        self.btnNewLogin.setGeometry(25, 30, 180, 40)
        NewSession.setMaximumSize(230, 120)

        self.retranslateUi(NewSession)
        QtCore.QMetaObject.connectSlotsByName(NewSession)

    def retranslateUi(self, NewSession):
        _translate = QtCore.QCoreApplication.translate
        NewSession.setWindowTitle(_translate("NewSession", "Start a new session"))
        self.btnNewLogin.setText(_translate("NewSession", "Start new session"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QDialog()
    session = NewSession()
    session.setupUi(win)
    session.setWindowTitle("Start new session")
    win.show()
    sys.exit(app.exec_())