# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debtorscreditors.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmDebtorsCreditors(object):
    def setupUi(self, frmDebtorsCreditors):
        frmDebtorsCreditors.setObjectName("frmDebtorsCreditors")
        frmDebtorsCreditors.resize(731, 246)
        frmDebtorsCreditors.setMaximumSize(QtCore.QSize(731, 500))
        frmDebtorsCreditors.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frmDebtorsCreditors.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2 = QtWidgets.QLabel(frmDebtorsCreditors)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 511, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 48, 70);\n"
"background-color: rgb(0, 111, 163);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(frmDebtorsCreditors)
        self.groupBox_2.setGeometry(QtCore.QRect(110, 89, 511, 91))
        self.groupBox_2.setStyleSheet("border:1px solid #ccc;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnDebtors = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDebtors.setGeometry(QtCore.QRect(30, 20, 121, 51))
        self.btnDebtors.setStyleSheet("background-color: rgb(255, 255,255);\n"
"color: rgb(0, 0, 0);\n"
"padding:4px;\n"
"border-radius:3px;")
        self.btnDebtors.setObjectName("btnDebtors")
        self.btnCreditors = QtWidgets.QPushButton(self.groupBox_2)
        self.btnCreditors.setGeometry(QtCore.QRect(190, 20, 121, 51))
        self.btnCreditors.setStyleSheet("background-color: rgb(255, 255,255);\n"
"color: rgb(0, 0, 0);\n"
"padding:4px;\n"
"border-radius:3px;")
        self.btnCreditors.setObjectName("btnCreditors")
        self.btnClose = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClose.setGeometry(QtCore.QRect(350, 20, 121, 51))
        self.btnClose.setStyleSheet("background-color: rgb(255, 255,255);\n"
"color: rgb(0, 0, 0);\n"
"padding:4px;\n"
"border-radius:3px;")
        self.btnClose.setObjectName("btnClose")
        self.btnDebtors.raise_()
        self.btnCreditors.raise_()
        self.btnClose.raise_()

        self.retranslateUi(frmDebtorsCreditors)
        QtCore.QMetaObject.connectSlotsByName(frmDebtorsCreditors)

    def retranslateUi(self, frmDebtorsCreditors):
        _translate = QtCore.QCoreApplication.translate
        frmDebtorsCreditors.setWindowTitle(_translate("frmDebtorsCreditors", "Debtors and Creditors"))
        self.label_2.setText(_translate("frmDebtorsCreditors", "Debtors and Creditors Report"))
        self.btnDebtors.setText(_translate("frmDebtorsCreditors", "Debtors"))
        self.btnCreditors.setText(_translate("frmDebtorsCreditors", "Creditors"))
        self.btnClose.setText(_translate("frmDebtorsCreditors", "Close"))


def showDebtorsCreditors():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        frmDebtorsCreditors = QtWidgets.QFrame()
        ui = Ui_frmDebtorsCreditors()
        ui.setupUi(frmDebtorsCreditors)
        frmDebtorsCreditors.show()
        sys.exit(app.exec_())
