# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invoices.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_Invoices(object):
    def setupUi(self, Invoices):
        Invoices.setObjectName("Invoices")
        Invoices.resize(932, 583)
        Invoices.setMaximumSize(QtCore.QSize(111024, 111024))
        self.gridLayout = QtWidgets.QGridLayout(Invoices)
        self.gridLayout.setObjectName("gridLayout")
        self.search = QtWidgets.QLineEdit(Invoices)
        self.search.setStyleSheet("min-width:220px;\n"
"padding:5px;")
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 0, 0, 1, 1)
        self.btnSearch = QtWidgets.QPushButton(Invoices)
        self.btnSearch.setStyleSheet("padding:5px 10px;\n"
"margin:5px;")
        self.btnSearch.setObjectName("btnSearch")
        self.gridLayout.addWidget(self.btnSearch, 0, 1, 1, 1)
        self.selectInvoice = QtWidgets.QComboBox(Invoices)
        self.selectInvoice.setStyleSheet("min-width:220px;\n"
"padding:5px;")
        self.selectInvoice.setObjectName("selectInvoice")
        self.gridLayout.addWidget(self.selectInvoice, 0, 2, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(Invoices)
        self.btnDelete.setStyleSheet("padding:5px 10px;\n"
"margin:5px;")
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout.addWidget(self.btnDelete, 0, 3, 1, 1)
        self.btnNewInvoice = QtWidgets.QPushButton(Invoices)
        self.btnNewInvoice.setStyleSheet("padding:5px;\n"
"margin:5px;")
        self.btnNewInvoice.setObjectName("btnNewInvoice")
        self.gridLayout.addWidget(self.btnNewInvoice, 0, 4, 1, 1)
        self.btnExit = QtWidgets.QPushButton(Invoices)
        self.btnExit.setStyleSheet("padding:5px 10px;\n"
"margin:5px;")
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 0, 6, 1, 1)
        self.invoiceView = QtWidgets.QTableView(Invoices)
        self.invoiceView.setObjectName("invoiceView")
        self.gridLayout.addWidget(self.invoiceView, 1, 0, 1, 7)

        self.retranslateUi(Invoices)
        self.btnExit.clicked.connect(Invoices.close)
        self.select_invoices()
        self.update_view()
        complet = QtWidgets.QCompleter()
        complet.setFilterMode(QtCore.Qt.MatchContains)
        complet.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        complet.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        qery = QtSql.QSqlQuery()
        qery.exec_("select distinct customer_name from invoices")
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(qery)
        self.search.setCompleter(complet)
        complet.setModel(modal)
        self.stylesheet()
        QtCore.QMetaObject.connectSlotsByName(Invoices)
        self.btnSearch.clicked.connect(lambda: self.search_invoices())
        self.search.textChanged.connect(lambda: self.search_invoices())
        self.btnDelete.clicked.connect(lambda: self.delete_record())

    def retranslateUi(self, Invoices):
        _translate = QtCore.QCoreApplication.translate
        Invoices.setWindowTitle(_translate("Invoices", "All invoices"))
        self.btnExit.setText(_translate("Invoices", "Cancel"))
        self.btnNewInvoice.setText(_translate("Invoices", "New Invoice"))
        self.btnSearch.setText(_translate("Invoices", "Search"))
        self.btnDelete.setText(_translate("Invoices", "Delete"))

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

    def update_view(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        q = QtSql.QSqlQuery()
        model.setTable("invoices")
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Invoice No.")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Product Code")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Product Name")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Sale Price")
        model.setHeaderData(7, QtCore.Qt.Horizontal, "Amount Paid")
        model.setHeaderData(8, QtCore.Qt.Horizontal, "Balance")
        model.setHeaderData(9, QtCore.Qt.Horizontal, "Quantity")
        model.setHeaderData(10, QtCore.Qt.Horizontal, "Total")
        model.setHeaderData(11, QtCore.Qt.Horizontal, "Date")
        model.select()
        self.invoiceView.setModel(model)
        self.invoiceView.horizontalHeader().setMinimumHeight(40)
        self.invoiceView.horizontalHeader().setDefaultSectionSize(180)
        self.invoiceView.setColumnHidden(0, True)
        self.invoiceView.setColumnHidden(6, True)
        self.invoiceView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.invoiceView.setShowGrid(True)
        self.invoiceView.show()
        modl = QtSql.QSqlQueryModel()
        qury = QtSql.QSqlQuery()
        qury.exec_("select distinct invoice_number from invoices")
        modl.setQuery(qury)
        if modl.rowCount() > 0:
            self.btnDelete.setEnabled(True)
            self.selectInvoice.setEnabled(True)
            self.selectInvoice.setModel(modl)
        else:
            self.selectInvoice.setDisabled(True)
            self.btnDelete.setDisabled(True)

    def select_invoices(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        q = QtSql.QSqlQuery()
        model.setTable("invoices")
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Invoice No.")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Product Code")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Product Name")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Sale Price")
        model.setHeaderData(7, QtCore.Qt.Horizontal, "Amount Paid")
        model.setHeaderData(8, QtCore.Qt.Horizontal, "Balance")
        model.setHeaderData(9, QtCore.Qt.Horizontal, "Quantity")
        model.setHeaderData(10, QtCore.Qt.Horizontal, "Total")
        model.setHeaderData(11, QtCore.Qt.Horizontal, "Date")
        model.select()
        self.invoiceView.setModel(model)
        self.invoiceView.horizontalHeader().setMinimumHeight(40)
        self.invoiceView.horizontalHeader().setDefaultSectionSize(180)
        self.invoiceView.setColumnHidden(0, True)
        self.invoiceView.setColumnHidden(6, True)
        self.invoiceView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.invoiceView.setShowGrid(True)
        self.invoiceView.show()


    def delete_record(self):
        if sql.connectDB():
            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete?"),
                                                     QtWidgets.qApp.tr("\nAre you sure you want to delete invoice with id <b>" +
                                                    self.selectInvoice.currentText() + "</b>?"),
                                                     QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if confirm == QtWidgets.QMessageBox.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("delete from invoices where invoice_number = ?")
                query.bindValue(0, self.selectInvoice.currentText())
                if query.exec_():
                    self.update_view()
                    self.select_invoices()
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Invoice deleted!"),
                                                      QtWidgets.qApp.tr("\nInvoice has been deleted"),
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Invoice not deleted!"),
                                                   QtWidgets.qApp.tr("\nInvoice couldn't be deleted"),
                                                   QtWidgets.QMessageBox.Ok)

    def search_invoices(self):
        if not self.search.text() == '' or not self.search.text().isspace():
            qry = QtSql.QSqlQuery()
            # self.setWindowTitle("Search results for " + self.search.text())
            qry.prepare("select * from invoices where product_code LIKE '%{0}%' or product_name LIKE '%{0}%' or "
                        "customer_name LIKE '%{0}%' or invoice_number LIKE '%{0}%' or date_bought LIKE '%{0}%'".format(
                str(self.search.text())))

            if qry.exec_():
                model = QtSql.QSqlQueryModel()
                model.setQuery(qry)
                model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
                model.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
                model.setHeaderData(2, QtCore.Qt.Horizontal, "Invoice No.")
                model.setHeaderData(3, QtCore.Qt.Horizontal, "Product Code")
                model.setHeaderData(4, QtCore.Qt.Horizontal, "Product Name")
                model.setHeaderData(5, QtCore.Qt.Horizontal, "Sale Price")
                model.setHeaderData(7, QtCore.Qt.Horizontal, "Amount Paid")
                model.setHeaderData(8, QtCore.Qt.Horizontal, "Balance")
                model.setHeaderData(9, QtCore.Qt.Horizontal, "Quantity")
                model.setHeaderData(10, QtCore.Qt.Horizontal, "Total")
                model.setHeaderData(11, QtCore.Qt.Horizontal, "Date")
                self.invoiceView.setModel(model)
                self.invoiceView.horizontalHeader().setMinimumHeight(40)
                self.invoiceView.horizontalHeader().setDefaultSectionSize(180)
                self.invoiceView.setColumnHidden(0, True)
                self.invoiceView.setColumnHidden(6, True)
                self.invoiceView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.invoiceView.setShowGrid(True)
                self.invoiceView.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Invoices = QtWidgets.QDialog()
    ui = Ui_Invoices()
    ui.setupUi(Invoices)
    Invoices.show()
    sys.exit(app.exec_())

