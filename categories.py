# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/categories.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_Category(object):
    def setupUi(self, Category):
        Category.setObjectName("Category")
        Category.resize(671, 523)
        Category.setMinimumSize(QtCore.QSize(0, 0))
        Category.setMaximumSize(QtCore.QSize(729, 540))
        self.groupBox_2 = QtWidgets.QGroupBox(Category)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 430, 471, 71))
        self.groupBox_2.setStyleSheet("border:1px solid #ccc;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.categoryName = QtWidgets.QLineEdit(self.groupBox_2)
        self.categoryName.setGeometry(QtCore.QRect(100, 19, 351, 31))
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
        self.categoryView.setGeometry(QtCore.QRect(40, 128, 591, 281))
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
        self.groupBox_3.setGeometry(QtCore.QRect(40, 0, 231, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.filter = QtWidgets.QLineEdit(self.groupBox_3)
        self.filter.setGeometry(QtCore.QRect(10, 30, 211, 31))
        self.filter.setObjectName("filter")
        self.btnUpdate = QtWidgets.QPushButton(Category)
        self.btnUpdate.setGeometry(QtCore.QRect(520, 430, 111, 31))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnSave = QtWidgets.QPushButton(Category)
        self.btnSave.setGeometry(QtCore.QRect(520, 470, 111, 31))
        self.btnSave.setObjectName("btnSave")
        self.groupBox_4 = QtWidgets.QGroupBox(Category)
        self.groupBox_4.setGeometry(QtCore.QRect(300, 0, 331, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.delete_select = QtWidgets.QComboBox(self.groupBox_4)
        self.delete_select.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.delete_select.setObjectName("delete_select")
        self.btnDelete = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDelete.setGeometry(QtCore.QRect(250, 30, 71, 31))
        self.btnDelete.setObjectName("btnDelete")

        sql.connectDB()
        model = QtSql.QSqlQueryModel()
        qry = QtSql.QSqlQuery()
        qry.exec_("select distinct name from categories")
        model.setQuery(qry)
        self.categoryView.setModel(model)
        self.delete_select.setModel(model)
        completer = QtWidgets.QCompleter()
        completer.setModel(model)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        completer.setWidget(self.filter)
        self.filter.setCompleter(completer)
        self.filter.textChanged.connect(lambda: self.get_category())

        self.retranslateUi(Category)
        QtCore.QMetaObject.connectSlotsByName(Category)

    def retranslateUi(self, Category):
        _translate = QtCore.QCoreApplication.translate
        Category.setWindowTitle(_translate("Category", "Categories"))
        self.label_2.setText(_translate("Category", "Category"))
        self.label.setText(_translate("Category", "Categories"))
        self.groupBox_3.setTitle(_translate("Category", "Filter"))
        self.filter.setPlaceholderText(_translate("Category", "Filter"))
        self.btnUpdate.setText(_translate("Category", "Update Item"))
        self.btnSave.setText(_translate("Category", "Save New"))
        self.groupBox_4.setTitle(_translate("Category", "Delete item"))
        self.btnDelete.setText(_translate("Category", "Delete"))


    def stylesheet(self):
        return """

            QListView::item {
                padding: 10px 20px;
            }

            * {
                font-size:14px;
            }

            QTableView::horizontalHeader{
                background-color: #111111;
                color: #efefef;
            }

            QPushButton:hover{
            background-color:#ffffff;
            color: #222222;
            }

            QPushButton{
            background-color: #cdcdcd;
            }

            QTableView::row{
            padding:15px;
            }

            QTableView::column{
            padding:15px;
            }

        """
    def get_category(self):
        sql.connectDB()
        if not self.filter.text() == '' or not self.filter.text().isspace():
            qry = QtSql.QSqlQuery()
            qry.prepare("select name from categories where name LIKE '%{0}%'".format(str(
                self.filter.text())))
            if qry.exec_():
                self.model = QtSql.QSqlQueryModel()
                self.model.setQuery(qry)
                self.categoryView.setModel(self.model)
                self.categoryView.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Category = QtWidgets.QDialog()
    ui = Ui_Category()
    ui.setupUi(Category)
    Category.show()
    sys.exit(app.exec_())

