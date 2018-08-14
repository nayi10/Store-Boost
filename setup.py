# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtSql import QSqlQuery
from categories import *
import webbrowser
from session import *
from sales import *
from viewsales import *
import os
from newinvoice import *
from invoice import *
from returns import *
from editcutomer import *
from formcreditor import *
from invoices import *
from registration import *
from datetime import datetime
from products import *
from creditors import *
from editproduct import *
from suppliers import *
from editdebtors import *
from editcreditors import *
from about import *
from analysis import *
from shutil import copy2
from users import *
from stock import *
from debtors import *
from formdebtors import *
from logs import *
from customers import *
from customer import *
from register import *
from supplier import *
from login import *
import sql
from formproduct import *
from functions import *
from about import *
from contacts import *
import sqlite3
from stocklist import *
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 713)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        style = self.stylesheet()
        MainWindow.setStyleSheet(style)
        self.stylesheet()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setFloatable(False)
        self.toolBar.setStyleSheet("background-color:#03a;color:#dcdcdc;padding-top:15px;padding-bottom:15px;margin-right:3px")
        # self.toolBar.setGeometry(0, 25, 2018, 40)
        self.gridLayout.addWidget(self.toolBar)
        self.viewProduct = QtWidgets.QAction(self.toolBar)
        self.viewProduct.setObjectName("viewProducts")
        self.viewProduct.setText("Products")
        self.toolBar.addAction(self.viewProduct)
        self.viewSuppliers = QtWidgets.QAction(self.toolBar)
        self.viewSuppliers.setObjectName("viewSuppliers")
        self.viewSuppliers.setText("Suppliers")
        self.toolBar.addAction(self.viewSuppliers)
        self.viewCustomers = QtWidgets.QAction(self.toolBar)
        self.viewCustomers.setObjectName("viewCustomers")
        self.viewCustomers.setText("Customers")
        self.toolBar.addAction(self.viewCustomers)
        self.viewDebtors = QtWidgets.QAction(self.toolBar)
        self.viewDebtors.setObjectName("viewDebtors")
        self.viewDebtors.setText("Debtors")
        self.toolBar.addAction(self.viewDebtors)
        self.viewReturns = QtWidgets.QAction(self.toolBar)
        self.viewReturns.setObjectName("viewReturns")
        self.viewReturns.setText("Returns")
        self.toolBar.addAction(self.viewReturns)
        self.viewCategories = QtWidgets.QAction(self.toolBar)
        self.viewCategories.setObjectName("viewCategories")
        self.viewCategories.setText("Categories")
        self.toolBar.addAction(self.viewCategories)
        self.viewCreditors = QtWidgets.QAction(self.toolBar)
        self.viewCreditors.setObjectName("viewCreditors")
        self.viewCreditors.setText("Creditors")
        self.toolBar.addAction(self.viewCreditors)
        self.newInvoice = QtWidgets.QAction(self.toolBar)
        self.newInvoice.setObjectName("newInvoice")
        self.newInvoice.setText("New Invoice")
        self.toolBar.addAction(self.newInvoice)
        self.viewSale = QtWidgets.QAction(self.toolBar)
        self.viewSale.setObjectName("viewSale")
        self.viewSale.setText("Sales")
        self.toolBar.addAction(self.viewSale)
        self.newSale = QtWidgets.QAction(self.toolBar)
        self.newSale.setObjectName("newSale")
        self.newSale.setText("New Sale")
        self.toolBar.addAction(self.newSale)
        self.viewSupplierInfo = QtWidgets.QAction(self.toolBar)
        self.viewSupplierInfo.setObjectName("viewSupplierInfo")
        self.viewSupplierInfo.setText("Supplier Information")
        self.toolBar.addAction(self.viewSupplierInfo)
        self.quickDelete = QtWidgets.QAction(self.toolBar)
        self.quickDelete.setText("Quick Delete")
        self.toolBar.addAction(self.quickDelete)
        self.new_stock = QtWidgets.QAction(self.toolBar)
        self.new_stock.setText("Update Stock")
        self.toolBar.addAction(self.new_stock)
        self.tblStockList = QtWidgets.QTableView(self.centralWidget)
        self.tblStockList.setMinimumSize(QtCore.QSize(700, 120))
        self.tblStockList.setStyleSheet("border:2px solid #dcdcdc;")
        self.tblStockList.setGridStyle(QtCore.Qt.SolidLine)
        self.tblStockList.setSortingEnabled(True)
        self.tblStockList.setObjectName("tblStockList")
        self.tblStockList.horizontalHeader().setHighlightSections(True)
        self.tblStockList.horizontalHeader().setMinimumSectionSize(140)
        self.gridLayout.addWidget(self.tblStockList, 1, 0, 1, 1)
        self.spacerItem = QtWidgets.QSpacerItem(120, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.toolBar.addSeparator()
        self.lbl = QtWidgets.QLabel(self.toolBar)
        self.lbl.setFixedWidth(0.4 * self.toolBar.width())
        self.toolBar.addWidget(self.lbl)
        self.toolBar.addSeparator()
        self.user = QtWidgets.QLabel(self.toolBar)
        self.user.setObjectName("user")
        self.user.setGeometry(0.9 * self.toolBar.width(), 0.2 * self.toolBar.height(), 250, 45)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPixelSize(16)
        self.user.setFont(font)
        self.toolBar.addWidget(self.user)
        self.toolBar.addSeparator()
        self.logout = QtWidgets.QAction(self.toolBar)
        self.logout.setObjectName("logout")
        self.logout.setFont(font)
        self.toolBar.addAction(self.logout)
        MainWindow.setCentralWidget(self.centralWidget)

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
        icon.addPixmap(QtGui.QPixmap(resource_path("src/Product.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.actionViewSales = QtWidgets.QAction(MainWindow)
        self.actionViewSales.setObjectName("actionViewSales")
        self.actionViewStockOut = QtWidgets.QAction(MainWindow)
        self.actionViewStockOut.setObjectName("actionViewStockOut")
        self.actionViewAllProducts = QtWidgets.QAction(MainWindow)
        self.actionViewAllProducts.setObjectName("actionViewAllProducts")
        self.actionEditProducts = QtWidgets.QAction(MainWindow)
        self.actionEditProducts.setObjectName("actionEditProducts")
        self.actionEditCustomerInfo = QtWidgets.QAction(MainWindow)
        self.actionEditCustomerInfo.setObjectName("actionEditCustomerInfo")
        self.actionEditSupplierInfo = QtWidgets.QAction(MainWindow)
        self.actionEditSupplierInfo.setObjectName("actionEditCompanyInfo")
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
        self.actionImportDB = QtWidgets.QAction(MainWindow)
        self.actionImportDB.setObjectName("actionImportDB")
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
        self.menuView.addAction(self.actionViewSales)
        self.menuView.addAction(self.actionViewStockOut)
        self.menuView.addAction(self.actionViewStoreStatistics)
        self.menuEdit.addAction(self.actionEditProducts)
        self.menuEdit.addAction(self.actionEditCustomerInfo)
        self.menuEdit.addAction(self.actionEditSupplierInfo)
        self.menuEdit.addAction(self.actionEditContact)
        self.menuEdit.addAction(self.actionEditCategories)
        self.menuEdit.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionProductSupport)
        self.menuHelp.addAction(self.actionAboutIMS)
        self.menuHelp.addAction(self.actionReportBugs)
        self.menuImport.addAction(self.actionImportDB)
        self.menuTools.addAction(self.actionBackupData)
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
        self.update_table()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IMS for Ahasaniya Enterprice"))
        self.menuFile.setTitle(_translate("MainWindow", "Create"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
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
        self.actionViewSales.setText(_translate("MainWindow", "Sales"))
        self.actionViewContacts.setText(_translate("MainWindow", "Contacts"))
        self.actionViewAllProducts.setText(_translate("MainWindow", "All Products"))
        self.actionEditProducts.setText(_translate("MainWindow", "Products"))
        self.actionEditCustomerInfo.setText(_translate("MainWindow", "Customer Info"))
        self.actionEditSupplierInfo.setText(_translate("MainWindow", "Supplier Info"))
        self.actionEditContact.setText(_translate("MainWindow", "Contact"))
        self.actionEditCategories.setText(_translate("MainWindow", "Categories"))
        self.actionViewLogs.setText(_translate("MainWindow", "Logs"))
        self.actionViewStockOut.setText(_translate("MainWindow", "Out-of-Stock Products"))
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
        self.actionImportDB.setText(_translate("MainWindow", "Backed up data"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNewStaff.setText(_translate("MainWindow", "New Employee"))
        self.logout.setText(_translate("MainWindow", "Logout"))
        self.user.setText(_translate("MainWindow", ""))
        self.actionViewStaff.setText(_translate("MainWindow", "Staff"))
        self.actionViewStoreStatistics.setText(_translate("MainWindow", "Store Statistics"))

    def get_current_user(self):
        return self.user.text()

    def is_empty(self, item):
        self.item = item
        if self.item.text() == "" or self.item.currentText() == '' or self.item.toPlainText() == "":
            return True
        return False

    def contains_num(self, lists):
        item = [0,1,2,3,4,5,6,7,8,9]
        for lis in lists:
            for i in item:
                if lis.find(str(i)):
                    return True
        return False

    def stylesheet(self):
        return """
       
            * {
                font-size:16px;
            }
            QListView::item {
                padding: 10px 20px;
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

    def printItem(self, w, item):
        self.item = item
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, w)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.item.print_(printer)

    def import_backup(self, MainWindow):
        self.widget = QtWidgets.QWidget()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.widget.setWindowIcon(icon)
        self.left = 250
        self.top = 20
        self.width = 640
        self.height = 480
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self.widget, "Import previous backup", "",
                                                  "Database Files (*.db)", options=options)
        if file:
            dst = os.getcwd()
            if copy2(file, dst):
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Database import successful"), QtWidgets.qApp.tr(
                    "Data has been imported successfully"), QtWidgets.QMessageBox.Ok)

    def backup(self, MainWindow):
        self.widget = QtWidgets.QWidget()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.widget.setWindowIcon(icon)
        self.left = 200
        self.top = 20
        self.width = 640
        self.height = 480
        self.widget.setGeometry(self.left, self.top, self.width, self.height)
        backup_file = "ims.db"
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self.widget, "Choose folder for backup data", "",
                                                  "All Files (*.);;Database Files (*.db)", options=options)

        if filename:
            ext = ".db"
            filename = filename + ext
            if copy2(backup_file, filename):
                QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("File copied"), QtWidgets.qApp.tr(
                    "Data has been backed up."), QtWidgets.QMessageBox.Ok)

    def newDebtor(self, MainWindow):
        Debtor = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Debtor.setWindowIcon(icon)
        ui_debt = Ui_FormDebtors()
        ui_debt.setupUi(Debtor)
        ui_debt.btnSave.clicked.connect(lambda: ui_debt.validate())
        ui_debt.btnCancel.clicked.connect(Debtor.close)
        Debtor.show()

    def viewInvoices(self, MainWindow):
        Invoices = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Invoices.setWindowIcon(icon)
        ui_inv = Ui_Invoices()
        ui_inv.setupUi(Invoices)
        ui_inv.btnNewInvoice.clicked.connect(lambda: self.createInvoice(MainWindow))
        Invoices.show()

    def newCreditor(self, MainWindow):
        Creditor = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Creditor.setWindowIcon(icon)
        ui_creditor = Ui_DialogCreditor()
        ui_creditor.setupUi(Creditor)
        Creditor.show()
        ui_creditor.btnSave.clicked.connect(lambda: ui_creditor.validate())
        ui_creditor.btnCancel.clicked.connect(Creditor.close)

    def editCreditors(self, MainWindow):
        EditCreditors = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditCreditors.setWindowIcon(icon)
        ui_edit = Ui_EditCreditors()
        ui_edit.setupUi(EditCreditors)
        ui_edit.btnEdit.clicked.connect(lambda: ui_edit.populate_fileds())
        ui_edit.btnNew.clicked.connect(lambda: self.newCreditor(MainWindow))
        EditCreditors.show()

    def newStock(self, MainWindow):
        Stock = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Stock.setWindowIcon(icon)
        self.update_table()
        ui = Ui_Stock()
        ui.setupUi(Stock)
        ui.btnRefresh.clicked.connect(lambda: ui.details())
        ui.selectStock()
        Stock.show()

    def newProduct(self, MainWindow):
        sql.connectDB()
        FormProduct = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormProduct.setWindowIcon(icon)
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
                        new_log(self.get_current_user(), operation="Added a new supplier " + supplierName.text())
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

            if (ui_prod_form.productName.text() == '' or ui_prod_form.productName.text().isspace()) and (
                    ui_prod_form.productCode.text() == '' or
                    ui_prod_form.productCode.text().isspace()) and (
                    ui_prod_form.realPrice.text() == '' or ui_prod_form.realPrice.text().isspace()) and (
                    ui_prod_form.salePrice.text() == '' or ui_prod_form.salePrice.text().isspace()) and (
                    ui_prod_form.dateAdded.text() == '' or
                    ui_prod_form.dateAdded.text().isspace()) and (
                    ui_prod_form.quantity.text() == '' or ui_prod_form.quantity.text().isspace()) and (
                    ui_prod_form.total.text() == '' or ui_prod_form.total.text().isspace()) and (
                    ui_prod_form.supplier.currentText() == '' or
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
                new_log(self.get_current_user(), "Added a new product " + ui_prod_form.productName.text())
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
                    self.update_table()
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

    def viewStock(self, MainWindow):
        Stocks = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Stocks.setWindowIcon(icon)
        ui = Ui_Stocks()
        ui.setupUi(Stocks)
        Stocks.show()

    def newSupplier(self, MainWindow):
        Supplier = QtWidgets.QMainWindow(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Supplier.setWindowIcon(icon)
        ui_supplier = Ui_Supplier()
        ui_supplier.setupUi(Supplier)
        sql.connectDB()
        qry = QtSql.QSqlQuery()
        qry.prepare("select distinct name from suppliers")
        qry.exec_()
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(qry)
        ui_supplier.supplierName.setModel(modal)

        def validate_data():
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
                new_log(self.get_current_user(), "Uploaded supplier information for " + ui_supplier.supplierName.currentText())
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

        Supplier.setGeometry(300, 40, 621, 583)
        ui_supplier.btnSave.clicked.connect(lambda: validate_data())
        Supplier.show()


    def newCustomer(self, MainWindow):
        NewCustomer = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewCustomer.setWindowIcon(icon)
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
                new_log(self.get_current_user(), "Created a new customer " + ui_customer.customerName.text())
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

        NewCustomer.setGeometry(360, 40, 544, 490)
        ui_customer.btnSave.clicked.connect(validate_data)
        NewCustomer.show()

    def editCustomer(self, MainWindow):
        EditCustomer = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditCustomer.setWindowIcon(icon)
        ui = Ui_EditCustomer()
        ui.setupUi(EditCustomer)
        ui.btnLoad.clicked.connect(lambda: ui.populate_fileds())
        ui.btnUpdate.clicked.connect(lambda: ui.update_records())
        ui.btnDelete.clicked.connect(lambda: ui.delete_record())
        EditCustomer.show()


    def get_stats(self, MainWindow):
        Analysis = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Analysis.setWindowIcon(icon)
        ui = Ui_Analysis()
        ui.setupUi(Analysis)
        Analysis.setGeometry(10, 45, 1337, 640)
        Analysis.show()


    def showAbout(self, MainWindow):
        Help_Dialog = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Help_Dialog.setWindowIcon(icon)
        ui_about = Ui_About()
        ui_about.setupUi(Help_Dialog)
        Help_Dialog.setWindowTitle("About IMS")
        Help_Dialog.setStyleSheet("background-color:#333;color:#fff;")
        Help_Dialog.setGeometry(450, 140, 400, 450)
        Help_Dialog.show()


    def showProducts(self, MainWindow):
        Products = QtWidgets.QDialog(MainWindow)
        Products.setWindowTitle("Products")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Products.setWindowIcon(icon)
        ui_products = Ui_Products()
        ui_products.setupUi(Products)
        ui_products.selectProducts()
        ui_products.tableView.setColumnHidden(0, True)
        ui_products.btnSearch.clicked.connect(lambda: ui_products.search_products())
        ui_products.btnEdit.clicked.connect(lambda: self.edit_product(Window))
        Products.setGeometry(40, 30, 1024, 650)
        ui_products.tableView.setMaximumWidth(950)
        ui_products.groupOne.setMaximumWidth(250)
        ui_products.groupOne.setFixedSize(550, 60)
        Products.show()


    def dialogSupplier(self,MainWindow):
        Form = QtWidgets.QDialog(MainWindow)
        Form.setWindowTitle("Add new supplier")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setGeometry(420, 200, 510, 100)
        supplierName = QtWidgets.QLineEdit(Form)
        supplierName.setObjectName("supplierName")
        supplierName.setGeometry(120, 40, 200, 30)
        lblName = QtWidgets.QLabel(Form)
        lblName.setText("Supplier Name:")
        lblName.setGeometry(10, 40, 100, 30)

        def save():
            if sql.connectDB():
                query = QtSql.QSqlQuery()
                if supplierName.text() == "" or supplierName.text().isspace():
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not Saved!"),
                                                   QtWidgets.qApp.tr("Suppplier name is required!"),
                                                   QtWidgets.QMessageBox.Close)
                else:
                    new_log(self.get_current_user(), "New supplier '" + supplierName.text() + "' added")
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


    def showContacts(self, MainWindow):
        Contacts = QtWidgets.QDialog(MainWindow)
        Contacts.setStyleSheet("background-color:#f0f0f0;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Contacts.setWindowIcon(icon)
        ui_contacts = Ui_Contacts()
        ui_contacts.setupUi(Contacts)
        ui_contacts.btnSave.clicked.connect(lambda: ui_contacts.saveNow())
        ui_contacts.btnSearch.clicked.connect(lambda: ui_contacts.search_contacts())
        ui_contacts.btnEdit.clicked.connect(lambda: ui_contacts.populate_fields())
        ui_contacts.btnUpdate.clicked.connect(lambda: ui_contacts.update_fields())
        ui_contacts.btnClose.clicked.connect(Contacts.close)
        ui_contacts.btnDelete.clicked.connect(lambda: ui_contacts.delete_contact())
        ui_contacts.showContacts()
        Contacts.setGeometry(340, 30, 637, 590)
        Contacts.show()


    ################################################################################################

    def get_product(self):
        if self.searchbox.text() == '' or self.searchbox.text().isspace():
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Enter search query"), QtWidgets.qApp.tr(
                "Please enter search criterion to search!"), QtWidgets.QMessageBox.Ok)
        else:
            qry = QtSql.QSqlQuery()
            qry.prepare("select * from products where product_name LIKE '%{0}%' or product_code LIKE '%{0}%' or "
                        "product_category LIKE '%{0}%' or date_added LIKE '%{0}%' or supplier LIKE '%{0}%'".format(
                str(self.searchbox.text())))
            # qry.bindValue(0, str(self.searchbox.text()))
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
                self.tblStockList.setModel(my_model)
                self.tblStockList.show()


    def show_suppliers(self, MainWindow):
        sql.connectDB()

        def search():
            if not inputFilter.text() == '' or not inputFilter.text().isspace():
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        suppliers.setWindowIcon(icon)
        suppliers.setGeometry(340, 30, 650, 490)
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
        inputFilter = QtWidgets.QLineEdit(suppliers)
        inputFilter.setGeometry(50, 45, 350, 30)
        inputFilter.setPlaceholderText("Search suppliers...")
        complet = QtWidgets.QCompleter()
        complet.setFilterMode(QtCore.Qt.MatchContains)
        complet.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        complet.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        inputFilter.setCompleter(complet)
        complet.setModel(my_model)
        btnSearch = QtWidgets.QPushButton(suppliers)
        btnSearch.setGeometry(360, 45, 80, 30)
        btnSearch.setText("Search")
        btnSearch.clicked.connect(lambda: search())
        inputFilter.textChanged.connect(lambda: search())
        btnNew = QtWidgets.QPushButton(suppliers)
        btnNew.setGeometry(470, 45, 120, 30)
        btnNew.setText("+ New Supplier")
        list = QtWidgets.QListView(suppliers)
        list.setGeometry(50, 85, 550, 360)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(45)
        list.setFont(font)
        list.setAlternatingRowColors(True)
        list.setStyleSheet(self.stylesheet())
        list.setModel(my_model)
        list.show()
        btnClose = QtWidgets.QPushButton(suppliers)
        btnClose.setGeometry(500, 450, 90, 35)
        btnClose.setText("Close")
        btnNew.clicked.connect(lambda: self.dialogSupplier(MainWindow))
        btnClose.clicked.connect(suppliers.close)
        suppliers.show()


    def dialogContact(self, MainWindow):
        def save():
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
                    new_log(self.get_current_user(), "Added a new contact information for " + contactName.text())
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Contact.setWindowIcon(icon)
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


    def showDebtors(self, MainWindow):
        Debtors = QtWidgets.QDialog(MainWindow)
        Debtors.setWindowTitle("Ahasaniya Enterprice | Debtors")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Debtors.setWindowIcon(icon)
        ui_d = Ui_Debtors()
        ui_d.setupUi(Debtors)
        ui_d.debtorView.setColumnHidden(0, True)
        ui_d.display_debtors()
        ui_d.btnSearch.clicked.connect(lambda: ui_d.get_debtor())
        ui_d.btnNewDebtor.clicked.connect(lambda: self.newDebtor(MainWindow))
        ui_d.btnEdit.clicked.connect(lambda: self.editDebtors(MainWindow))
        Debtors.show()

    def editDebtors(self, MainWindow):
        Dialog = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        ui_upd = Ui_EditDebtors()
        ui_upd.setupUi(Dialog)
        ui_upd.btnNewDebtor.clicked.connect(lambda: self.newDebtor(MainWindow))
        ui_upd.btnDelete.clicked.connect(lambda: ui_upd.delete_record())
        Dialog.show()


    def showCreditors(self, MainWindow):
        Creditors = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Creditors.setWindowIcon(icon)
        ui = Ui_Creditors()
        ui.setupUi(Creditors)
        ui.creditorView.setColumnHidden(0, True)
        ui.display_creditors()
        ui.btnSearch.clicked.connect(lambda: ui.get_creditor(MainWindow))
        ui.btnEdit.clicked.connect(lambda: self.editCreditors(MainWindow))
        ui.btnNewCreditor.clicked.connect(lambda: self.newCreditor(MainWindow))
        ui.btnDelete.clicked.connect(lambda: self.select_item(MainWindow))
        Creditors.show()


    def dialogCategory(self, MainWindow):
        def save():
            import sql
            if sql.connectDB():
                query = QtSql.QSqlQuery()
                if categoryName.text() == "" or categoryName.text().isspace():
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not Saved!"),
                                                   QtWidgets.qApp.tr("Category is required!"),
                                                   QtWidgets.QMessageBox.Close)
                else:
                    new_log(self.get_current_user(), "Added new category - " + categoryName.text())
                    query.prepare("insert into categories(name) values(?)")
                    query.bindValue(0, categoryName.text())
                    if query.exec_():
                        categoryName.setText("")
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


    def showCustomers(self, MainWindow):
        Customers = QtWidgets.QDialog(MainWindow)
        Customers.setStyleSheet("background-color:#fff;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Customers.setWindowIcon(icon)
        Customers.setGeometry(120, 20, 1201, 760)
        ui_custs = Ui_Customers()
        ui_custs.setupUi(Customers)
        ui_custs.btnFilter.clicked.connect(lambda: ui_custs.filter_customers())
        ui_custs.btnNew.clicked.connect(lambda: self.newCustomer(MainWindow))
        ui_custs.btnEdit.clicked.connect(lambda: self.editCustomer(MainWindow))
        ui_custs.showView()
        Customers.show()


    def showRegistration(self, MainWindow):
        w = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        w.setWindowIcon(icon)
        ui_register = Ui_Registration()
        ui_register.setupUi(w)
        w.setWindowTitle("Register now")
        w.show()

    def showReturns(self, MainWindow):
        Returns = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Returns.setWindowIcon(icon)
        ui = Ui_Returns()
        ui.setupUi(Returns)
        ui.display_returns()
        ui.btnClose.clicked.connect(Returns.close)
        ui.btnNewReturn.clicked.connect(lambda: ui.new_return(MainWindow))
        ui.btnNewEdit.clicked.connect(lambda: ui.populate_fileds())
        ui.btnEdit.clicked.connect(lambda: ui.showMessage())
        ui.btnDelete.clicked.connect(lambda: ui.delete_record())
        ui.btnSearch.clicked.connect(lambda: ui.get_return())
        ui.btnUpdate.clicked.connect(lambda: ui.update_records())
        Returns.show()


    def saveCategory(self, item1):
        if sql.connectDB():
            ui_category = Ui_Category()
            sql.connectDB()
            query = QtSql.QSqlQuery()
            if item1.text() == "" or item1.text().isspace():
                QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not Saved!"),
                                               QtWidgets.qApp.tr("Please enter category to save!"),
                                               QtWidgets.QMessageBox.Close)
            else:
                new_log(self.get_current_user(), "Created a new category " + item1.text())
                query.prepare("insert into categories(name) values(?)")
                query.bindValue(0, item1.text())
                if query.exec_():
                    item1.setText("")
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

    def delete_record(self, item1):
        sql.connectDB()
        if not item1.currentText() == '' and not item1.currentText().isspace():
            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete?"),
                QtWidgets.qApp.tr(
                    "Are you sure you want to delete <b>" + item1.currentText() + "</b>?"),
                QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if confirm == QtWidgets.QMessageBox.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("delete from categories where name = ?")
                query.bindValue(0, item1.currentText())
                if query.exec_():
                    operation = "Deleted " + item1.currentText() + " from categories"
                    new_log(self.get_current_user(), operation)
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Category deleted!"),
                              QtWidgets.qApp.tr("Category has been deleted successfully"),
                              QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Category not deleted!"),
                                                   QtWidgets.qApp.tr("Category couldn't be deleted"),
                                                   QtWidgets.QMessageBox.Ok)

    def showCat(self, MainWindow):
        Category = QtWidgets.QDialog(MainWindow)
        Category.setWindowTitle("Product Categories")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Category.setWindowIcon(icon)
        ui_category = Ui_Category()
        ui_category.setupUi(Category)
        sql.connectDB()
        ui_category.btnUpdate.setText("Close")
        ui_category.btnUpdate.clicked.connect(Category.close)
        ui_category.btnSave.clicked.connect(lambda: self.saveCategory(ui_category.categoryName))
        ui_category.btnDelete.clicked.connect(lambda: self.delete_record(ui_category.delete_select))
        Category.show()

    def createInvoice(self, MainWindow):
        sql.connectDB()
        Invoice = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Invoice.setWindowIcon(icon)
        Invoice.setWindowTitle("Generate a new invoice")
        Invoice.setGeometry(0.25 * MainWindow.width(), 0.3 * MainWindow.height(), 0.50 * MainWindow.width(), 285)
        label = QtWidgets.QLabel(Invoice)
        label.setGeometry(10, 10, 250, 30)
        label.setText("Select product to generate invoice:")
        select_product = QtWidgets.QComboBox(Invoice)
        select_product.setGeometry(10, 40, 0.45 * Invoice.width(), 35)
        label_pay = QtWidgets.QLabel(Invoice)
        label_pay.setGeometry(15 + 0.48 * Invoice.width(), 10, 100, 35)
        label_pay.setText("Status:")
        select_status = QtWidgets.QComboBox(Invoice)
        select_status.setGeometry(15 + 0.48 * Invoice.width(), 40, 0.20 * Invoice.width(), 35)
        select_status.addItem("")
        select_status.addItem("")
        select_status.addItem("")
        select_status.setItemText(0, "Paid")
        select_status.setItemText(1, " Payment Incomplete")
        select_status.setItemText(2, "Unpaid")
        lbl_amount = QtWidgets.QLabel(Invoice)
        lbl_amount.setGeometry(15 + 0.71 * Invoice.width(), 10, 0.21 * Invoice.width(), 35)
        lbl_amount.setText("Amount Paid:")
        amount_paid = QtWidgets.QLineEdit(Invoice)
        amount_paid.setGeometry(15 + 0.71 * Invoice.width(), 40, 0.24 * Invoice.width(), 35)
        c_label = QtWidgets.QLabel(Invoice)
        c_label.setGeometry(10, 100, 250, 30)
        c_label.setText("Select from below:")
        customer_name = QtWidgets.QComboBox(Invoice)
        customer_name.setGeometry(10, 140, 0.28 * Invoice.width(), 35)
        mod = QtSql.QSqlQueryModel()
        querry = QtSql.QSqlQuery()
        querry.exec_("select distinct name from customers")
        mod.setQuery(querry)

        def toggle():
            btnName.hide()
            cust_label.show()
            cust_label.setGeometry(10, 100, 250, 30)
            name_enter.show()
            name_enter.setFocus(QtCore.Qt.PopupFocusReason)
            c_label.hide()
            c_labl.hide()

            customer_name.hide()

        if mod.rowCount() > 0:
            customer_name.setModel(mod)
            c_labl = QtWidgets.QLabel(Invoice)
            c_labl.setGeometry(15 + 0.30 * Invoice.width(), 140, 20, 30)
            c_labl.setText("Or")
            cust_label = QtWidgets.QLabel(Invoice)
            cust_label.setGeometry(10 + 0.35 * Invoice.width(), 100, 250, 30)
            cust_label.setText("Enter customer name:")
            name_enter = QtWidgets.QLineEdit(Invoice)
            name_enter.setGeometry(10, 140, 0.65 * Invoice.width(), 35)
            name_enter.hide()
            btnName = QtWidgets.QPushButton(Invoice)
            btnName.setText("Click to enter name")
            btnName.setGeometry(10 + 0.35 * Invoice.width(), 140, 0.30 * Invoice.width(), 35)
            btnName.clicked.connect(toggle)


        qty_label = QtWidgets.QLabel(Invoice)
        qty_label.setGeometry(15 + 0.65 * Invoice.width(), 100, 0.3 * Invoice.width(), 35)
        qty_label.setText("Quantity:")
        quantity = QtWidgets.QLineEdit(Invoice)
        quantity.setGeometry(15 + 0.66 * Invoice.width(), 140, 0.3 * Invoice.width(), 35)
        btnSubmit = QtWidgets.QPushButton(Invoice)
        btnSubmit.setGeometry(15 + 0.81 * Invoice.width(), 200, 100, 40)
        btnSubmit.setText("Generate")
        btnExit = QtWidgets.QPushButton(Invoice)
        btnExit.setGeometry(15 + 0.60 * Invoice.width(), 200, 0.20 * Invoice.width(), 40)
        btnExit.setText("Cancel")
        btnExit.clicked.connect(Invoice.close)
        model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        query.exec_("Select distinct product_name from products")
        model.setQuery(query)
        if num_rows(query) > 0:
            select_product.setModel(model)

        def generate_invoice():
            error = 0
            if len(name_enter.text()) > 0:
                customer = name_enter.text()
            else:
                customer = customer_name.currentText()

            if (customer == "" or customer.isspace()) and \
                    (quantity.text() == "" or quantity.text().isspace()):
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Fill all fields"),
                                                  QtWidgets.qApp.tr("Please enter customer name and quantity!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 1
            elif amount_paid.text() == "" or amount_paid.text().isspace():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Enter Amount Paid"),
                                                  QtWidgets.qApp.tr("\nPlease enter amount paid by customer!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 2

            elif amount_paid.text().isalnum():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Enter Valid Amount Paid"),
                                                  QtWidgets.qApp.tr("\nPlease enter a numeric value for amount!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 2

            elif quantity.text() == "" or quantity.text().isspace():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Enter Quantity"),
                                                  QtWidgets.qApp.tr("\nPlease enter quantity!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 3

            elif customer == "" or customer.isspace():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Fill customer name"),
                                        QtWidgets.qApp.tr("\nPlease provide customer name!"), QtWidgets.QMessageBox.Ok)
                error = 4
            elif quantity.text().isnumeric() == False:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Invalid Quantity Value"),
                                        QtWidgets.qApp.tr("\nQuantity must be a number!"), QtWidgets.QMessageBox.Ok)

                error = 5

            elif customer.isnumeric():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Invalid customer name"),
                                QtWidgets.qApp.tr("\nPlease provide a valid customer name!"), QtWidgets.QMessageBox.Ok)
                error = 6

            if error == 0:
                date_bought = QtCore.QDate.currentDate().toString()
                connection = sqlite3.connect("ims.db")
                if connection:
                    cursor = connection.cursor()
                    cursor.execute("select * from products where product_name = '{0}'".format(str(select_product.currentText())))
                    rows = cursor.fetchall()
                    modal = QtSql.QSqlTableModel()
                    q = QtSql.QSqlQuery()
                    q.exec_("select * from products where product_name = '{0}'".format(
                        select_product.currentText()))
                    modal.setQuery(q)
                    sale_price = rows[0][4]
                    real_price = rows[0][3]
                    qty = quantity.text()
                    subtotal = round(sale_price * int(qty))
                    tax_rate = 0.00
                    total_payable = subtotal + tax_rate
                    amount = amount_paid.text()
                    balance = float(amount) - total_payable
                    code = rows[0][1]
                    qery = QtSql.QSqlQuery()
                    new_log(self.get_current_user(), "Generated a new invoice for " + customer)
                    qery.prepare("insert into invoices(customer_name, invoice_number, product_code, product_name, "
                                 "sale_price, real_price, amount_paid, balance, quantity, total, date_bought) values("
                                 "?,?,?,?,?,?,?,?,?,?,?)")
                    qery.bindValue(0, customer)
                    qery.bindValue(1, invoice_no)
                    qery.bindValue(2, code)
                    qery.bindValue(3, rows[0][2])
                    qery.bindValue(4, sale_price)
                    qery.bindValue(5, real_price)
                    qery.bindValue(6, amount)
                    qery.bindValue(7, balance)
                    qery.bindValue(8, qty)
                    qery.bindValue(9, total_payable)
                    qery.bindValue(10, date_bought)
                    if qery.exec_():
                        Invoice.close()
                        newInvoice = QtWidgets.QMainWindow(MainWindow)
                        ui_invoice = Ui_newInvoice()
                        ui_invoice.setupUi(newInvoice)
                        ui_invoice.invoiceNo.setText(invoice_no)
                        ui_invoice.date.setText(date_bought)
                        ui_invoice.dueDate.setText(date_bought)

                        q = QtSql.QSqlQuery()
                        q.prepare("select * from invoices where invoice_number = '{0}'".format(invoice_no))
                        q.exec_()
                        modl = QtSql.QSqlQueryModel()
                        modl.setQuery(q)
                        modl.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
                        modl.setHeaderData(2, QtCore.Qt.Horizontal, "Invoice No.")
                        modl.setHeaderData(3, QtCore.Qt.Horizontal, "Product Name")
                        modl.setHeaderData(5, QtCore.Qt.Horizontal, "Sale Price")
                        modl.setHeaderData(7, QtCore.Qt.Horizontal, "Amount Paid")
                        modl.setHeaderData(8, QtCore.Qt.Horizontal, "Balance")
                        modl.setHeaderData(9, QtCore.Qt.Horizontal, "Quantity")
                        modl.setHeaderData(10, QtCore.Qt.Horizontal, "Total")
                        modl.setHeaderData(11, QtCore.Qt.Horizontal, "Date")
                        ui_invoice.invoiceView.setModel(modl)
                        ui_invoice.invoiceView.horizontalHeader().setMinimumHeight(40)
                        ui_invoice.invoiceView.horizontalHeader().setDefaultSectionSize(120)
                        ui_invoice.invoiceView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                        ui_invoice.invoiceView.setShowGrid(True)
                        ui_invoice.invoiceView.show()
                        ui_invoice.tax.setText(str(tax_rate))
                        ui_invoice.subtotal.setText("GHC" + str(subtotal))
                        ui_invoice.amountPaid.setText("GHC" + str(amount))
                        ui_invoice.paymentStatus.setText(select_status.currentText())
                        # ui_invoice.rate.setText("GHC" + str(sale_price))
                        ui_invoice.balance.setText(str(balance) + "(GHC)")
                        ui_invoice.total.setText("GHC" + str(total_payable))
                        # ui_invoice.amount.setText("GHC" + str(subtotal))
                        ui_invoice.toName.setText(customer)
                        newInvoice.show()

            qry = QtSql.QSqlQuery()
            qry.prepare("select * from products where product_name = ?")
            qry.bindValue(0, select_product.currentText())

        btnSubmit.clicked.connect(lambda: generate_invoice())
        Invoice.show()


    def new_invoice(self, MainWindow):
        NewInvoice = QtWidgets.QMainWindow(MainWindow)
        NewInvoice.setGeometry(0.20 * MainWindow.width(), 40, 772, 618)
        ui_ = Ui_NewInvoice()
        ui_.setupUi(NewInvoice)
        invoice_no = strftime("%m%y%d%H%M%S", gmtime())
        ui_.invoice_no.setText(invoice_no)
        NewInvoice.show()

        def generate_invoice():
            error = 0
            if len(ui_.name_enter.text()) > 0:
                customer = ui_.name_enter.text()
            else:
                customer = ui_.customer.currentText()

            if (customer == "" or customer.isspace()) and \
                    (ui_.quantity.text() == "" or ui_.quantity.text().isspace()):
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Fill all fields"),
                                                  QtWidgets.qApp.tr("Please enter customer name and quantity!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 1
            elif ui_.amount.text() == "" or ui_.amount.text().isspace():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Enter Amount Paid"),
                                                  QtWidgets.qApp.tr("\nPlease enter amount paid by customer!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 2

            elif ui_.amount.text().isalnum():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Enter Valid Amount Paid"),
                                                  QtWidgets.qApp.tr("\nPlease enter a numeric value for amount!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 2

            elif ui_.quantity.text() == "" or ui_.quantity.text().isspace():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Enter Quantity"),
                                                  QtWidgets.qApp.tr("\nPlease enter quantity!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 3

            elif customer == "" or customer.isspace():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Fill customer name"),
                                                  QtWidgets.qApp.tr("\nPlease provide customer name!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 4
            elif ui_.quantity.text().isnumeric() == False:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Invalid Quantity Value"),
                                                  QtWidgets.qApp.tr("\nQuantity must be a number!"),
                                                  QtWidgets.QMessageBox.Ok)

                error = 5

            elif customer.isnumeric():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Invalid customer name"),
                                                  QtWidgets.qApp.tr("\nPlease provide a valid customer name!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 6

            if error == 0:
                query = QtSql.QSqlQuery()
                query.prepare("select invoice_number from invoices where invoice_number = ?")
                query.bindValue(0, ui_.invoice_no.text())
                if query.exec_():
                    if num_rows(query) > 0:
                        invoice_no = query.value(0)
                        print("Invoice no.:" + query.value(0))

                date_bought = QtCore.QDate.currentDate().toString()
                connection = sqlite3.connect("ims.db")
                if connection:
                    cursor = connection.cursor()
                    cursor.execute("select * from products where product_name = '{0}'".format(
                        str(ui_.select_product.currentText())))
                    rows = cursor.fetchall()
                    modal = QtSql.QSqlTableModel()
                    q = QtSql.QSqlQuery()
                    q.exec_("select * from products where product_name = '{0}'".format(
                        ui_.select_product.currentText()))
                    modal.setQuery(q)
                    sale_price = rows[0][4]
                    real_price = rows[0][3]
                    qty = ui_.quantity.text()
                    subtotal = round(sale_price * int(qty))
                    tax_rate = 0.00
                    total_payable = subtotal + tax_rate
                    amount = ui_.amount.text()
                    balance = float(amount) - total_payable
                    code = rows[0][1]
                    qery = QtSql.QSqlQuery()
                    qery.prepare("insert into invoices(customer_name, invoice_number, product_code, product_name, "
                                 "sale_price, real_price, amount_paid, balance, quantity, total, date_bought) values("
                                 "?,?,?,?,?,?,?,?,?,?,?)")
                    qery.bindValue(0, customer)
                    qery.bindValue(1, invoice_no)
                    qery.bindValue(2, code)
                    qery.bindValue(3, rows[0][2])
                    qery.bindValue(4, sale_price)
                    qery.bindValue(5, real_price)
                    qery.bindValue(6, amount)
                    qery.bindValue(7, balance)
                    qery.bindValue(8, qty)
                    qery.bindValue(9, total_payable)
                    qery.bindValue(10, date_bought)
                    if qery.exec_():
                        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Product Added"),
                                                          QtWidgets.qApp.tr("Product has been added!"),
                                                          QtWidgets.QMessageBox.Ok)
                        NewInvoice.close()
                        newInvoice = QtWidgets.QMainWindow(MainWindow)
                        ui_invoice = Ui_newInvoice()
                        ui_invoice.setupUi(newInvoice)
                        ui_invoice.invoiceNo.setText(invoice_no)
                        ui_invoice.date.setText(date_bought)
                        ui_invoice.dueDate.setText(date_bought)

                        q = QtSql.QSqlQuery()
                        q.prepare("select * from invoices where invoice_number = '{0}'".format(invoice_no))
                        q.exec_()
                        modl = QtSql.QSqlQueryModel()
                        modl.setQuery(q)
                        modl.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
                        modl.setHeaderData(1, QtCore.Qt.Horizontal, "Customer")
                        modl.setHeaderData(2, QtCore.Qt.Horizontal, "Invoice No.")
                        modl.setHeaderData(3, QtCore.Qt.Horizontal, "Product Code")
                        modl.setHeaderData(4, QtCore.Qt.Horizontal, "Product Name")
                        modl.setHeaderData(5, QtCore.Qt.Horizontal, "Sale Price")
                        modl.setHeaderData(6, QtCore.Qt.Horizontal, "Sale Price")
                        modl.setHeaderData(7, QtCore.Qt.Horizontal, "Amount Paid")
                        modl.setHeaderData(8, QtCore.Qt.Horizontal, "Balance")
                        modl.setHeaderData(9, QtCore.Qt.Horizontal, "Quantity")
                        modl.setHeaderData(10, QtCore.Qt.Horizontal, "Total")
                        modl.setHeaderData(11, QtCore.Qt.Horizontal, "Date")
                        ui_invoice.invoiceView.setModel(modl)
                        ui_invoice.invoiceView.horizontalHeader().setMinimumHeight(50)
                        ui_invoice.invoiceView.horizontalHeader().setStyleSheet("background-color:black;color:#fff;")
                        ui_invoice.invoiceView.horizontalHeader().setDefaultSectionSize(120)
                        ui_invoice.invoiceView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                        ui_invoice.invoiceView.setColumnHidden(0, True)
                        ui_invoice.invoiceView.setColumnHidden(3, True)
                        ui_invoice.invoiceView.setColumnHidden(6, True)
                        ui_invoice.invoiceView.setShowGrid(True)
                        ui_invoice.invoiceView.show()
                        ui_invoice.tax.setText(str(tax_rate))
                        ui_invoice.subtotal.setText("GHC" + str(subtotal))
                        ui_invoice.amountPaid.setText("GHC" + str(amount))
                        ui_invoice.paymentStatus.setText(ui_.status.currentText())
                        # ui_invoice.rate.setText("GHC" + str(sale_price))
                        ui_invoice.balance.setText(str(balance) + "(GHC)")
                        ui_invoice.total.setText("GHC" + str(total_payable))
                        # ui_invoice.amount.setText("GHC" + str(subtotal))
                        ui_invoice.toName.setText(customer)
                        newInvoice.show()

        ui_.btnSubmit.clicked.connect(lambda: generate_invoice())

    def addSale(self, MainWindow):
        sql.connectDB()
        Sale = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Sale.setWindowIcon(icon)
        Sale.setWindowTitle("Add a new sale")
        Sale.setGeometry(0.25 * MainWindow.width(), 0.3 * MainWindow.height(), 0.40 * MainWindow.width(), 285)
        label = QtWidgets.QLabel(Sale)
        label.setGeometry(30, 10, 250, 30)
        label.setText("Select product:")
        select_product = QtWidgets.QComboBox(Sale)
        select_product.setGeometry(30, 40, 0.4 * Sale.width(), 35)
        product_enter = QtWidgets.QLineEdit(Sale)
        product_enter.setGeometry(30, 40, 0.40 * Sale.width(), 35)
        product_enter.hide()
        btnProduct = QtWidgets.QPushButton(Sale)
        btnProduct.setText("+")
        btnProduct.setStyleSheet("font-size:20px;")
        btnProduct.setGeometry(31 + 0.4 * Sale.width(), 40, 35, 35)
        btnProduct.setToolTip("Click to enter product name")
        btnProduct.clicked.connect(lambda: slide())
        lbl_amount = QtWidgets.QLabel(Sale)
        lbl_amount.setGeometry(15 + 0.55 * Sale.width(), 10, 0.25 * Sale.width(), 35)
        lbl_amount.setText("Amount Paid:")
        amount_paid = QtWidgets.QLineEdit(Sale)
        amount_paid.setDisabled(True)
        amount_paid.setGeometry(15 + 0.51 * Sale.width(), 40, 0.35 * Sale.width(), 35)
        btnref = QtWidgets.QPushButton(Sale)
        btnref.setGeometry(15 + 0.86 * Sale.width(), 40, 35, 35)
        btnref.setText("+")
        btnref.setStyleSheet("color:#ff6622;font-size:20px;")
        btnref.clicked.connect(lambda: amount_paid.setEnabled(True))
        btnref.setToolTip("Click to add custom amount")
        c_label = QtWidgets.QLabel(Sale)
        c_label.setGeometry(30, 100, 250, 30)
        c_label.setText("Select from below:")
        customer_name = QtWidgets.QComboBox(Sale)
        customer_name.setGeometry(30, 140, 0.40 * Sale.width(), 35)
        mod = QtSql.QSqlQueryModel()
        querry = QtSql.QSqlQuery()
        querry.exec_("select distinct name from customers")
        mod.setQuery(querry)

        def slide():
            select_product.hide()
            product_enter.show()
            prd_label = QtWidgets.QLabel(Sale)
            prd_label.setGeometry(30, 10, 250, 30)
            prd_label.setText("Enter product name:")
            prd_label.show()
            product_enter.show()
            product_enter.setFocus(QtCore.Qt.PopupFocusReason)
            label.hide()


        def toggle():
            btnName.hide()
            cust_label = QtWidgets.QLabel(Sale)
            cust_label.setGeometry(10 + 0.35 * Sale.width(), 100, 250, 30)
            cust_label.setText("Enter customer name:")
            cust_label.show()
            cust_label.setGeometry(30, 100, 250, 30)
            name_enter.show()
            name_enter.setFocus(QtCore.Qt.PopupFocusReason)
            c_label.hide()

            customer_name.hide()

        if mod.rowCount() > 0:
            customer_name.setModel(mod)
            name_enter = QtWidgets.QLineEdit(Sale)
            name_enter.setGeometry(30, 140, 0.40 * Sale.width(), 35)
            name_enter.hide()
            btnName = QtWidgets.QPushButton(Sale)
            btnName.setText("+")
            btnName.setStyleSheet("font-size:20px;")
            btnName.setGeometry(10 + 0.44 * Sale.width(), 140, 35, 35)
            btnName.clicked.connect(toggle)
        else:
            customer_name.setDisabled(True)
            c_label.hide()
            cust_label = QtWidgets.QLabel(Sale)
            cust_label.setGeometry(10 + 0.35 * Sale.width(), 100, 250, 30)
            cust_label.setText("Enter customer name:")
            cust_label.show()
            cust_label.setGeometry(30, 100, 250, 30)
            name_enter = QtWidgets.QLineEdit(Sale)
            name_enter.setGeometry(30, 140, 0.45 * Sale.width(), 35)
            name_enter.hide()
            name_enter.show()

        qty_label = QtWidgets.QLabel(Sale)
        qty_label.setGeometry(15 + 0.54 * Sale.width(), 100, 0.3 * Sale.width(), 35)
        qty_label.setText("Quantity:")
        quantity = QtWidgets.QLineEdit(Sale)
        quantity.setGeometry(15 + 0.54 * Sale.width(), 140, 0.39 * Sale.width(), 35)
        btnSubmit = QtWidgets.QPushButton(Sale)
        btnSubmit.setGeometry(15 + 0.74 * Sale.width(), 200, 100, 35)
        btnSubmit.setText("Submit")
        btnExit = QtWidgets.QPushButton(Sale)
        btnExit.setGeometry(15 + 0.55 * Sale.width(), 200, 0.18 * Sale.width(), 35)
        btnExit.setText("Cancel")
        btnExit.clicked.connect(Sale.close)
        model = QtSql.QSqlQueryModel()

        print(strftime("%c", gmtime()))
        query = QtSql.QSqlQuery()
        query.exec_("Select distinct product_name, sale_price from products")
        model.setQuery(query)
        comp = QtWidgets.QCompleter()
        comp.setModel(model)
        comp.setCompletionColumn(0)
        comp.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        product_enter.setCompleter(comp)
        if num_rows(query) > 0:
            select_product.setModelColumn(0)
            select_product.setModel(model)
            select_product.currentTextChanged.connect(lambda: sel_changed())
            product_enter.textChanged.connect(lambda: sel_changed())

        def sel_changed():
            conn = sqlite3.connect("ims.db")
            cursor = conn.cursor()
            if product_enter.text() == "":
                cursor.execute("select sale_price from products where product_name = '{0}'".format(select_product.currentText()))
                row = cursor.fetchall()
                amount_paid.setText(str(row[0][0]))
            else:
                cursor.execute(
                    "select sale_price from products where product_name = '{0}'".format(product_enter.text()))
                row = cursor.fetchall()
                if len(row) > 0:
                    amount_paid.setText(str(row[0][0]))


        def generate_sale():
            error = 0
            if len(name_enter.text()) > 0:
                customer = name_enter.text()
            else:
                customer = customer_name.currentText()

            if (customer == "" or customer.isspace()) and \
                    (quantity.text() == "" or quantity.text().isspace()):
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Fill all fields"),
                                                  QtWidgets.qApp.tr("Please enter customer name and quantity!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 1
            elif amount_paid.isEnabled():

                if amount_paid.text() == "" or amount_paid.text().isspace():
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Enter Amount Paid"),
                                                  QtWidgets.qApp.tr("\nPlease enter amount paid by customer!"),
                                                  QtWidgets.QMessageBox.Ok)
                    error = 2

                elif amount_paid.text().isalnum():
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Enter Valid Amount Paid"),
                                                      QtWidgets.qApp.tr("\nPlease enter a numeric value for amount!"),
                                                      QtWidgets.QMessageBox.Ok)
                    error = 2

            elif quantity.text() == "" or quantity.text().isspace():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Enter Quantity"),
                                                  QtWidgets.qApp.tr("\nPlease enter quantity!"),
                                                  QtWidgets.QMessageBox.Ok)
                error = 3

            elif customer == "" or customer.isspace():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Fill customer name"),
                                        QtWidgets.qApp.tr("\nPlease provide customer name!"), QtWidgets.QMessageBox.Ok)
                error = 4
            elif quantity.text().isnumeric() == False:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Invalid Quantity Value"),
                                        QtWidgets.qApp.tr("\nQuantity must be a number!"), QtWidgets.QMessageBox.Ok)

                error = 5

            elif customer.isnumeric():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Invalid customer name"),
                                QtWidgets.qApp.tr("\nPlease provide a valid customer name!"), QtWidgets.QMessageBox.Ok)
                error = 6

            if error == 0:
                date_bought = strftime("%d/%m/%Y", gmtime())
                connection = sqlite3.connect("ims.db")
                if connection:
                    cursor = connection.cursor()
                    cursor.execute("select sale_price from products where product_name = '{0}'".format(
                        str(select_product.currentText())))
                    rows = cursor.fetchall()

                    if amount_paid.text() == '':
                        amount = rows[0][0]
                    else:
                        amount = amount_paid.text()

                    if product_enter.text() == "":
                        product_name = select_product.currentText()
                    else:
                        product_name = product_enter.text()

                    qty  = quantity.text()
                    qery = QtSql.QSqlQuery()
                    qery.prepare("insert into sales(customer_name, product_name, amount_paid, quantity, date_bought) "
                                 "values(?,?,?,?,?)")
                    qery.bindValue(0, customer)
                    qery.bindValue(1, product_name)
                    qery.bindValue(2, amount)
                    qery.bindValue(3, qty)
                    qery.bindValue(4, date_bought)
                    if qery.exec_():
                        q = QtSql.QSqlQuery()
                        q.prepare("update products set quantity = (quantity - ?) where product_name = ? and sale_price = ?")
                        q.bindValue(0, int(qty))
                        q.bindValue(1, select_product.currentText())
                        q.bindValue(2, rows[0][0])
                        if q.exec_():
                            new_log(self.get_current_user(), "Sold item <b>" + product_name + "</b> for " + customer)
                            quantity.clear()
                            self.update_table()
                            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Product purchase added"),
                                                              QtWidgets.qApp.tr("\nSale has been added successfully."),
                                                              QtWidgets.QMessageBox.Ok)
                    else:
                        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Error"),
                                                          QtWidgets.qApp.tr("\nThe sale could not be added!"),
                                                          QtWidgets.QMessageBox.Ok)

        btnSubmit.clicked.connect(lambda: generate_sale())
        Sale.show()

    def mainLoop(self, MainWindow):
        Logs = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Logs.setWindowIcon(icon)
        ui_logs = Ui_Logs()
        ui_logs.setupUi(Logs)

        ui_logs.get_logs()
        ui_logs.logsView.setColumnHidden(0, True)
        ui_logs.logsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        Logs.setGeometry(320, 50, 720, 600)
        Logs.show()

    def showUsers(self, MainWindow):
        sql.connectDB()
        Users = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Users.setWindowIcon(icon)
        ui_users = Ui_Users()
        ui_users.setupUi(Users)
        ui_users.widgetUsers.showMaximized()
        ui_users.widgetUsers.setColumnHidden(0, True)
        ui_users.widgetUsers.setColumnHidden(2, True)
        ui_users.widgetUsers.horizontalHeader().setMinimumHeight(40)
        ui_users.widgetUsers.horizontalHeader().setDefaultSectionSize(120)
        ui_users.widgetUsers.horizontalHeader().setMinimumSectionSize(100)
        ui_users.widgetUsers.horizontalHeader().setSortIndicatorShown(True)
        ui_users.widgetUsers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        Users.show()

    def showSales(self, MainWindow):
        Sales = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Sales.setWindowIcon(icon)
        ui_sale = Ui_Sales()
        ui_sale.setupUi(Sales)
        ui_sale.btnNewSale.deleteLater()
        Sales.show()

    def edit_suppliers(self, MainWindow):
        SupplierInfo = QtWidgets.QMainWindow(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SupplierInfo.setWindowIcon(icon)
        SupplierInfo.setWindowTitle("Supplier Information")
        Sup = QtWidgets.QTabWidget(SupplierInfo)
        ui = Ui_SupplierInfo()
        ui.setupUi(Sup)
        w = MainWindow.width()
        h = MainWindow.height()
        SupplierInfo.setGeometry((20/100) * w, 25, 69/100*w, 90/100*h)
        Sup.setGeometry(0, 0, 69 / 100 * w, 90 / 100 * h)
        ui.btnNew.clicked.connect(lambda: self.newSupplier(MainWindow))
        ui.btnCancel.clicked.connect(SupplierInfo.close)
        ui.btnExit.clicked.connect(SupplierInfo.close)
        Sup.show()
        SupplierInfo.show()

    def view_sales(self, MainWindow):
        ViewSales = QtWidgets.QDialog(MainWindow)
        ui = Ui_ViewSales()
        ui.setupUi(ViewSales)
        ViewSales.show()

    def edit_product(self, MainWindow):
        EditProduct = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditProduct.setWindowIcon(icon)
        ui_edit = Ui_EditProduct()
        ui_edit.setupUi(EditProduct)
        ui_edit.btnSave.clicked.connect(lambda: ui_edit.validate())
        ui_edit.btnRefresh.clicked.connect(lambda: ui_edit.populate_fileds())
        ui_edit.btnAddSupplier.clicked.connect(lambda: self.dialogSupplier(MainWindow))
        EditProduct.show()

    def select_item(self, MainWindow):
        widget = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        widget.setWindowIcon(icon)
        widget.setGeometry(30/100 * MainWindow.width(), 0.3 * MainWindow.height(), 550, 300)
        widget.setWindowTitle("Choose item to delete")
        label = QtWidgets.QLabel(widget)
        label.setText("Select item category:")
        label.setGeometry(20, 20, 150, 30)
        label.show()
        selected = QtWidgets.QComboBox(widget)
        selected.setGeometry(172, 20, 250, 30)
        meta = ["Products", "Users", "Categories", "Debtors", "Suppliers", "Creditors", "Contacts", "Customers", "Returns",
                "Logs", "Supplier Information"]
        _translate = QtCore.QCoreApplication.translate
        selected.addItems(meta)
        selected.show()
        btnContinue = QtWidgets.QPushButton(widget)
        btnContinue.setGeometry(425, 20, 90, 30)
        btnContinue.setText("Continue")
        btnContinue.show()
        group = QtWidgets.QGroupBox(widget)
        group.setGeometry(20, 60, 499, 100)
        del_action = QtWidgets.QLabel(group)
        del_action.setGeometry(10, 20, 260, 30)
        name = QtWidgets.QComboBox(group)
        name.setGeometry(10, 60, 350, 30)
        btnDelete = QtWidgets.QPushButton(group)
        btnDelete.setGeometry(365, 60, 100, 30)
        btnDelete.setText("Delete item")
        group.hide()
        btn_close = QtWidgets.QPushButton(widget)
        btn_close.setGeometry(400, 220, 99, 30)
        btn_close.setText("Cancel")
        btn_close.clicked.connect(widget.close)

        def toggle_groupbox():
            group.show()
            sql.connectDB()
            lbltxt = selected.currentText()
            if lbltxt == "":
                del_action.setText("")
            else:
                item = lbltxt.rstrip("s")
                if item == "Categorie":
                    i = "category"
                else:
                    i = item.lower()
                del_action.setText("Select " + i + " to delete:")
            del_action.show()

            if lbltxt == "Products":
                string = "products"
                item_name = "product_name"
            elif lbltxt == "Users":
                string = "users"
                item_name = "username"
            elif lbltxt == "Categories":
                string = "categories"
                item_name = "name"
            elif lbltxt == "Creditors":
                string = "creditors"
                item_name = "creditor_name"
            elif lbltxt == "Debtors":
                string = "debts"
                item_name = "customer_name"
            elif lbltxt == "Suppliers":
                string = "suppliers"
                item_name = "name"
            elif lbltxt == "Supplier Information":
                string = "supplier_info"
                item_name = "name"
            elif lbltxt == "Returns":
                string = "returns"
                item_name = "product_name"
            elif lbltxt == "Customers":
                string = "customers"
                item_name = "name"
            elif lbltxt == "Contacts":
                string = "contacts"
                item_name = "contact_name"
            else:
                string = "logs"
                item_name = "name"

            query = QSqlQuery()
            query.prepare("select {0} from {1}".format(str(item_name), str(string)))
            if query.exec_():
                model = QtSql.QSqlQueryModel()
                model.setQuery(query)
                name.setModel(model)

        def delete():
            lbltxt = selected.currentText()
            if lbltxt == "":
                del_action.setText("")

            sql.connectDB()
            query = QtSql.QSqlQuery()
            if lbltxt == "Products":
                string = "products"
                item_name = "product_name"
            elif lbltxt == "Users":
                string = "users"
                item_name = "username"
            elif lbltxt == "Categories":
                string = "categories"
                item_name = "name"
            elif lbltxt == "Creditors":
                string = "creditors"
                item_name = "creditor_name"
            elif lbltxt == "Debtors":
                string = "debts"
                item_name = "customer_name"
            elif lbltxt == "Suppliers":
                string = "suppliers"
                item_name = "name"
            elif lbltxt == "Supplier Information":
                string = "supplier_info"
                item_name = "name"
            elif lbltxt == "Returns":
                string = "returns"
                item_name = "product_name"
            elif lbltxt == "Customers":
                string = "customers"
                item_name = "name"
            elif lbltxt == "Contacts":
                string = "contacts"
                item_name = "contact_name"
            else:
                string = "logs"
                item_name = "name"

            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Confirm deletion"),
                QtWidgets.qApp.tr("\nAre you sure you want to delete this item?"),
                                              QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)

            if confirm == QtWidgets.QMessageBox.Yes:
                operation = "Deleted " + name.currentText() + " from " + string
                new_log(self.get_current_user(), operation)
                query.prepare("delete from {0} where {1} = '{2}'".format(string, item_name, name.currentText()))
                if query.exec_():
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Deleted Successfully"),
                              QtWidgets.qApp.tr("\n" + name.currentText() + " has been deleted from " + string.capitalize()),
                              QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not able to delete"),
                                                      QtWidgets.qApp.tr("Item couldn't be deleted"),
                                                      QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

        btnDelete.clicked.connect(delete)
        btnContinue.clicked.connect(toggle_groupbox)
        widget.show()


    def help_window(self, MainWindow):
        window = QtWidgets.QDialog(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.setWindowIcon(icon)
        window.setGeometry(450, 150, 450, 180)
        window.setWindowTitle("Permission required")
        window.setStyleSheet("background-color:#dfdfdf;")
        label = QtWidgets.QLabel(window)
        label.setGeometry(10, 15, 440, 80)
        label.setText("Get help about IMS online at the  Bandughana IMS website.\n"
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

    def db_changed(self):
        self.watcher = QtCore.QFileSystemWatcher()
        self.watcher.addPath("ims.db")
        self.watcher.dumpObjectInfo()
        self.watcher.fileChanged.connect(self.update_table(), QtCore.Qt.QueuedConnection)

    def update_table(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        model.setTable("products")
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
        self.tblStockList.setModel(model)
        self.tblStockList.horizontalHeader().setMinimumHeight(50)
        self.tblStockList.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tblStockList.horizontalHeader().setDefaultSectionSize(145)
        self.tblStockList.setMinimumHeight(40)
        self.tblStockList.setStyleSheet(self.stylesheet())
        self.tblStockList.setAlternatingRowColors(True)
        self.tblStockList.setColumnHidden(0, True)
        self.tblStockList.setShowGrid(True)
        self.tblStockList.show()

    def open_support(self):
        self.link = "https://software.bandughana.com/ims/support/"
        webbrowser.open_new(self.link)


    def report_bugs(self):
        self.link = "https://software.bandughana.com/bugs?r_s=ims"
        webbrowser.open_new(self.link)


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        Login.setWindowTitle(self, "Login")
        self.label = QtWidgets.QLabel(self)
        self.label.setStyleSheet("background-color: rgb(0, 85, 127);\ncolor: rgb(255, 255, 255);font-size:16px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Login to continue")
        self.label.setMaximumHeight(50)
        self.username = QtWidgets.QLineEdit(self)
        self.username.setStyleSheet("padding:8px;")
        self.username.setPlaceholderText("Enter Username")
        self.password = QtWidgets.QLineEdit(self)
        self.password.setStyleSheet("padding:8px;")
        self.password.setPlaceholderText("Enter Password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.groupbox = QtWidgets.QGroupBox(self)
        self.groupbox.setFixedHeight(75)
        self.buttonLogin = QtWidgets.QPushButton(self.groupbox)
        self.buttonLogin.setText("Login")
        self.buttonLogin.setGeometry(200, 31, 90, 35)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.btnCancel = QtWidgets.QPushButton(self.groupbox)
        self.btnCancel.setText("Cancel")
        self.btnCancel.setGeometry(20, 31, 90, 35)
        self.btnCancel.clicked.connect(self.close)
        self.lbl_error = QtWidgets.QLabel(self)
        self.lbl_error.setStyleSheet("color:#fff;font-size:14px;background-color:#ee6666;border-radius:3px;padding:10px;")
        self.lbl_error.setGeometry(10, 5, 330, 32)
        self.lbl_error.setMaximumHeight(34)
        self.lbl_error.hide()
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.groupbox)
        layout.setContentsMargins(-25, -25, -40, -35)
        layout.setSpacing(23)
        layout.addWidget(self.lbl_error)

    def handleLogin(self):
        sql.connectDB()
        self.lbl_error.setText("")
        error = 0
        if (self.username.text().isspace() or self.username.text() == '') and (
                self.password.text().isspace() or self.password.text() == ''):
            self.lbl_error.show()
            self.lbl_error.setText("Please enter your username and password.\n")
            error = 1
        elif self.username.text().isspace() or self.username.text() == '':
            self.lbl_error.show()
            self.lbl_error.setText("Please enter your username")
            error = 2
        elif self.password.text().isspace() or self.password.text() == '':
            self.lbl_error.show()
            self.lbl_error.setText("Please enter your password")
            error = 3
        else:
            self.lbl_error.clear()
            user_logged_in = self.username.text()
            password = self.password.text()

            if error == 0:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * from users where username = ? and password = ?")
                query.bindValue(0, user_logged_in)
                query.bindValue(1, password)
                query.exec_()
                if num_rows(query) > 0:
                    self.user_type = str(query.value(6))
                    # time = strftime("%I:%M:%S%p")
                    operation = "Successfully logged in to system"
                    new_log(user_logged_in, operation)
                    self.accept()

                else:
                    self.lbl_error.hide()
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not registered"),
                                               QtWidgets.qApp.tr("\nInvalid user details. Please try again!!"),
                                               QtWidgets.QMessageBox.Abort)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        global Window
        super(Window, self).__init__()
        Window = QtWidgets.QMainWindow()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window.setWindowIcon(icon)
        ui = Ui_MainWindow()
        ui.setupUi(Window)
        ui.actionNewCreditor.triggered.connect(lambda: ui.newCreditor(Window))
        ui.viewCustomers.triggered.connect(lambda: ui.showCustomers(Window))
        ui.actionNewCategory.triggered.connect(lambda: ui.dialogCategory(Window))
        ui.actionViewCustomers.triggered.connect(lambda: ui.showCustomers(Window))
        ui.actionViewAllProducts.triggered.connect(lambda: ui.showProducts(Window))
        ui.viewProduct.triggered.connect(lambda: ui.showProducts(Window))
        ui.newSale.triggered.connect(lambda: ui.addSale(Window))
        ui.toolBar.show()
        ui.actionViewStockOut.triggered.connect(lambda: ui.viewStock(Window))
        ui.logout.triggered.connect(lambda: exchangeWindows(Window))
        ui.quickDelete.triggered.connect(lambda: ui.select_item(Window))
        ui.actionNewProduct.triggered.connect(lambda: ui.newProduct(Window))
        ui.actionViewProductCategories.triggered.connect(lambda: ui.showCat(Window))
        ui.actionPrint.triggered.connect(lambda: ui.printItem(Window, ui.centralWidget))
        ui.actionNewSupplier.triggered.connect(lambda: ui.dialogSupplier(Window))
        ui.actionNewStaff.triggered.connect(lambda: ui.showRegistration(Window))
        ui.actionAboutIMS.triggered.connect(lambda: ui.showAbout(Window))
        ui.actionViewLogs.triggered.connect(lambda: ui.mainLoop(Window))
        ui.actionNewSupplierInfo.triggered.connect(lambda: ui.newSupplier(Window))
        ui.actionViewStoreStatistics.triggered.connect(lambda: ui.get_stats(Window))
        ui.actionExit.triggered.connect(Window.close)
        ui.actionViewCreditors.triggered.connect(lambda: ui.showCreditors(Window))
        ui.new_stock.triggered.connect(lambda: ui.newStock(Window))
        ui.actionViewDebtors.triggered.connect(lambda: ui.showDebtors(Window))
        ui.actionNewDebtor.triggered.connect(lambda: ui.newDebtor(Window))
        ui.viewDebtors.triggered.connect(lambda: ui.showDebtors(Window))
        ui.viewCreditors.triggered.connect(lambda: ui.showCreditors(Window))
        ui.viewSuppliers.triggered.connect(lambda: ui.show_suppliers(Window))
        ui.viewSupplierInfo.triggered.connect(lambda: ui.edit_suppliers(Window))
        ui.actionNewContact.triggered.connect(lambda: ui.dialogContact(Window))
        ui.viewCategories.triggered.connect(lambda: ui.showCat(Window))
        ui.actionViewStaff.triggered.connect(lambda: ui.showUsers(Window))
        ui.actionEditContact.triggered.connect(lambda: ui.showContacts(Window))
        ui.actionViewCompanyInfo.triggered.connect(lambda: ui.show_suppliers(Window))
        ui.actionViewSales.triggered.connect(lambda: ui.view_sales(Window))
        ui.actionNewCustomerInfo.triggered.connect(lambda: ui.newCustomer(Window))
        ui.actionViewContacts.triggered.connect(lambda: ui.showContacts(Window))
        ui.actionProductSupport.triggered.connect(lambda: ui.open_support())
        ui.actionHelp.triggered.connect(lambda: ui.help_window(Window))
        ui.actionBackupData.triggered.connect(lambda: ui.backup(Window))
        ui.actionImportDB.triggered.connect(lambda: ui.import_backup(Window))
        ui.actionReportBugs.triggered.connect(lambda: ui.report_bugs())
        ui.actionEditCategories.triggered.connect(lambda: ui.showCat(Window))
        ui.actionEditProducts.triggered.connect(lambda: ui.edit_product(Window))
        ui.actionNewCreditor.triggered.connect(lambda: ui.newCreditor(Window))
        ui.actionEditCustomerInfo.triggered.connect(lambda: ui.editCustomer(Window))
        ui.actionNewInvoice.triggered.connect(lambda: ui.createInvoice(Window))
        ui.actionEditSupplierInfo.triggered.connect(lambda: ui.edit_suppliers(Window))
        ui.viewReturns.triggered.connect(lambda: ui.showReturns(Window))
        ui.actionViewInvoices.triggered.connect(lambda: ui.viewInvoices(Window))
        ui.newInvoice.triggered.connect(lambda: ui.createInvoice(Window))
        ui.viewSale.triggered.connect(lambda: ui.showSales(Window))
        ui.user.setText(login.username.text().capitalize())
        if login.user_type == "Employee":
            ui.quickDelete.setDisabled(True)
            ui.actionViewStoreStatistics.setDisabled(True)
            ui.actionViewStaff.setDisabled(True)
            ui.actionNewStaff.setDisabled(True)
            ui.actionViewLogs.setDisabled(True)
            ui.actionNewSupplier.setDisabled(True)
            ui.new_stock.setDisabled(True)
            ui.actionViewCompanyInfo.setDisabled(True)



        Window.showMaximized()
        Window.show()


def exchangeWindows(Window):
    Window.close()
    import sys
    global win
    win = QtWidgets.QDialog()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    win.setWindowIcon(icon)
    session = NewSession()
    session.setupUi(win)
    session.setGeometry(250, 250, 250, 150)
    win.setWindowTitle("Start new session")
    session.btnNewLogin.clicked.connect(lambda: init())
    win.show()


def licence_dialog():
    conf = QtWidgets.QDialog()
    conf.setWindowTitle("Enter License Key")
    conf.setModal(True)
    conf.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowContextHelpButtonHint)
    lbl = QtWidgets.QLabel(conf)
    lbl.setText("Enter Licence Key to continue:")
    lbl.setGeometry(20, 20, 310, 35)
    keyin = QtWidgets.QLineEdit(conf)
    keyin.setGeometry(20, 55, 310, 40)
    btnOk = QtWidgets.QPushButton(conf)
    btnOk.setText("Continue")
    btnOk.setGeometry(285, 55, 80, 40)
    btnClose = QtWidgets.QPushButton(conf)
    btnClose.setText("Close")
    btnClose.setGeometry(370, 55, 80, 40)
    btnClose.clicked.connect(conf.close)
    conf.resize(480, 120)
    value = keyin
    def check_empty():
        key = "BA21-N18D-28UG-1H8A-2NA2"
        value = keyin.text()
        if value.isspace() or value == "":
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Licence key required"),
                                           QtWidgets.qApp.tr("Please enter your license key!"),
                                           QtWidgets.QMessageBox.Ok)
        elif value != key:
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Invalid Licence key"),
                                           QtWidgets.qApp.tr("The License key you entered is invalid!"),
                                           QtWidgets.QMessageBox.Ok)
        else:
            sql.connectDB()
            query = QtSql.QSqlQuery()
            query.exec_("insert into license values(?)")
            query.bindValue(0, key)
            if query.exec_():
                conf.accept()

    btnOk.clicked.connect(lambda: check_empty())
    conf.exec_()

def check_key():
    if sql.connectDB():
        if sql.createDB():
            con = sqlite3.connect("ims.db")
            cur = con.cursor()

            key = "BA21-N18D-28UG-1H8A-2NA2"
            cur.execute("select * from license where code = '{0}'".format(key))
            rows = cur.fetchall()
            if len(rows) > 0:
                return len(rows)


def init():
    global log
    log = Login()

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    log.setWindowIcon(icon)
    log.setGeometry(QtCore.QRect(435, 120, 350, 330))
    log.setMaximumWidth(350)
    log.setMaximumHeight(330)

    if log.exec_() == QtWidgets.QDialog.Accepted:
        QtWidgets.QApplication.closeAllWindows()
        Window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(Window)
        ui.actionNewCreditor.triggered.connect(lambda: ui.newCreditor(Window))
        ui.viewCustomers.triggered.connect(lambda: ui.showCustomers(Window))
        ui.actionNewCategory.triggered.connect(lambda: ui.dialogCategory(Window))
        ui.actionViewCustomers.triggered.connect(lambda: ui.showCustomers(Window))
        ui.actionViewAllProducts.triggered.connect(lambda: ui.showProducts(Window))
        ui.viewProduct.triggered.connect(lambda: ui.showProducts(Window))
        ui.toolBar.show()
        ui.logout.triggered.connect(lambda: exchangeWindows(Window))
        ui.quickDelete.triggered.connect(lambda: ui.select_item(Window))
        ui.actionNewProduct.triggered.connect(lambda: ui.newProduct(Window))
        ui.actionViewProductCategories.triggered.connect(lambda: ui.showCat(Window))
        ui.actionPrint.triggered.connect(lambda: ui.printItem(Window, ui.centralWidget))
        ui.actionNewSupplier.triggered.connect(lambda: ui.dialogSupplier(Window))
        ui.actionNewStaff.triggered.connect(lambda: ui.showRegistration(Window))
        ui.actionAboutIMS.triggered.connect(lambda: ui.showAbout(Window))
        ui.actionViewLogs.triggered.connect(lambda: ui.mainLoop(Window))
        ui.actionNewSupplierInfo.triggered.connect(lambda: ui.newSupplier(Window))
        ui.actionViewStoreStatistics.triggered.connect(lambda: ui.get_stats(Window))
        ui.actionExit.triggered.connect(Window.close)
        ui.actionViewCreditors.triggered.connect(lambda: ui.showCreditors(Window))
        ui.new_stock.triggered.connect(lambda: ui.newStock(Window))
        ui.actionViewDebtors.triggered.connect(lambda: ui.showDebtors(Window))
        ui.actionViewStockOut.triggered.connect(lambda: ui.viewStock(Window))
        ui.actionNewDebtor.triggered.connect(lambda: ui.newDebtor(Window))
        ui.viewDebtors.triggered.connect(lambda: ui.showDebtors(Window))
        ui.viewCreditors.triggered.connect(lambda: ui.showCreditors(Window))
        ui.viewSuppliers.triggered.connect(lambda: ui.show_suppliers(Window))
        ui.viewSupplierInfo.triggered.connect(lambda: ui.edit_suppliers(Window))
        ui.actionViewSales.triggered.connect(lambda: ui.view_sales(Window))
        ui.actionNewContact.triggered.connect(lambda: ui.dialogContact(Window))
        ui.newSale.triggered.connect(lambda: ui.addSale(Window))
        ui.viewCategories.triggered.connect(lambda: ui.showCat(Window))
        ui.actionViewStaff.triggered.connect(lambda: ui.showUsers(Window))
        ui.actionEditContact.triggered.connect(lambda: ui.showContacts(Window))
        ui.actionViewCompanyInfo.triggered.connect(lambda: ui.show_suppliers(Window))
        ui.actionNewCustomerInfo.triggered.connect(lambda: ui.newCustomer(Window))
        ui.actionViewContacts.triggered.connect(lambda: ui.showContacts(Window))
        ui.actionProductSupport.triggered.connect(lambda: ui.open_support())
        ui.actionHelp.triggered.connect(lambda: ui.help_window(Window))
        ui.actionBackupData.triggered.connect(lambda: ui.backup(Window))
        ui.actionImportDB.triggered.connect(lambda: ui.import_backup(Window))
        ui.actionReportBugs.triggered.connect(lambda: ui.report_bugs())
        ui.actionEditCategories.triggered.connect(lambda: ui.showCat(Window))
        ui.actionEditProducts.triggered.connect(lambda: ui.edit_product(Window))
        ui.actionNewCreditor.triggered.connect(lambda: ui.newCreditor(Window))
        ui.actionEditCustomerInfo.triggered.connect(lambda: ui.editCustomer(Window))
        ui.actionNewInvoice.triggered.connect(lambda: ui.createInvoice(Window))
        ui.actionEditSupplierInfo.triggered.connect(lambda: ui.edit_suppliers(Window))
        ui.viewReturns.triggered.connect(lambda: ui.showReturns(Window))
        ui.viewSale.triggered.connect(lambda: ui.showSales(Window))
        ui.actionViewInvoices.triggered.connect(lambda: ui.viewInvoices(Window))
        ui.newInvoice.triggered.connect(lambda: ui.createInvoice(Window))
        ui.user.setText(login.username.text().capitalize())
        if login.user_type == "Employee":
            ui.quickDelete.setDisabled(True)
            ui.actionViewStoreStatistics.setDisabled(True)
            ui.actionViewStaff.setDisabled(True)
            ui.actionNewStaff.setDisabled(True)
            ui.actionViewLogs.setDisabled(True)
            ui.actionNewSupplier.setDisabled(True)
            ui.new_stock.setDisabled(True)
            ui.actionViewCompanyInfo.setDisabled(True)

        Window.showMaximized()
        Window.show()



def initialize():
    global login
    login = Login()
    if not check_key():
        if licence_dialog() == QtWidgets.QMessageBox.Accepted:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            login.setWindowIcon(icon)
            login.setGeometry(QtCore.QRect(560, 120, 350, 330))
            login.setMaximumWidth(350)
            login.setMaximumHeight(330)

            if login.exec_() == QtWidgets.QDialog.Accepted:
                login.close()
                Window()
    else:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        login.setGeometry(QtCore.QRect(560, 120, 350, 330))
        login.setMaximumWidth(350)
        login.setMaximumHeight(330)

        if login.exec_() == QtWidgets.QDialog.Accepted:
            login.close()
            Window()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    print(strftime("%", gmtime()))
    initialize()
    sys.exit(app.exec_())