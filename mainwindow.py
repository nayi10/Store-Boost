# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtSql import QSqlQuery
from categories import *
import webbrowser
from registration import *
from products import *
from creditors import *
from about import *
from analysis import *
from users import *
from stock import *
from stock import *
from debtors import *
from formdebtors import *
from logs import *
from customerlist import *
from customer import *
from PyQt5.QtGui import QImage, QPainter, QIcon, QKeySequence, QIcon, QTextCursor, QCursor, QDropEvent, QTextDocument, \
    QTextTableFormat, QColor
from PyQt5.QtCore import QFile, QSettings, Qt, QFileInfo, QItemSelectionModel, QDir
from PyQt5.QtWidgets import (QMainWindow, QAction, QWidget, QLineEdit, QMessageBox, QAbstractItemView, QApplication,
                             QTableWidget, QTableWidgetItem, QGridLayout, QFileDialog, QMenu, QInputDialog)
from register import *
from supplier import *
from login import *
import sql
from formproduct import *
from functions import num_rows
from about import *
from contacts import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Welcome to Inventory Management System")
        MainWindow.resize(2024, 789)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 871, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tblStockList = QtWidgets.QTableView(self.centralWidget)
        self.tblStockList.setGeometry(QtCore.QRect(50, 60, 1140, 400))
        self.tblStockList.setMinimumSize(QtCore.QSize(700, 120))
        self.tblStockList.setStyleSheet("border:2px solid #dcdcdc;")
        self.tblStockList.setGridStyle(QtCore.Qt.SolidLine)
        self.tblStockList.setSortingEnabled(True)
        self.tblStockList.setObjectName("tblStockList")
        self.tblStockList.horizontalHeader().setHighlightSections(True)
        self.tblStockList.horizontalHeader().setMinimumSectionSize(140)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 2024, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy)
        self.menuBar.setStyleSheet("alternate-background-color: rgb(0, 170, 255);\n"
"selection-background-color: rgb(255, 85, 0);\n"
"selection-color: rgb(255, 255, 255);")
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setStyleSheet("")
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuExport = QtWidgets.QMenu(self.menuTools)
        self.menuExport.setObjectName("menuExport")
        self.menuImport = QtWidgets.QMenu(self.menuTools)
        self.menuImport.setObjectName("menuImport")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNewProduct = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/Product.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewProduct.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.actionNewProduct.setFont(font)
        self.actionNewProduct.setObjectName("actionNewProduct")
        self.actionNewCategory = QtWidgets.QAction(MainWindow)
        self.actionNewCategory.setObjectName("actionNewCategory")
        self.actionNewInvoice = QtWidgets.QAction(MainWindow)
        self.actionNewInvoice.setObjectName("actionNewInvoice")
        self.actionNewSupplierInfo = QtWidgets.QAction(MainWindow)
        self.actionNewSupplierInfo.setObjectName("actionNewSupplierInfo")
        self.actionNewSupplier = QtWidgets.QAction(MainWindow)
        self.actionNewSupplier.setObjectName("actionNewSupplier")
        self.actionNewContact = QtWidgets.QAction(MainWindow)
        self.actionNewContact.setObjectName("actionNewContact")
        self.actionNewCustomerInfo = QtWidgets.QAction(MainWindow)
        self.actionNewDebtor = QtWidgets.QAction(MainWindow)
        self.actionNewDebtor.setObjectName("actionNewDebtor")
        self.actionNewCreditor = QtWidgets.QAction(MainWindow)
        self.actionNewCreditor.setObjectName("actionNewCreditor")
        self.actionNewCustomerInfo = QtWidgets.QAction(MainWindow)
        self.actionNewCustomerInfo = QtWidgets.QAction(MainWindow)
        self.actionNewCustomerInfo.setObjectName("actionNewCustomerInfo")
        self.actionViewCreditors = QtWidgets.QAction(MainWindow)
        self.actionViewCreditors.setObjectName("actionViewCreditors")
        self.actionViewDebtors = QtWidgets.QAction(MainWindow)
        self.actionViewDebtors.setObjectName("actionViewDebtors")
        self.actionViewProductCategories = QtWidgets.QAction(MainWindow)
        self.actionViewProductCategories.setObjectName("actionViewProductCategories")
        self.actionViewInvoices = QtWidgets.QAction(MainWindow)
        self.actionViewInvoices.setObjectName("actionViewInvoices")
        self.actionViewCompanyInfo = QtWidgets.QAction(MainWindow)
        self.actionViewCompanyInfo.setObjectName("actionViewCompanyInfo")
        self.actionViewCustomers = QtWidgets.QAction(MainWindow)
        self.actionViewCustomers.setObjectName("actionViewCustomers")
        self.actionViewContacts = QtWidgets.QAction(MainWindow)
        self.actionViewContacts.setObjectName("actionViewContacts")
        self.actionViewAllProducts = QtWidgets.QAction(MainWindow)
        self.actionViewAllProducts.setObjectName("actionViewAllProducts")
        self.actionEditProducts = QtWidgets.QAction(MainWindow)
        self.actionEditProducts.setObjectName("actionEditProducts")
        self.actionEditCustomerInfo = QtWidgets.QAction(MainWindow)
        self.actionEditCustomerInfo.setObjectName("actionEditCustomerInfo")
        self.actionEditCompanyInfo = QtWidgets.QAction(MainWindow)
        self.actionEditCompanyInfo.setObjectName("actionEditCompanyInfo")
        self.actionEditContact = QtWidgets.QAction(MainWindow)
        self.actionEditContact.setObjectName("actionEditContact")
        self.actionEditCategories = QtWidgets.QAction(MainWindow)
        self.actionEditCategories.setObjectName("actionEditCategories")
        self.actionViewLogs = QtWidgets.QAction(MainWindow)
        self.actionViewLogs.setObjectName("actionViewLogs")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionProductSupport = QtWidgets.QAction(MainWindow)
        self.actionProductSupport.setObjectName("actionProductSupport")
        self.actionAboutIMS = QtWidgets.QAction(MainWindow)
        self.actionAboutIMS.setObjectName("actionAboutIMS")
        self.actionReportBugs = QtWidgets.QAction(MainWindow)
        self.actionReportBugs.setObjectName("actionReportBugs")
        self.actionBackupData = QtWidgets.QAction(MainWindow)
        self.actionBackupData.setObjectName("actionBackupData")
        self.actionExportExcel = QtWidgets.QAction(MainWindow)
        self.actionExportExcel.setObjectName("actionExportExcel")
        self.actionExportCSV = QtWidgets.QAction(MainWindow)
        self.actionExportCSV.setObjectName("actionExportCSV")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionImportExcelFile = QtWidgets.QAction(MainWindow)
        self.actionImportExcelFile.setObjectName("actionImportExcelFile")
        self.actionImportCSV = QtWidgets.QAction(MainWindow)
        self.actionImportCSV.setObjectName("actionImportCSV")
        self.actionImportODFSpreadsheet = QtWidgets.QAction(MainWindow)
        self.actionImportODFSpreadsheet.setObjectName("actionImportODFSpreadsheet")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNewStaff = QtWidgets.QAction(MainWindow)
        self.actionNewStaff.setObjectName("actionNewStaff")
        self.actionViewStaff = QtWidgets.QAction(MainWindow)
        self.actionViewStaff.setObjectName("actionViewStaff")
        self.actionViewStoreStatistics = QtWidgets.QAction(MainWindow)
        self.actionViewStoreStatistics.setObjectName("actionViewStoreStatistics")
        self.menuFile.addAction(self.actionNewProduct)
        self.menuFile.addAction(self.actionNewCategory)
        self.menuFile.addAction(self.actionNewInvoice)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNewSupplierInfo)
        self.menuFile.addAction(self.actionNewCustomerInfo)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNewContact)
        self.menuFile.addAction(self.actionNewDebtor)
        self.menuFile.addAction(self.actionNewCreditor)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNewStaff)
        self.menuFile.addAction(self.actionNewSupplier)
        self.menuView.addAction(self.actionViewCreditors)
        self.menuView.addAction(self.actionViewDebtors)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionViewProductCategories)
        self.menuView.addAction(self.actionViewAllProducts)
        self.menuView.addAction(self.actionViewInvoices)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionViewCompanyInfo)
        self.menuView.addAction(self.actionViewCustomers)
        self.menuView.addAction(self.actionViewContacts)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionViewStaff)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionViewLogs)
        self.menuView.addAction(self.actionViewStoreStatistics)
        self.menuEdit.addAction(self.actionEditProducts)
        self.menuEdit.addAction(self.actionEditCustomerInfo)
        self.menuEdit.addAction(self.actionEditCompanyInfo)
        self.menuEdit.addAction(self.actionEditContact)
        self.menuEdit.addAction(self.actionEditCategories)
        self.menuEdit.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionProductSupport)
        self.menuHelp.addAction(self.actionAboutIMS)
        self.menuHelp.addAction(self.actionReportBugs)
        self.menuExport.addAction(self.actionExportExcel)
        self.menuExport.addAction(self.actionExportCSV)
        self.menuImport.addAction(self.actionImportExcelFile)
        self.menuImport.addAction(self.actionImportCSV)
        self.menuImport.addAction(self.actionImportODFSpreadsheet)
        self.menuTools.addAction(self.actionBackupData)
        self.menuTools.addAction(self.menuExport.menuAction())
        self.menuTools.addAction(self.menuImport.menuAction())
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionPrint)
        self.menuTools.addSeparator()
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome to Inventory Management System"))
        self.label.setText(_translate("MainWindow", "Stock Lists"))
        self.menuFile.setTitle(_translate("MainWindow", "Create"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.actionNewProduct.setText(_translate("MainWindow", "New Product"))
        self.actionNewProduct.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionNewCategory.setText(_translate("MainWindow", "New Category"))
        self.actionNewCategory.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.actionNewInvoice.setText(_translate("MainWindow", "New Invoice"))
        self.actionNewInvoice.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionNewSupplierInfo.setText(_translate("MainWindow", "Supplier Info"))
        self.actionNewSupplierInfo.setShortcut(_translate("MainWindow", "Ctrl+Shift+I"))
        self.actionNewSupplier.setText(_translate("MainWindow", "New Supplier"))
        self.actionNewSupplier.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionNewContact.setText(_translate("MainWindow", "Contact"))
        self.actionNewContact.setShortcut(_translate("MainWindow", "Alt+N"))
        self.actionNewDebtor.setText(_translate("MainWindow", "Debtor"))
        self.actionNewDebtor.setShortcut(_translate("MainWindow", "Ctrl+Alt+D"))
        self.actionNewCreditor.setText(_translate("MainWindow", "Creditor"))
        self.actionNewCreditor.setShortcut(_translate("MainWindow", "Ctrl+Alt+C"))
        self.actionNewCustomerInfo.setText(_translate("MainWindow", "Customer Info"))
        self.actionNewCustomerInfo.setShortcut(_translate("MainWindow", "Ctrl+Alt+N"))
        self.actionViewCreditors.setText(_translate("MainWindow", "Creditors"))
        self.actionViewDebtors.setText(_translate("MainWindow", "Debtors"))
        self.actionViewProductCategories.setText(_translate("MainWindow", "Product Categories"))
        self.actionViewInvoices.setText(_translate("MainWindow", "Invoices"))
        self.actionViewCompanyInfo.setText(_translate("MainWindow", "Suppliers"))
        self.actionViewCustomers.setText(_translate("MainWindow", "Customers"))
        self.actionViewContacts.setText(_translate("MainWindow", "Contacts"))
        self.actionViewAllProducts.setText(_translate("MainWindow", "All Products"))
        self.actionEditProducts.setText(_translate("MainWindow", "Products"))
        self.actionEditCustomerInfo.setText(_translate("MainWindow", "Customer Info"))
        self.actionEditCompanyInfo.setText(_translate("MainWindow", "Company Info"))
        self.actionEditContact.setText(_translate("MainWindow", "Contact"))
        self.actionEditCategories.setText(_translate("MainWindow", "Categories"))
        self.actionViewLogs.setText(_translate("MainWindow", "Logs"))
        self.actionHelp.setText(_translate("MainWindow", "Help Content"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionProductSupport.setText(_translate("MainWindow", "Product Support"))
        self.actionProductSupport.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        self.actionAboutIMS.setText(_translate("MainWindow", "About IMS"))
        self.actionReportBugs.setText(_translate("MainWindow", "Report Bugs"))
        self.actionBackupData.setText(_translate("MainWindow", "Backup Data"))
        self.actionExportExcel.setText(_translate("MainWindow", "Excel"))
        self.actionExportCSV.setText(_translate("MainWindow", "CSV"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionImportExcelFile.setText(_translate("MainWindow", "Excel File"))
        self.actionImportCSV.setText(_translate("MainWindow", "CSV File"))
        self.actionImportODFSpreadsheet.setText(_translate("MainWindow", "ODF Spreadsheet"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNewStaff.setText(_translate("MainWindow", "New Employee"))
        self.actionViewStaff.setText(_translate("MainWindow", "Staff"))
        self.actionViewStoreStatistics.setText(_translate("MainWindow", "Store Statistics"))

    def stylesheet(self):
        return """
            QPushButton:hover{
            background-color:#fff;
            color: blue;
            }

            QPushButton{
            background-color: #cdcdcd;
            }
            
            QTableView::row{
            padding:15px;
            }
        """

def main():
    if sql.connectDB():
        query = QSqlQuery()
        query.exec_("SELECT * from users")

        if num_rows(query) < 1:
            import sys
            signup = QtWidgets.QFrame()
            u_register = Ui_Register()
            u_register.setupUi(signup)
            typ = u_register.userType.currentText()
            status = u_register.status.currentText()

            def register_user():
                error = 0
                if u_register.name.text() == '' or u_register.name.text().isspace():
                    u_register.lblError.setText("Please enter name")
                    error = 1
                if u_register.username.text() == '' or u_register.username.text().isspace():
                    u_register.lblError.setText("Please enter username")
                    error = 2
                if u_register.password.text() == '' or u_register.password.text().isspace():
                    u_register.lblError.setText("Please enter password")
                    error = 3
                if u_register.email.text() == '' or u_register.email.text().isspace():
                    u_register.lblError.setText("Please enter email")
                    error = 4
                if u_register.phone.text() == '' or u_register.phone.text().isspace():
                    u_register.lblError.setText("Please enter phone number")
                    error = 5

                if (u_register.name.text() == '' or u_register.name.text().isspace()) and (u_register.username.text() == '' or
                                                                         u_register.username.text().isspace()) and (
                        u_register.email.text() == '' or u_register.email.text().isspace()) and (u_register.password.text() == '' or
                                                                               u_register.password.text().isspace()) and (
                        u_register.phone.text() == '' or u_register.phone.text().isspace()):
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Correct Errors!"),
                                                      QtWidgets.qApp.tr("Please enter all details "),
                                                      QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

                    u_register.lblError.setText("")

                if error == 0:
                    insert_data()

            def insert_data():
                query.prepare("INSERT INTO users(name,password,username,email,phone,user_type,status) "
                              "VALUES(?,?,?,?,?,?,?)")
                query.bindValue(0, u_register.name.text())
                query.bindValue(1, u_register.password.text())
                query.bindValue(2, u_register.username.text())
                query.bindValue(3, u_register.email.text())
                query.bindValue(4, u_register.phone.text())
                query.bindValue(5, typ)
                query.bindValue(6, status)
                if query.exec_():
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Successful"),
                                                      QtWidgets.qApp.tr("Your user details have been saved\n"
                                                                        "You can now login using your username and password"),
                                                      QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Not Successful"),
                                                      QtWidgets.qApp.tr("Registration could not be processed successfully"),
                                                      QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

            signup.setGeometry(450, 100, 750, 500)
            signup.setMaximumWidth(750)
            signup.setWindowTitle("Register now")
            signup.show()
            u_register.btnCancel.clicked.connect(quit)
            u_register.btnRegister.clicked.connect(register_user)

        else:
            import sys
            Login = QtWidgets.QFrame()
            ui_login = Ui_Login()
            ui_login.setupUi(Login)

            def validateForm():
                error = 0
                if (ui_login.username.text().isspace() or ui_login.username.text() == '') and (ui_login.password.text().isspace() or ui_login.password.text() == ''):
                    ui_login.lbl_error.setText("Please enter your username and password.\n")
                    error = 1
                else:
                    if ui_login.username.text().isspace() or ui_login.username.text() == '':
                        ui_login.lbl_error.setText("Please enter your username")
                        error = 2
                    else:
                        username = ui_login.username.text()

                    if ui_login.password.text().isspace() or ui_login.password.text() == '':
                        ui_login.lbl_error.setText("Please enter your password")
                        error = 3
                    else:
                        ui_login.lbl_error.clear()
                        password = ui_login.password.text()

                    if error == 0:
                        query = QtSql.QSqlQuery()
                        query.prepare("SELECT username, password from users where username = ? and password = ?")
                        query.bindValue(0, username)
                        query.bindValue(1, password)
                        query.exec_()
                        if num_rows(query) > 0:
                            Login.close()
                        else:
                            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not registered"),
                                QtWidgets.qApp.tr("There is no user with those details\n"
                                                  "Ensure you're registered before trying!\n"
                                                  "to login!" + str(num_rows(query))),
                                QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Close)

            Login.setGeometry(500,150,750,500)
            Login.setMaximumWidth(750)
            Login.setWindowTitle("Enter Your Details To Login")
            Login.show()
            ui_login.btn_cancel.clicked.connect(quit)
            ui_login.btn_login.clicked.connect(validateForm)
            sys.exit(app.exec_())


def newDebtor():
    def nok():
        if not ui_debt.validate():
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("There are blank fields"),
                                           QtWidgets.qApp.tr("\nPlease all fields are required!\n\n"
                                                             "Make sure you fill all fields"),
                                           QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)
        else:
            ui_debt.insert_data()

    FormDebtor = QtWidgets.QDialog(MainWindow)
    ui_debt = Ui_FormDebtors()
    ui_debt.setupUi(FormDebtor)
    FormDebtor.show()
    ui_debt.btnSave.clicked.connect(nok)
    ui_debt.btnCancel.clicked.connect(FormDebtor.close)


def newProduct():
    if __name__ == "__main__":
        sql.connectDB()
        FormProduct = QtWidgets.QDialog(MainWindow)
        FormProduct.setGeometry(440, 80, 458, 450)
        FormProduct.setStyleSheet("background-color:#f1f1f1;")
        query = QtSql.QSqlQuery()
        query.prepare("select distinct name from suppliers")
        query.exec_()
        modl = QtSql.QSqlQueryModel()
        modl.setQuery(query)
        query2 = QtSql.QSqlQuery()
        query2.prepare("select distinct name from categories")
        query2.exec_()
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(query2)
        ui_prod_form = Ui_FormProduct()
        ui_prod_form.setupUi(FormProduct)

        ui_prod_form.update_field()
        ui_prod_form.supplier.setModel(modl)
        ui_prod_form.category.setModel(modal)
        ui_prod_form.supplier.show()

        def dialog():

            def save():
                import sql
                if sql.connectDB():
                    query = QtSql.QSqlQuery()
                    if supplierName.text() == "" or supplierName.text().isspace():
                        QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not Saved!"),
                                                       QtWidgets.qApp.tr("Suppplier name is required!"),
                                                       QtWidgets.QMessageBox.Close)
                    else:
                        query.prepare("insert into suppliers(name) values(?)")
                        query.bindValue(0, str(supplierName.text()))
                        if query.exec_():
                            supplierName.setText("")
                            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Saved!"),
                                                              QtWidgets.qApp.tr("Supplier added successfully!"),
                                                              QtWidgets.QMessageBox.Close)
                            query.finish()

            Form = QtWidgets.QDialog(FormProduct)
            Form.setWindowTitle("Add new supplier")
            Form.setGeometry(430, 200, 490, 100)
            supplierName = QtWidgets.QLineEdit(Form)
            supplierName.setObjectName("supplierName")
            supplierName.setGeometry(120, 40, 200, 30)
            lblName = QtWidgets.QLabel(Form)
            lblName.setText("Supplier Name:")
            lblName.setGeometry(10, 40, 100, 30)
            btnSave = QtWidgets.QPushButton(Form)
            btnSave.setGeometry(330, 40, 80, 30)
            btnSave.setText("Save")
            btnCancel = QtWidgets.QPushButton(Form)
            btnCancel.setGeometry(415, 40, 80, 30)
            btnCancel.setText("Close")
            btnCancel.clicked.connect(Form.close)
            btnSave.clicked.connect(save)
            Form.show()

        def validate():
            error = 0
            if ui_prod_form.productName.text() == '' or ui_prod_form.productName.text().isspace():
                error = 1
            if ui_prod_form.productCode.text() == '' or ui_prod_form.productCode.text().isspace():
                error = 2
            if ui_prod_form.quantity.text() == '' or ui_prod_form.quantity.text().isspace():
                error = 3
            if ui_prod_form.realPrice.text() == '' or ui_prod_form.realPrice.text().isspace():
                error = 4
            if ui_prod_form.salePrice.text() == '' or ui_prod_form.salePrice.text().isspace():
                error = 5
            if ui_prod_form.total.text() == '' or ui_prod_form.total.text().isspace():
                error = 6
            if ui_prod_form.dateAdded.text() == '' or ui_prod_form.dateAdded.text().isspace():
                error = 7
            if ui_prod_form.supplier.currentText() == '' or ui_prod_form.supplier.currentText().isspace():
                error = 9
            if ui_prod_form.category.currentText() == '' or ui_prod_form.category.currentText().isspace():
                error = 12

            if (ui_prod_form.productName.text() == '' or ui_prod_form.productName.text().isspace()) and (ui_prod_form.productCode.text() == '' or
                                                                                     ui_prod_form.productCode.text().isspace()) and (
                    ui_prod_form.realPrice.text() == '' or ui_prod_form.realPrice.text().isspace()) and (
                    ui_prod_form.salePrice.text() == '' or ui_prod_form.salePrice.text().isspace()) and (ui_prod_form.dateAdded.text() == '' or
                                                                                     ui_prod_form.dateAdded.text().isspace()) and (
                    ui_prod_form.quantity.text() == '' or ui_prod_form.quantity.text().isspace()) and (
                    ui_prod_form.total.text() == '' or ui_prod_form.total.text().isspace()) and (ui_prod_form.supplier.currentText() == '' or
                    ui_prod_form.supplier.currentText().isspace()) and (ui_prod_form.category.currentText() == '' or
                                                                        ui_prod_form.category.currentText().isspace()):
                error = 8

            if error == 0:
                insert_data()
            else:
                QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("All fields required!"),
                                               QtWidgets.qApp.tr("\nPlease there are some empty fields. "
                                                                 "Make sure you fill them to continue."),
                                               QtWidgets.QMessageBox.Close)

        def quitMe():
            FormProduct.close()

        def insert_data():
            if sql.connectDB():
                query.prepare("INSERT INTO products(product_code,product_name,real_price,sale_price,total_price,"
                              "quantity,product_category,date_added,supplier) VALUES(?,?,?,?,?,?,?,?,?)")

                query.bindValue(0, ui_prod_form.productCode.text())
                query.bindValue(1, ui_prod_form.productName.text())
                query.bindValue(2, ui_prod_form.realPrice.text())
                query.bindValue(3, ui_prod_form.salePrice.text())
                query.bindValue(4, ui_prod_form.total.text())
                query.bindValue(5, ui_prod_form.quantity.text())
                query.bindValue(6, ui_prod_form.category.currentText())
                query.bindValue(7, ui_prod_form.dateAdded.text())
                query.bindValue(8, ui_prod_form.supplier.currentText())
                if query.exec_():
                    ui_prod_form.productName.setText("")
                    ui_prod_form.productCode.setText("")
                    ui_prod_form.quantity.setText("")
                    ui_prod_form.realPrice.setText("")
                    ui_prod_form.salePrice.setText("")
                    ui_prod_form.total.setText("")
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Save Successful"),
                                                      QtWidgets.qApp.tr("\nProduct information has been added!"),
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Successful"),
                                                      QtWidgets.qApp.tr("Data could not be saved successfully"),
                                                      QtWidgets.QMessageBox.Close)

        ui_prod_form.btnAddSupplier.clicked.connect(dialog)
        ui_prod_form.btnCancel.clicked.connect(quitMe)
        ui_prod_form.btnSave.clicked.connect(validate)
        FormProduct.show()


def newSupplier():
    Supplier = QtWidgets.QMainWindow(MainWindow)
    ui_supplier = Ui_Supplier()
    ui_supplier.setupUi(Supplier)
    sql.connectDB()
    qry = QtSql.QSqlQuery()
    qry.prepare("select distinct name from suppliers")
    qry.exec_()
    modal = QtSql.QSqlQueryModel()
    modal.setQuery(qry)
    ui_supplier.supplierName.setModel(modal)

    def validate_data(self):
        error = 0
        if ui_supplier.contact.text() == '' or ui_supplier.contact.text().isspace():
            error = 2
        if ui_supplier.city.text() == '' or ui_supplier.city.text().isspace():
            error = 3
        if ui_supplier.region.text() == '' or ui_supplier.region.text().isspace():
            error = 4
        if ui_supplier.fax.text() == '' or ui_supplier.fax.text().isspace():
            error = 5
        if ui_supplier.address.toPlainText() == '' or ui_supplier.address.toPlainText().isspace():
            error = 6
        if ui_supplier.postalAddress.text() == '' or ui_supplier.postalAddress.text().isspace():
            error = 7
        if ui_supplier.registrationNumber.text() == '' or ui_supplier.registrationNumber.text().isspace():
            error = 9
        if ui_supplier.email.text() == '' or ui_supplier.email.text().isspace():
            error = 10
        if ui_supplier.productsInStore.text() == '' or ui_supplier.productsInStore.text().isspace():
            error = 11

        if (ui_supplier.contact.text() == '' or ui_supplier.contact.text().isspace()) and (
                ui_supplier.region.text() == '' or ui_supplier.region.text().isspace()) and (
                ui_supplier.fax.text() == '' or ui_supplier.fax.text().isspace()) and (
                ui_supplier.postalAddress.text() == '' or ui_supplier.postalAddress.text().isspace()) and (
                ui_supplier.city.text() == '' or ui_supplier.city.text().isspace()) and (
                ui_supplier.address.toPlainText() == '' or ui_supplier.address.toPlainText().isspace()) and (
                ui_supplier.registrationNumber.text() == '' or ui_supplier.registrationNumber.text().isspace()) and (
                ui_supplier.email.text() == '' or ui_supplier.email.text().isspace()):
            error = 13

        if error == 0:
            insert_data()
        else:
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Fill required fields!"),
                                           QtWidgets.qApp.tr("\nPlease there are still some required empty fields.."),
                                           QtWidgets.QMessageBox.Close)

    def insert_data():
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO supplier_info(name,contact,city,region,fax,address,postal_zip,email,"
                          "registration_no,products_instore,remarks,date_added) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)")

            date_added = QtCore.QDate.currentDate().toString()
            query.bindValue(0, ui_supplier.supplierName.currentText())
            query.bindValue(1, ui_supplier.contact.text())
            query.bindValue(2, ui_supplier.city.text())
            query.bindValue(3, ui_supplier.region.text())
            query.bindValue(4, ui_supplier.fax.text())
            query.bindValue(5, ui_supplier.address.toPlainText())
            query.bindValue(6, ui_supplier.postalAddress.text())
            query.bindValue(7, ui_supplier.email.text())
            query.bindValue(8, ui_supplier.registrationNumber.text())
            query.bindValue(9, ui_supplier.productsInStore.text())
            query.bindValue(10, ui_supplier.remarks.toPlainText())
            query.bindValue(11, date_added)
            if query.exec_():
                ui_supplier.city.setText("")
                ui_supplier.address.setText("")
                ui_supplier.city.setText("")
                ui_supplier.region.setText("")
                ui_supplier.fax.setText("")
                ui_supplier.postalAddress.setText("")
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Saved Successfully"),
                                                  QtWidgets.qApp.tr("\nSupplier information has been added!"),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Successful"),
                                                  QtWidgets.qApp.tr("Data could not be saved successfully"),
                                                  QtWidgets.QMessageBox.Close)
    Supplier.setGeometry(300, 0, 621, 583)
    ui_supplier.btnSave.clicked.connect(validate_data)
    Supplier.show()


def newCustomer():
    NewCustomer = QtWidgets.QDialog(MainWindow)
    ui_customer = Ui_NewCustomer()
    ui_customer.setupUi(NewCustomer)

    def validate_data():
        error = 0
        if ui_customer.phone.text() == '' or ui_customer.phone.text().isspace():
            error = 1
        if ui_customer.city.text() == '' or ui_customer.city.text().isspace():
            error = 2
        if ui_customer.region.text() == '' or ui_customer.region.text().isspace():
            error = 3
        if ui_customer.customerName.text() == '' or ui_customer.customerName.text().isspace():
            error = 4
        if ui_customer.address.toPlainText() == '' or ui_customer.address.toPlainText().isspace():
            error = 5
        if ui_customer.gender.currentText() == '' or ui_customer.gender.currentText().isspace():
            error = 6
        if ui_customer.postalAddress.text() == '' or ui_customer.postalAddress.text().isspace():
            error = 7
        if ui_customer.email.text() == '' or ui_customer.email.text().isspace():
            error = 8

        if (ui_customer.phone.text() == '' or ui_customer.phone.text().isspace()) and (
                ui_customer.region.text() == '' or ui_customer.region.text().isspace()) and (
                ui_customer.customerName.text() == '' or ui_customer.customerName.text().isspace()) and (
                ui_customer.gender.currentText() == '' or ui_customer.gender.currentText().isspace()) and (
                ui_customer.city.text() == '' or ui_customer.city.text().isspace()) and (
                ui_customer.address.toPlainText() == '' or ui_customer.address.toPlainText().isspace()) and (
                ui_customer.postalAddress.text() == '' or ui_customer.postalAddress.text().isspace()) and (
                ui_customer.email.text() == '' or ui_customer.email.text().isspace()):
            error = 9

        if error == 0:
            insert_data()
        else:
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Fill required fields!"),
                                           QtWidgets.qApp.tr("\nPlease all fields are required"),
                                           QtWidgets.QMessageBox.Close)

    def insert_data():
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO customers(name,phone,city,region,gender,address,post_office,email,"
                          "date_registered,remarks) VALUES(?,?,?,?,?,?,?,?,?,?)")

            date_added = QtCore.QDate.currentDate().toString()
            query.bindValue(0, ui_customer.customerName.text())
            query.bindValue(1, ui_customer.phone.text())
            query.bindValue(2, ui_customer.city.text())
            query.bindValue(3, ui_customer.region.text())
            query.bindValue(4, ui_customer.gender.currentText())
            query.bindValue(5, ui_customer.address.toPlainText())
            query.bindValue(6, ui_customer.postalAddress.text())
            query.bindValue(7, ui_customer.email.text())
            query.bindValue(8, date_added)
            query.bindValue(9, ui_customer.remarks.toPlainText())
            if query.exec_():
                ui_customer.city.setText("")
                ui_customer.address.setText("")
                ui_customer.phone.setText("")
                ui_customer.region.setText("")
                ui_customer.customerName.setText("")
                ui_customer.email.setText("")
                ui_customer.postalAddress.setText("")
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Saved Successfully"),
                                                  QtWidgets.qApp.tr("\nCustomer information has been added!"),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Successful"),
                                                  QtWidgets.qApp.tr("Data could not be saved successfully" +
                                                                    query.lastError().text()),
                                                  QtWidgets.QMessageBox.Close)
    NewCustomer.setGeometry(360, 0, 544, 490)
    ui_customer.btnSave.clicked.connect(validate_data)
    NewCustomer.show()


def get_stats():
    if __name__ == "__main__":
        Analysis = QtWidgets.QDialog(MainWindow)
        ui = Ui_Analysis()
        ui.setupUi(Analysis)
        ui.lblDebtors.setText(str(get_total("debts")))
        ui.lblInStock.setText(str(get_greater_total("stock", "quantity", 0)))
        ui.lblOutStock.setText(str(get_lesser_total("stock", "quantity", 1)))
        ui.lblTotal.setText(str(get_total("products")))
        ui.lblCustomers.setText(str(get_total("customers")))
        ui.lblSuppliers.setText(str(get_total("suppliers")))
        ui.lblOutwards.setText(str(get_constraint_total("returns", "return_type", "outward")))
        ui.lblInwards.setText(str(get_constraint_total("returns", "return_type", "inward")))
        Analysis.setGeometry(130, 20, 1073, 612)
        Analysis.show()


def showAbout():
    if __name__ == "__main__":
        Help_Dialog = QtWidgets.QWidget(MainWindow)
        ui_about = Ui_Form()
        def quitMe():
            Help_Dialog.close()

        ui_about.setupUi(Help_Dialog)
        Help_Dialog.setWindowTitle("About IMS")
        Help_Dialog.setStyleSheet("background-color:#333;color:#fff;")
        Help_Dialog.setGeometry(450, 140, 400, 450)
        closeBtn = QtWidgets.QPushButton(Help_Dialog)
        closeBtn.setGeometry(385, 0, 15, 15)
        closeBtn.setStyleSheet("background-color:#333;color:ccc;")
        closeBtn.setText("X")
        closeBtn.show()
        closeBtn.clicked.connect(quitMe)
        Help_Dialog.show()


def showProducts():
    if __name__ == "__main__":
        frmProductsLists = QtWidgets.QDialog(MainWindow)
        frmProductsLists.setWindowTitle("Products")
        ui_products = Ui_frmProductsLists()
        ui_products.setupUi(frmProductsLists)
        ui_products.selectProducts()
        ui_products.tableView.setColumnHidden(0, True)
        frmProductsLists.setGeometry(40, 20, 1280, 650)
        frmProductsLists.show()



def dialogSupplier():
    Form = QtWidgets.QDialog(MainWindow)
    Form.setWindowTitle("Add new supplier")
    Form.setGeometry(420, 200, 510, 100)
    supplierName = QtWidgets.QLineEdit(Form)
    supplierName.setObjectName("supplierName")
    supplierName.setGeometry(120, 40, 200, 30)
    lblName = QtWidgets.QLabel(Form)
    lblName.setText("Supplier Name:")
    lblName.setGeometry(10, 40, 100, 30)

    def save():
        import sql
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            if supplierName.text() == "" or supplierName.text().isspace():
                QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not Saved!"),
                                                 QtWidgets.qApp.tr("Suppplier name is required!"),
                                                 QtWidgets.QMessageBox.Close)
            else:
                query.prepare("insert into suppliers(name) values(?)")
                query.bindValue(0, str(supplierName.text()))
                if query.exec_():
                    supplierName.setText("")
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Saved!"),
                                                      QtWidgets.qApp.tr("Supplier added successfully!"),
                                                  QtWidgets.QMessageBox.Close)


    btnSave = QtWidgets.QPushButton(Form)
    btnSave.setGeometry(330, 40, 80, 30)
    btnSave.setText("Save")
    btnCancel = QtWidgets.QPushButton(Form)
    btnCancel.setGeometry(415, 40, 80, 30)
    btnCancel.setText("Close")
    btnCancel.clicked.connect(Form.close)
    btnSave.clicked.connect(save)
    Form.show()


def showContacts():
    if __name__ == "__main__":
        Contacts = QtWidgets.QDialog(MainWindow)
        Contacts.setStyleSheet("background-color:#f0f0f0;")
        ui_contacts = Ui_Contacts()
        ui_contacts.setupUi(Contacts)
        ui_contacts.btnSave.clicked.connect(ui_contacts.saveNow)
        ui_contacts.btnClose.clicked.connect(Contacts.close)
        ui_contacts.showContacts()
        Contacts.setGeometry(340, 0, 637, 590)
        Contacts.show()

################################################################################################

def get_product():

    if searchbox.text() == '' or searchbox.text().isspace():
        QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Enter search query"), QtWidgets.qApp.tr(
            "Please enter search criterion to search!"), QtWidgets.QMessageBox.Ok)
    else:
        qry = QtSql.QSqlQuery()
        qry.prepare("select * from products where product_name LIKE '%{0}%' or product_code LIKE '%{0}%' or "
                    "product_category LIKE '%{0}%' or date_added LIKE '%{0}%' or supplier LIKE '%{0}%'".format(str(searchbox.text())))
        #qry.bindValue(0, str(searchbox.text()))
        if qry.exec_():
            my_model = QtSql.QSqlQueryModel()
            my_model.setQuery(qry)
            my_model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            my_model.setHeaderData(1, QtCore.Qt.Horizontal, "Product Code")
            my_model.setHeaderData(2, QtCore.Qt.Horizontal, "Product Name")
            my_model.setHeaderData(3, QtCore.Qt.Horizontal, "Product Price")
            my_model.setHeaderData(4, QtCore.Qt.Horizontal, "Sale Price")
            my_model.setHeaderData(5, QtCore.Qt.Horizontal, "Total Price")
            my_model.setHeaderData(6, QtCore.Qt.Horizontal, "Quantity")
            my_model.setHeaderData(7, QtCore.Qt.Horizontal, "Category")
            my_model.setHeaderData(8, QtCore.Qt.Horizontal, "Date Added")
            my_model.setHeaderData(9, QtCore.Qt.Horizontal, "Supplier")
            ui.tblStockList.setModel(my_model)
            print(my_model.rowCount())
            ui.tblStockList.show()



def show_suppliers():
    sql.connectDB()

    def search():
        if inputFilter.text() == '' or inputFilter.text().isspace():
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Enter search query"), QtWidgets.qApp.tr(
                "Please enter supplier name to search!"), QtWidgets.QMessageBox.Ok)
        else:
            qry = QtSql.QSqlQuery()
            qry.prepare("select name from suppliers where name LIKE '%{0}%'".format(str(inputFilter.text())))
            # qry.bindValue(0, str(inputFilter.text()))
            if qry.exec_():
                my_model = QtSql.QSqlQueryModel()
                my_model.setQuery(qry)
                list.setModel(my_model)
                list.show()

    my_query = QtSql.QSqlQuery()
    my_query.exec_("SELECT distinct name from suppliers")
    my_model = QtSql.QSqlQueryModel()
    my_model.setQuery(my_query)
    suppliers = QtWidgets.QDialog(MainWindow)
    suppliers.setWindowTitle("List of Suppliers")
    suppliers.setGeometry(340, 0, 650, 490)
    lblHead = QtWidgets.QLabel(suppliers)
    lblHead.setText("Ahasaniya Enterprice | Main Suppliers")
    lblHead.setStyleSheet("background-color:rgb(0,80,127);color:#fff;")
    font = QtGui.QFont()
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    lblHead.setFont(font)
    lblHead.setGeometry(QtCore.QRect(0, 0, 650, 38))
    lblHead.setAlignment(QtCore.Qt.AlignCenter)
    lblHead.show()
    inputFilter = QtWidgets.QLineEdit(suppliers)
    inputFilter.setGeometry(50, 45, 350, 30)
    inputFilter.setPlaceholderText("Search suppliers...")
    inputFilter.show()
    btnSearch = QtWidgets.QPushButton(suppliers)
    btnSearch.setGeometry(360, 45, 80, 30)
    btnSearch.setText("Search")
    btnSearch.clicked.connect(search)
    btnNew = QtWidgets.QPushButton(suppliers)
    btnNew.setGeometry(470, 45, 120, 30)
    btnNew.setText("+ New Supplier")
    list =  QtWidgets.QListView(suppliers)
    list.setGeometry(50, 85, 550, 360)
    font = QtGui.QFont()
    font.setPointSize(12)
    font.setWeight(45)
    list.setFont(font)
    list.setAlternatingRowColors(True)
    list.setStyleSheet(stylesheet())
    list.setModel(my_model)
    list.show()
    btnClose = QtWidgets.QPushButton(suppliers)
    btnClose.setGeometry(500, 450, 90, 35)
    btnClose.setText("Close")
    btnNew.clicked.connect(dialogSupplier)
    btnClose.clicked.connect(suppliers.close)
    suppliers.show()


def dialogContact():
    def save():
        import sql
        if sql.connectDB():
            query = QtSql.QSqlQuery()

            error = 0
            if contactName.text() == "" or contactName.text().isspace():
                error = 1

            if contactPhone.text() == "" or contactPhone.text().isspace():
                error = 2

            if error > 0:
                QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Error! All fields required!!"),
                                               QtWidgets.qApp.tr("Contact name and Phone are required!"),
                                               QtWidgets.QMessageBox.Close)

            else:
                day = QtCore.QDate.currentDate().toString()
                query.prepare("insert into contacts(contact_name, contact_phone, date_added) values(?,?,?)")
                query.bindValue(0, str(contactName.text()))
                query.bindValue(1, str(contactPhone.text()))
                query.bindValue(2, day)
                query.exec_()
                if query.numRowsAffected():
                    contactName.setText("")
                    contactPhone.setText("")
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Contact added!"),
                                                      QtWidgets.qApp.tr("Contact has been added!"),
                                                  QtWidgets.QMessageBox.Close)

    Contact = QtWidgets.QDialog(MainWindow)
    Contact.setWindowTitle("Add new contact")
    Contact.setGeometry(420, 200, 450, 180)
    contactName = QtWidgets.QLineEdit(Contact)
    contactName.setObjectName("contactName")
    contactName.setGeometry(130, 20, 200, 30)
    lblName = QtWidgets.QLabel(Contact)
    lblName.setText("Contact Name:")
    lblName.setGeometry(14, 20, 100, 30)
    contactPhone = QtWidgets.QLineEdit(Contact)
    contactPhone.setObjectName("contactPhone")
    contactPhone.setGeometry(130, 60, 200, 30)
    lblPhone = QtWidgets.QLabel(Contact)
    lblPhone.setText("Phone:")
    lblPhone.setGeometry(14, 60, 100, 30)
    btnSave = QtWidgets.QPushButton(Contact)
    btnSave.setGeometry(140, 120, 80, 30)
    btnSave.setText("Save")
    btnCancel = QtWidgets.QPushButton(Contact)
    btnCancel.setGeometry(230, 120, 80, 30)
    btnCancel.setText("Close")
    btnCancel.clicked.connect(Contact.close)
    btnSave.clicked.connect(save)
    Contact.show()


def showDebtors():
    Debtors = QtWidgets.QDialog(MainWindow)
    Debtors.setWindowTitle("Ahasaniya Enterprice | Debtors")
    ui_d = Ui_Debtors()
    ui_d.setupUi(Debtors)
    ui_d.debtorView.setColumnHidden(0, True)
    ui_d.display_debtors()
    ui_d.btnSearch.clicked.connect(lambda: ui_d.get_debtor())
    ui_d.btnNewDebtor.clicked.connect(newDebtor)
    ui_d.btnClose.clicked.connect(Debtors.close)
    Debtors.show()


def showCreditors():
    Creditors = QtWidgets.QDialog(MainWindow)
    ui = Ui_Creditors()
    ui.setupUi(Creditors)
    ui.creditorView.setColumnHidden(0, True)
    ui.display_creditors()
    ui.btnSearch.clicked.connect(lambda: ui.get_creditor())
    Creditors.show()


def dialogCategory():

    def save():
        import sql
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            if categoryName.text() == "" or categoryName.text().isspace():
                QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not Saved!"),
                                                 QtWidgets.qApp.tr("Category is required!"),
                                                 QtWidgets.QMessageBox.Close)
            else:
                query.prepare("insert into categories(name) values(?)")
                query.bindValue(0, categoryName.text())
                if query.exec_():
                    categoryName.setText("")
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Saved!"),
                                                      QtWidgets.qApp.tr("Product category has been added successfully!"),
                                                  QtWidgets.QMessageBox.Close)
                else:
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Saved!"),
                                                      QtWidgets.qApp.tr(
                                                          "Product category could not be added!" +
                                                      query.lastError().text()),
                                                      QtWidgets.QMessageBox.Close)

    FormCat = QtWidgets.QDialog(MainWindow)
    FormCat.setWindowTitle("Add new product category")
    FormCat.setGeometry(420, 200, 510, 100)
    categoryName = QtWidgets.QLineEdit(FormCat)
    categoryName.setObjectName("categoryName")
    categoryName.setGeometry(120, 40, 200, 30)
    lblName = QtWidgets.QLabel(FormCat)
    lblName.setText("Category:")
    lblName.setGeometry(10, 40, 100, 30)
    btnSave = QtWidgets.QPushButton(FormCat)
    btnSave.setGeometry(330, 40, 80, 30)
    btnSave.setText("Save")
    btnCancel = QtWidgets.QPushButton(FormCat)
    btnCancel.setGeometry(415, 40, 80, 30)
    btnCancel.setText("Close")
    btnCancel.clicked.connect(FormCat.close)
    btnSave.clicked.connect(save)
    FormCat.show()


def printPreview(obj):
    if obj.rowAt(0) == '':
        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("No enough rows!"),
                                          QtWidgets.qApp.tr("There are not enough rows to print!"),
                                          QtWidgets.QMessageBox.Ok)
    else:
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.setFixedSize(1000, 700)
        dialog.exec_()


def showCustomers():
    if __name__ == "__main__":
        CustomerLists = QtWidgets.QDialog(MainWindow)
        CustomerLists.setStyleSheet("background-color:#fff;")
        CustomerLists.setGeometry(120, 62, 1201, 760)
        ui_cust_list = Ui_Customers()
        ui_cust_list.setupUi(CustomerLists)
        ui_cust_list.selectCustomers()
        CustomerLists.show()

def showRegistration():
    if sql.connectDB():
        query = QtSql.QSqlQuery()
        w = QtWidgets.QDialog(MainWindow)
        ui_register = Ui_Registration()
        ui_register.setupUi(w)
        typ = ui_register.userType.currentText()
        status = ui_register.status.currentText()
        def add_user():
            error = 0
            if ui_register.name.text() == '' or ui_register.name.text().isspace():
                error = 1
            if ui_register.username.text() == '' or ui_register.username.text().isspace():
                error = 2
            if ui_register.password.text() == '' or ui_register.password.text().isspace():
                error = 3
            if ui_register.email.text() == '' or ui_register.email.text().isspace():
                error = 4
            if ui_register.phone.text() == '' or ui_register.phone.text().isspace():
                error = 5

            if (ui_register.name.text() == '' or ui_register.name.text().isspace()) and (ui_register.username.text() == '' or
                                                                     ui_register.username.text().isspace()) and (
                    ui_register.email.text() == '' or ui_register.email.text().isspace()) and (ui_register.password.text() == '' or
                                                                           ui_register.password.text().isspace()) and (
                    ui_register.phone.text() == '' or ui_register.phone.text().isspace()):
                error = 6

            if error == 0:
                insert_data()
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Correct Errors!"),
                                                  QtWidgets.qApp.tr("Please enter all details "),
                                                  QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

        def insert_data():
            query.prepare("INSERT INTO users(name,password,username,email,phone,user_type,status) "
                          "VALUES(?,?,?,?,?,?,?)")
            query.bindValue(0, ui_register.name.text())
            query.bindValue(1, ui_register.password.text())
            query.bindValue(2, ui_register.username.text())
            query.bindValue(3, ui_register.email.text())
            query.bindValue(4, ui_register.phone.text())
            query.bindValue(5, typ)
            query.bindValue(6, status)
            if query.exec_():
                ui_register.phone.setText("")
                ui_register.password.setText("")
                ui_register.name.setText("")
                ui_register.email.setText("")
                ui_register.username.setText("")
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Successful"),
                                                  QtWidgets.qApp.tr("The user's details have been saved\n"),
                                                  QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Registration Not Successful"),
                                                  QtWidgets.qApp.tr("The user could not be registered successfully"),
                                                  QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

        w.setGeometry(450, 100, 431, 398)
        w.setMaximumWidth(750)
        w.setWindowTitle("Register now")
        ui_register.btnRegister.setStyleSheet("background-color:#768355;color:#fff;")
        ui_register.btnCancel.clicked.connect(w.close)
        ui_register.btnRegister.clicked.connect(add_user)
        w.show()

def showCat():
    if __name__ == "__main__":
        frmCategory = QtWidgets.QDialog(MainWindow)
        frmCategory.setGeometry(260, 90, 400, 500)
        frmCategory.setFixedWidth(900)
        frmCategory.setWindowTitle("Product Categories")
        ui_category = Ui_Category()
        ui_category.setupUi(frmCategory)
        sql.connectDB()

        def saveCategory():
            import sql
            if sql.connectDB():
                query = QtSql.QSqlQuery()
                if ui_category.categoryName.text() == "" or ui_category.categoryName.text().isspace():
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not Saved!"),
                                                   QtWidgets.qApp.tr("Category is required!"),
                                                   QtWidgets.QMessageBox.Close)
                else:
                    query.prepare("insert into categories(name) values(?)")
                    query.bindValue(0, ui_category.categoryName.text())
                    if query.exec_():
                        ui_category.categoryName.setText("")
                        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Saved!"),
                                                          QtWidgets.qApp.tr(
                                                              "Product category has been added successfully!"),
                                                          QtWidgets.QMessageBox.Close)
                    else:
                        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Saved!"),
                                                          QtWidgets.qApp.tr(
                                                              "Product category could not be added!" +
                                                              query.lastError().text()),
                                                          QtWidgets.QMessageBox.Close)

        qry = QtSql.QSqlQuery()
        qry.exec_("select distinct name from categories")
        model = QtSql.QSqlQueryModel()
        model.setQuery(qry)
        ui_category.categoryView.setModel(model)
        ui_category.categoryView.show()
        ui_category.btnSave.clicked.connect(saveCategory)
        ui_category.btnFilter.clicked.connect(ui_category.get_category)
        ui_category.categoryView.setStyleSheet(stylesheet())
        frmCategory.show()


def mainLoop():
    Logs = QtWidgets.QDialog(MainWindow)
    ui_logs = Ui_Logs()
    ui_logs.setupUi(Logs)

    def getState():
        if ui_logs.selectAll.checkState() >= 1:
            ui_logs.selectAll.stateChanged['int'].connect(ui_logs.logsView.selectAll())
        else:
            ui_logs.logsView.clearSelection()

    ui_logs.get_logs()
    ui_logs.logsView.setColumnHidden(0, True)
    ui_logs.logsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    ui_logs.selectAll.clicked.connect(getState)
    ui_logs.btnGetData.clicked.connect(ui_logs.get_data)
    ui_logs.btnReset.clicked.connect(ui_logs.clearList)
    ui_logs.btnDeleteAll.clicked.connect(ui_logs.delete_all)
    Logs.setGeometry(320, 50, 720, 600)
    Logs.show()

def showUsers():
    sql.connectDB()
    Users = QtWidgets.QDialog(MainWindow)
    ui_users = Ui_Users()
    ui_users.setupUi(Users)

    def search():
        if ui_users.search_users.text() == '' or ui_users.search_users.text().isspace():
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Enter search query"), QtWidgets.qApp.tr(
                "Please enter criterion to search!"), QtWidgets.QMessageBox.Ok)
        else:
            qry = QtSql.QSqlQuery()
            qry.prepare("select * from users where name LIKE '%{0}%' or username LIKE '%{0}%' or id LIKE '%{0}%'"
                        "or email LIKE '%{0}%' or phone LIKE '%{0}%'".format(str(ui_users.search_users.text())))
            # qry.bindValue(0, str(inputFilter.text()))
            if qry.exec_():
                my_model = QtSql.QSqlQueryModel()
                my_model.setQuery(qry)
                ui_users.widgetUsers.setModel(my_model)
                my_model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
                my_model.setHeaderData(1, QtCore.Qt.Horizontal, "Full Name")
                my_model.setHeaderData(2, QtCore.Qt.Horizontal, "Password")
                my_model.setHeaderData(4, QtCore.Qt.Horizontal, "Email")
                my_model.setHeaderData(5, QtCore.Qt.Horizontal, "Phone")
                my_model.setHeaderData(3, QtCore.Qt.Horizontal, "Username")
                my_model.setHeaderData(6, QtCore.Qt.Horizontal, "Type")
                my_model.setHeaderData(7, QtCore.Qt.Horizontal, "Status")
                ui_users.widgetUsers.show()

    ui_users.checkUser()
    ui_users.widgetUsers.showMaximized()
    ui_users.widgetUsers.setColumnHidden(0, True)
    ui_users.widgetUsers.setColumnHidden(2, True)
    ui_users.widgetUsers.horizontalHeader().setMinimumHeight(40)
    ui_users.widgetUsers.horizontalHeader().setDefaultSectionSize(120)
    ui_users.widgetUsers.horizontalHeader().setMinimumSectionSize(100)
    ui_users.widgetUsers.horizontalHeader().setSortIndicatorShown(True)
    ui_users.widgetUsers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    ui_users.widgetUsers.horizontalHeader().setStyleSheet("background-color:#222;color:#dadada;")
    ui_users.pushButton.clicked.connect(search)
    Users.show()


def help_window():
    window = QtWidgets.QDialog(MainWindow)
    window.setGeometry(450, 150, 450, 180)
    window.setWindowTitle("Permission required")
    window.setStyleSheet("background-color:#dfdfdf;")
    label = QtWidgets.QLabel(window)
    label.setGeometry(10, 15, 440, 80)
    label.setText("Get help about IMS online at the  Bandughana IMS website.\n\n"
                  "Click Open Link in Browser to navigate to the website using \nyour default browser")
    font = QtGui.QFont()
    font.setPixelSize(15)
    font.setBold(True)
    label.setFont(font)
    label.show()

    def openLink():
        link = "https://software.bandughana.com/ims"
        webbrowser.open_new(link)
        window.close()

    btnGo = QtWidgets.QPushButton(window)
    btnGo.setGeometry(130, 130, 180, 35)
    btnGo.setText("Open Link in Browser")
    btnGo.show()
    btnGo.clicked.connect(openLink)
    window.show()


def open_support():
    link = "https://software.bandughana.com/ims/support/"
    webbrowser.open_new(link)

def report_bugs():
    link = "https://software.bandughana.com/bugs?r_s=ims"
    webbrowser.open_new(link)

def stylesheet():
    return """     
        QListView::item {
            padding: 10px 20px;
        }
    """

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("Welcome to Bandughana IMS")
    MainWindow.showMaximized()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setStyleSheet(ui.stylesheet())
    sql.connectDB()
    from PyQt5 import QtSql as qs
    model = qs.QSqlTableModel()
    model = QtSql.QSqlTableModel()
    model.setTable("products")
    w = MainWindow.width()
    h = MainWindow.height()
    model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "Product Code")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Product Name")
    model.setHeaderData(3, QtCore.Qt.Horizontal, "Product Price")
    model.setHeaderData(4, QtCore.Qt.Horizontal, "Sale Price")
    model.setHeaderData(5, QtCore.Qt.Horizontal, "Total Price")
    model.setHeaderData(6, QtCore.Qt.Horizontal, "Quantity")
    model.setHeaderData(7, QtCore.Qt.Horizontal, "Category")
    model.setHeaderData(8, QtCore.Qt.Horizontal, "Date Added")
    model.setHeaderData(9, QtCore.Qt.Horizontal, "Supplier")
    model.select()
    ui.tblStockList.setGeometry(25, 60, ((65/100) * w), (70/100) * h)
    lblAct = QtWidgets.QLabel(MainWindow)
    lblAct.setGeometry(25, 15 + (80/100) * h, 100, 30)
    lblAct.setText("With selected:")
    lblAct.show()
    btnDel = QtWidgets.QPushButton(MainWindow)
    btnDel.setGeometry(130, 15 + (80/100) * h, 80, 30)
    btnDel.setText("Delete")
    btnDel.show()
    btnEdit = QtWidgets.QPushButton(MainWindow)
    btnEdit.setGeometry(220, 15 + (80/100) * h, 50, 30)
    btnEdit.setText("Edit")
    btnEdit.show()
    searchbox = QtWidgets.QLineEdit(MainWindow)
    searchbox.setGeometry((20/100) * w, 15 + (80/100) * h, (20/100) * w, 30)
    searchbox.show()
    btnSearch = QtWidgets.QPushButton(MainWindow)
    btnSearch.setGeometry(40/100 * w, 15 + (80/100) * h, 80, 30)
    btnSearch.setText("Search")
    btnSearch.show()
    ui.tblStockList.setModel(model)
    ui.tblStockList.horizontalHeader().setMinimumHeight(50)
    ui.tblStockList.horizontalHeader().setStyleSheet("background-color:#111;color:#dadada")
    ui.tblStockList.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    ui.tblStockList.horizontalHeader().setDefaultSectionSize(145)
    ui.tblStockList.setMinimumHeight(40)
    ui.tblStockList.setStyleSheet(ui.stylesheet())
    ui.tblStockList.setAlternatingRowColors(True)
    ui.tblStockList.setColumnHidden(0, True)
    ui.tblStockList.setShowGrid(True)
    ui.tblStockList.show()
    toolBar = QtWidgets.QToolBar(MainWindow)
    toolBar.setFloatable(False)
    toolBar.setStyleSheet("background-color:#a03;color:#dcdcdc;padding-top:15px;padding-bottom:15px;margin-right:3px")
    toolBar.setGeometry(0, 25, 2018, 40)
    viewProduct = QtWidgets.QAction(toolBar)
    viewProduct.setObjectName("viewProducts")
    viewProduct.setText("Products")
    toolBar.addAction(viewProduct)
    viewSuppliers = QtWidgets.QAction(toolBar)
    viewSuppliers.setObjectName("viewSuppliers")
    viewSuppliers.setText("Suppliers")
    toolBar.addAction(viewSuppliers)
    viewCustomers = QtWidgets.QAction(toolBar)
    viewCustomers.setObjectName("viewCustomers")
    viewCustomers.setText("Customers")
    toolBar.addAction(viewCustomers)
    viewDebtors = QtWidgets.QAction(toolBar)
    viewDebtors.setObjectName("viewDebtors")
    viewDebtors.setText("Debtors")
    toolBar.addAction(viewDebtors)
    viewReturns = QtWidgets.QAction(toolBar)
    viewReturns.setObjectName("viewReturns")
    viewReturns.setText("Returns")
    toolBar.addAction(viewReturns)
    viewCategories = QtWidgets.QAction(toolBar)
    viewCategories.setObjectName("viewCategories")
    viewCategories.setText("Categories")
    toolBar.addAction(viewCategories)
    viewCreditors = QtWidgets.QAction(toolBar)
    viewCreditors.setObjectName("viewCreditors")
    viewCreditors.setText("Creditors")
    toolBar.addAction(viewCreditors)
    newInvoice = QtWidgets.QAction(toolBar)
    newInvoice.setObjectName("newInvoice")
    newInvoice.setText("New Invoice")
    viewCustomers.triggered.connect(lambda: showCustomers())
    ui.actionNewCategory.triggered.connect(lambda: dialogCategory())
    ui.actionViewCustomers.triggered.connect(lambda: showCustomers())
    ui.actionViewAllProducts.triggered.connect(lambda: showProducts())
    viewProduct.triggered.connect(lambda: showProducts())
    toolBar.show()
    ui.actionNewProduct.triggered.connect(lambda: newProduct())
    ui.actionViewProductCategories.triggered.connect(lambda: showCat())
    ui.actionPrint.triggered.connect(lambda: printPreview(ui.tblStockList))
    ui.actionNewSupplier.triggered.connect(lambda: dialogSupplier())
    ui.actionNewStaff.triggered.connect(lambda: showRegistration())
    ui.actionAboutIMS.triggered.connect(lambda: showAbout())
    ui.actionViewLogs.triggered.connect(lambda: mainLoop())
    ui.actionNewSupplierInfo.triggered.connect(lambda: newSupplier())
    ui.actionViewStoreStatistics.triggered.connect(lambda: get_stats())
    ui.actionExit.triggered.connect(quit)
    ui.actionViewCreditors.triggered.connect(lambda: showCreditors())
    ui.actionViewDebtors.triggered.connect(lambda: showDebtors())
    ui.actionNewDebtor.triggered.connect(lambda: newDebtor())
    btnSearch.clicked.connect(get_product)
    viewDebtors.triggered.connect(lambda: showDebtors())
    viewCreditors.triggered.connect(lambda: showCreditors())
    viewSuppliers.triggered.connect(lambda: show_suppliers())
    ui.actionNewContact.triggered.connect(lambda: dialogContact())
    viewCategories.triggered.connect(lambda: showCat())
    ui.actionViewStaff.triggered.connect(lambda: showUsers())
    ui.actionEditContact.triggered.connect(lambda: showContacts())
    ui.actionViewCompanyInfo.triggered.connect(lambda: show_suppliers())
    ui.actionNewCustomerInfo.triggered.connect(lambda: newCustomer())
    ui.actionViewContacts.triggered.connect(lambda: showContacts())
    ui.actionProductSupport.triggered.connect(lambda: open_support())
    ui.actionHelp.triggered.connect(lambda: help_window())
    ui.actionReportBugs.triggered.connect(lambda: report_bugs())
    ui.actionEditCategories.triggered.connect(lambda: showCat())
    MainWindow.show()
    main()
    sys.exit(app.exec_())