# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customerlist.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_Customers(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1199, 614)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(810, 570, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(50, 100, 1101, 451))
        self.tableView.setObjectName("tableView")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 10, 681, 80))
        self.groupBox_2.setStyleSheet("border:1px solid #ccc;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 10, 241, 61))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 81, 20))
        self.label_7.setStyleSheet("border:0;")
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 191, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(270, 10, 371, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("border: 1px solid #ccc")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCancel = QtWidgets.QPushButton(self.groupBox)
        self.btnCancel.setStyleSheet("background-color: rgb(220, 0, 0);\n"
"alternate-background-color: rgb(170, 0, 0);\n"
"selection-background-color: rgb(216, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"padding:8px;\n"
"border-radius:3px;")
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.btnExportExcel = QtWidgets.QPushButton(self.groupBox)
        self.btnExportExcel.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"border-radius:3px;\n"
"color: rgb(255, 255, 255);\n"
"padding:8px;")
        self.btnExportExcel.setObjectName("btnExportExcel")
        self.horizontalLayout.addWidget(self.btnExportExcel)
        self.btnExportCSV = QtWidgets.QPushButton(self.groupBox)
        self.btnExportCSV.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"padding:8px;\n"
"border-radius:3px;")
        self.btnExportCSV.setObjectName("btnExportCSV")
        self.horizontalLayout.addWidget(self.btnExportCSV)
        self.btnReset = QtWidgets.QPushButton(self.groupBox)
        self.btnReset.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);padding:8px;border-radius:3px;")
        self.btnReset.setObjectName("btnReset")
        self.horizontalLayout.addWidget(self.btnReset)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "All customers"))
        self.label_7.setText(_translate("Dialog", "Filter by:"))
        self.comboBox.setItemText(0, _translate("Dialog", "Customer Name"))
        self.comboBox.setItemText(1, _translate("Dialog", "City"))
        self.comboBox.setItemText(2, _translate("Dialog", "Phone"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))
        self.btnExportExcel.setText(_translate("Dialog", "Export Excel"))
        self.btnExportCSV.setText(_translate("Dialog", "Export CSV"))
        self.btnReset.setText(_translate("Dialog", "Reset"))


    def selectCustomers(self):
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
        self.tableView.horizontalHeader().setMinimumHeight(35)
        self.tableView.horizontalHeader().setStyleSheet("background-color:#444;color:#fff;")
        self.tableView.setColumnHidden(0, True)
        self.tableView.show()
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     CustomerLists = QtWidgets.QDialog()
#     CustomerLists.setGeometry(120, 100, 1201, 760)
#     ui = Ui_Dialog()
#     ui.setupUi(CustomerLists)
#     ui.selectCustomers()
#     CustomerLists.show()
#     sys.exit(app.exec_())