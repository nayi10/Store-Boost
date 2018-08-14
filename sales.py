# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/sales.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sqlite3
from time import strftime, gmtime
import sql

class Ui_Sales(object):
    def setupUi(self, Sales):
        Sales.setObjectName("Sales")
        Sales.resize(976, 593)
        self.saleView = QtWidgets.QTableView(Sales)
        self.saleView.setGeometry(QtCore.QRect(30, 47, 914, 500))
        self.saleView.setObjectName("saleView")
        self.search = QtWidgets.QLineEdit(Sales)
        self.search.setGeometry(QtCore.QRect(30, 4, 200, 33))
        self.search.setStyleSheet("min-width:220px;\n"
"padding:5px;")
        self.search.setObjectName("search")
        self.search.setObjectName("search")
        self.btnSearch = QtWidgets.QPushButton(Sales)
        self.btnSearch.setGeometry(QtCore.QRect(260, 0, 80, 41))
        self.btnSearch.setStyleSheet("padding:5px 10px;\n"
"margin:5px;")
        self.btnSearch.setObjectName("btnSearch")
        self.selectSale = QtWidgets.QComboBox(Sales)
        self.selectSale.setGeometry(QtCore.QRect(350, 4, 230, 33))
        self.selectSale.setStyleSheet("min-width:220px;\n"
"padding:5px;")
        self.selectSale.setObjectName("selectSale")
        self.btnDelete = QtWidgets.QPushButton(Sales)
        self.btnDelete.setGeometry(QtCore.QRect(580, 0, 81, 41))
        self.btnDelete.setStyleSheet("padding:5px 10px;\n"
"margin:5px;")
        self.btnDelete.setObjectName("btnDelete")
        self.btnView = QtWidgets.QPushButton(Sales)
        self.btnView.setGeometry(QtCore.QRect(654, 0, 120, 41))
        self.btnView.setStyleSheet("padding:5px 10px;\n"
                                   "margin:5px;")
        self.btnView.setObjectName("btnView")
        self.btnNewSale = QtWidgets.QPushButton(Sales)
        self.btnNewSale.setGeometry(QtCore.QRect(770, 0, 95, 41))
        self.btnNewSale.setStyleSheet("padding:5px;\n"
"margin:5px;")
        self.btnNewSale.setObjectName("btnNewSale")

        self.btnExit = QtWidgets.QPushButton(Sales)
        self.btnExit.setGeometry(QtCore.QRect(865, 0, 81, 41))
        self.btnExit.setStyleSheet("padding:5px 10px;\n"
"margin:5px;")
        self.btnExit.setObjectName("btnExit")
        self.label12 = QtWidgets.QLabel(Sales)
        self.label12.setGeometry(QtCore.QRect(750, 550, 100, 41))
        self.label12.setStyleSheet("font-size:16px;font-weight:bold;")
        self.lblTotal = QtWidgets.QLabel(Sales)
        self.lblTotal.setGeometry(QtCore.QRect(850, 550, 80, 41))
        self.lblTotal.setStyleSheet("font-size:16px;font-weight:bold;")

        self.retranslateUi(Sales)
        self.stylesheet()
        self.update_view()
        self.btnExit.clicked.connect(Sales.close)
        self.btnSearch.clicked.connect(lambda: self.search_sales())
        self.btnDelete.clicked.connect(lambda: self.delete_record())
        self.search.textChanged.connect(lambda: self.search_sales())
        self.btnView.clicked.connect(lambda: self.get_today_sales())
        QtCore.QMetaObject.connectSlotsByName(Sales)

    def retranslateUi(self, Sales):
        _translate = QtCore.QCoreApplication.translate
        Sales.setWindowTitle(_translate("Sales", "All sales"))
        self.btnSearch.setText(_translate("Sales", "Search"))
        self.btnExit.setText(_translate("Sales", "Cancel"))
        self.btnDelete.setText(_translate("Sales", "Delete"))
        self.btnView.setText(_translate("Sales", "Today's Sales"))
        self.btnNewSale.setText(_translate("Sales", "New Sale"))
        self.label12.setText(_translate("Sales", "Total Sales:"))

    def update_view(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        q = QtSql.QSqlQuery()
        model.setTable("sales")
        completer = QtWidgets.QCompleter()
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        q.exec_("select customer_name, product_name from sales")
        m = QtSql.QSqlQueryModel()
        m.setQuery(q)
        completer.setModel(m)
        self.search.setCompleter(completer)
        self.lblTotal.setText(str(m.rowCount()))
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Product Name")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Quantity")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Amount Paid")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Date")
        model.select()
        self.saleView.setModel(model)
        self.saleView.horizontalHeader().setMinimumHeight(40)
        self.saleView.horizontalHeader().setDefaultSectionSize(180)
        self.saleView.setColumnHidden(0, True)
        self.saleView.setColumnHidden(6, True)
        self.saleView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.saleView.setShowGrid(True)
        self.saleView.show()
        modl = QtSql.QSqlQueryModel()
        qury = QtSql.QSqlQuery()
        qury.exec_("select distinct product_name from sales")
        modl.setQuery(qury)
        if modl.rowCount() > 0:
            self.btnDelete.setEnabled(True)
            self.selectSale.setEnabled(True)
            self.selectSale.setModel(modl)
        else:
            self.selectSale.setDisabled(True)
            self.btnDelete.setDisabled(True)

    def delete_record(self):
        if sql.connectDB():
            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete?"),
                                     QtWidgets.qApp.tr("\nAre you sure you want to delete invoice with id <b>" +
                                    self.selectSale.currentText() + "</b>?"),
                                     QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if confirm == QtWidgets.QMessageBox.Yes:
                product = self.selectSale.currentText()
                con = sqlite3.connect("ims.db")

                if con:
                    cursor = con.cursor()
                    cursor.execute("select * from sales where product_name = '" + product + "'")
                    row = cursor.fetchall()
                    if row:
                        query = QtSql.QSqlQuery()
                        query.prepare("delete from sales where product_name = ? and customer_name = ?")
                        print(row[0][0])
                        query.bindValue(0, product)
                        query.bindValue(1, str(row[0][1]))
                        if query.exec_():
                            self.update_view()
                            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Sale deleted!"),
                                                              QtWidgets.qApp.tr("\nSale has been deleted"),
                                                              QtWidgets.QMessageBox.Ok)
                        else:
                            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Sale not deleted!"),
                                                           QtWidgets.qApp.tr("\nSale couldn't be deleted"),
                                                       QtWidgets.QMessageBox.Ok)

    def search_sales(self):
        sql.connectDB()
        if not self.search.text() == '' or not self.search.text().isspace():
            qry = QtSql.QSqlQuery()
            # self.setWindowTitle("Search results for " + self.search.text())
            qry.prepare("select * from sales where customer_name LIKE '%{0}%' or product_name LIKE '%{0}%' or "
                        "quantity LIKE '%{0}%' or amount_paid LIKE '%{0}%' or date_bought LIKE '%{0}%'".format(
                str(self.search.text())))

            if qry.exec_():
                model = QtSql.QSqlQueryModel()
                model.setQuery(qry)
                self.lblTotal.setText(str(model.rowCount()))
                model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
                model.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
                model.setHeaderData(2, QtCore.Qt.Horizontal, "Product Name")
                model.setHeaderData(4, QtCore.Qt.Horizontal, "Quantity")
                model.setHeaderData(3, QtCore.Qt.Horizontal, "Amount Paid")
                model.setHeaderData(5, QtCore.Qt.Horizontal, "Date")
                self.saleView.setModel(model)
                self.saleView.horizontalHeader().setMinimumHeight(40)
                self.saleView.horizontalHeader().setDefaultSectionSize(180)
                self.saleView.setColumnHidden(0, True)
                self.saleView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.saleView.setShowGrid(True)
                self.saleView.show()

    def get_today_sales(self):
        sql.connectDB()
        today = strftime("%d/%m/%Y", gmtime())
        qry = QtSql.QSqlQuery()
        qry.prepare("select * from sales where date_bought = ?")
        qry.bindValue(0, str(today))
        if qry.exec_():
            model = QtSql.QSqlQueryModel()
            model.setQuery(qry)
            self.lblTotal.setText(str(model.rowCount()))
            model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            model.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
            model.setHeaderData(2, QtCore.Qt.Horizontal, "Product Name")
            model.setHeaderData(4, QtCore.Qt.Horizontal, "Quantity")
            model.setHeaderData(3, QtCore.Qt.Horizontal, "Amount Paid")
            model.setHeaderData(5, QtCore.Qt.Horizontal, "Date")
            self.saleView.setModel(model)
            self.saleView.horizontalHeader().setMinimumHeight(40)
            self.saleView.horizontalHeader().setDefaultSectionSize(180)
            self.saleView.setColumnHidden(0, True)
            self.saleView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            self.saleView.setShowGrid(True)
            self.saleView.show()

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sales = QtWidgets.QDialog()
    ui = Ui_Sales()
    ui.setupUi(Sales)
    Sales.show()
    sys.exit(app.exec_())

