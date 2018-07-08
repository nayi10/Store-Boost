# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categories.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_Category(object):
    def setupUi(self, Category):
        Category.setObjectName("Category")
        Category.resize(668, 523)
        Category.setMinimumSize(QtCore.QSize(0, 0))
        Category.setMaximumSize(QtCore.QSize(668, 540))
        self.buttonBox = QtWidgets.QDialogButtonBox(Category)
        self.buttonBox.setGeometry(QtCore.QRect(270, 470, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox_2 = QtWidgets.QGroupBox(Category)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 390, 381, 61))
        self.groupBox_2.setStyleSheet("border:1px solid #ccc;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.categoryName = QtWidgets.QLineEdit(self.groupBox_2)
        self.categoryName.setGeometry(QtCore.QRect(100, 20, 261, 27))
        self.categoryName.setObjectName("categoryName")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:0;")
        self.label_2.setLineWidth(0)
        self.label_2.setObjectName("label_2")
        self.categoryView = QtWidgets.QListView(Category)
        self.categoryView.setGeometry(QtCore.QRect(40, 128, 591, 251))
        self.categoryView.setStyleSheet("border:2px solid #dcdcdc;")
        self.categoryView.setObjectName("categoryView")
        self.label = QtWidgets.QLabel(Category)
        self.label.setGeometry(QtCore.QRect(41, 90, 590, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 48, 70);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(Category)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 0, 410, 71))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.filter = QtWidgets.QLineEdit(self.groupBox_3)
        self.filter.setGeometry(QtCore.QRect(70, 30, 261, 27))
        self.filter.setObjectName("filter")
        self.btnFilter = QtWidgets.QPushButton(self.groupBox_3)
        self.btnFilter.setObjectName("btnFilter")
        self.btnFilter.setGeometry(QtCore.QRect(335, 30, 65, 27))
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnUpdate = QtWidgets.QPushButton(Category)
        self.btnUpdate.setGeometry(QtCore.QRect(430, 400, 100, 41))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnSave = QtWidgets.QPushButton(Category)
        self.btnSave.setGeometry(QtCore.QRect(550, 400, 80, 41))
        self.btnSave.setObjectName("btnSave")
        self.btnDelete = QtWidgets.QPushButton(Category)
        self.btnDelete.setGeometry(QtCore.QRect(480, 25, 140, 41))
        self.btnDelete.setObjectName("btnDelete")

        self.retranslateUi(Category)
        self.buttonBox.accepted.connect(Category.accept)
        self.buttonBox.rejected.connect(Category.reject)
        QtCore.QMetaObject.connectSlotsByName(Category)

    def retranslateUi(self, Category):
        _translate = QtCore.QCoreApplication.translate
        Category.setWindowTitle(_translate("Category", "Categories"))
        self.label_2.setText(_translate("Category", "Category"))
        self.label.setText(_translate("Category", "Categories"))
        self.filter.setPlaceholderText(_translate("Category", "Filter"))
        self.label_4.setText(_translate("Category", "Filter"))
        self.btnFilter.setText(_translate("Category", "Filter"))
        self.btnUpdate.setText(_translate("Category", "Update"))
        self.btnSave.setText(_translate("Category", "Save"))
        self.btnDelete.setText(_translate("Category", "Delete Selected"))

    
    def get_category(self):

        if self.filter.text() == '' or self.filter.text().isspace():
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Enter filter query"), QtWidgets.qApp.tr(
                "Please enter filter criterion to filter!"), QtWidgets.QMessageBox.Ok)
        else:
            qry = QtSql.QSqlQuery()
            qry.prepare("select name from categories where id LIKE '%{0}%' or name LIKE '%{0}%'".format(str(
                self.filter.text())))
            if qry.exec_():
                model = QtSql.QSqlQueryModel()
                model.setQuery(qry)
                self.categoryView.setModel(model)
                self.categoryView.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Category = QtWidgets.QDialog()
    ui = Ui_Category()
    ui.setupUi(Category)
    Category.show()
    sys.exit(app.exec_())

