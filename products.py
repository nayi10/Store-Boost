# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'products.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql

class Ui_Products(object):
    def setupUi(self, Products):
        Products.setObjectName("Products")
        Products.resize(1205, 605)
        self.groupBox_2 = QtWidgets.QGroupBox(Products)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 30, 391, 61))
        self.groupBox_2.setStyleSheet("border:1px solid #999;\n"
"border-radius: 3px;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.search = QtWidgets.QLineEdit(self.groupBox_2)
        self.search.setGeometry(QtCore.QRect(10, 24, 271, 25))
        self.search.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly)
        self.search.setObjectName("search")
        self.btnSearch = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSearch.setGeometry(QtCore.QRect(290, 24, 81, 27))
        self.btnSearch.setObjectName("btnSearch")
        self.tableView = QtWidgets.QTableView(Products)
        self.tableView.setGeometry(QtCore.QRect(30, 100, 1141, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableView.setLineWidth(1)
        self.tableView.setMidLineWidth(0)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setIconSize(QtCore.QSize(0, 0))
        self.tableView.setShowGrid(False)
        self.tableView.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(150)
        self.groupOne = QtWidgets.QGroupBox(Products)
        self.groupOne.setGeometry(QtCore.QRect(430, 30, 741, 55))
        self.groupOne.setStyleSheet("border:1px solid #999;\n"
"border-radius: 3px;")
        self.groupOne.setTitle("")
        self.groupOne.setObjectName("groupBox_3")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.selectedProduct = QtWidgets.QComboBox(self.groupOne)
        self.selectedProduct.setGeometry(QtCore.QRect(10, 10, 210, 35))
        self.selectedProduct.setObjectName("selectedProduct")
        self.btnDelete = QtWidgets.QPushButton(self.groupOne)
        self.btnDelete.setGeometry(QtCore.QRect(225, 10, 121, 35))
        self.btnDelete.setObjectName("btnDelete")
        self.btnEdit = QtWidgets.QPushButton(self.groupOne)
        self.btnEdit.setGeometry(QtCore.QRect(360, 10, 111, 35))
        self.btnEdit.setObjectName("btnEdit")
        self.btnDeleteAll = QtWidgets.QPushButton(self.groupOne)
        self.btnDeleteAll.setGeometry(QtCore.QRect(580, 10, 150, 35))
        self.btnDeleteAll.setObjectName("btnDeleteAll")
        self.btnClose = QtWidgets.QPushButton(Products)
        self.btnClose.setGeometry(QtCore.QRect(1050, 550, 121, 41))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(Products)
        sql.connectDB()
        complet = QtWidgets.QCompleter()
        complet.setFilterMode(QtCore.Qt.MatchContains)
        complet.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        complet.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        qery = QtSql.QSqlQuery()
        qery.exec_("select product_name from products")
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(qery)
        self.search.setCompleter(complet)
        complet.setModel(modal)
        self.btnClose.clicked.connect(Products.close)
        self.btnDeleteAll.clicked.connect(self.delete_all)
        self.btnDelete.clicked.connect(self.delete_record)
        self.search.textChanged.connect(lambda: self.search_products())
        QtCore.QMetaObject.connectSlotsByName(Products)
        self.update_view()
        self.selectProducts()

    def update_view(self):
        sql.connectDB()
        model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        query.exec_("select distinct product_name from products")
        model.setQuery(query)
        if model.rowCount() > 0:
            self.btnDelete.setEnabled(True)
            self.selectedProduct.setModel(model)
        else:
            self.btnDelete.setDisabled(True)
            
    def retranslateUi(self, Products):
        _translate = QtCore.QCoreApplication.translate
        Products.setWindowTitle(_translate("Products", "Products"))
        self.groupBox_2.setTitle(_translate("Products", "Search products by name"))
        self.btnSearch.setText(_translate("Products", "Search"))
        self.btnDelete.setText(_translate("Products", "Delete Seleted"))
        self.btnEdit.setText(_translate("Products", "Edit Product"))
        self.btnDeleteAll.setText(_translate("Products", "Delete All Products"))
        self.btnClose.setText(_translate("Products", "Close"))

    def delete_record(self):
        if sql.connectDB():
            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete?"),
                                                     QtWidgets.qApp.tr("Are you sure you want to delete <b>" +
                                                    self.selectedProduct.currentText() + "</b> from products?"),
                                                     QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if confirm == QtWidgets.QMessageBox.Yes:
                self.update_view()
                self.selectProducts()
                query = QtSql.QSqlQuery()
                query.prepare("delete from products where product_name = ?")
                query.bindValue(0, self.selectedProduct.currentText())
                if query.exec_():
                    self.update_view()
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Product deleted!"),
                                                      QtWidgets.qApp.tr("Product has been deleted"),
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Product not deleted!"),
                                                   QtWidgets.qApp.tr("Product couldn't be deleted"),
                                                   QtWidgets.QMessageBox.Ok)

    def delete_all(self):
        if sql.connectDB():
            confirm = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete products?"),
                                             QtWidgets.qApp.tr("Are you sure you want to delete <b>all</b> products? "
                                            "This will delete all products data!"),
                                             QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if confirm == QtWidgets.QMessageBox.Yes:
                self.update_view()
                self.selectProducts()
                query = QtSql.QSqlQuery()
                query.prepare("truncate products")
                query.bindValue(0, self.selectedProduct.currentText())
                if query.exec_():
                    self.update_view()
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Product deleted!"),
                                                      QtWidgets.qApp.tr("Product has been deleted"),
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Product not deleted!"),
                                                   QtWidgets.qApp.tr("Product couldn't be deleted"),
                                                   QtWidgets.QMessageBox.Ok)

    def selectProducts(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        q = QtSql.QSqlQuery()
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
        self.tableView.setModel(model)
        self.tableView.horizontalHeader().setMinimumHeight(40)
        self.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableView.setShowGrid(True)
        self.tableView.show()


    def search_products(self):

        if not self.search.text() == '' or not self.search.text().isspace():
            qry = QtSql.QSqlQuery()
            qry.prepare("select * from products where product_code LIKE '%{0}%' or product_name LIKE '%{0}%' or "
                        "product_category LIKE '%{0}%' or supplier LIKE '%{0}%' or date_added LIKE '%{0}%'".format(
                str(self.search.text())))
            # qry.bindValue(0, str(self.search.text()))
            if qry.exec_():
                model = QtSql.QSqlQueryModel()
                model.setQuery(qry)
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
                self.tableView.setModel(model)
                self.tableView.horizontalHeader().setMinimumHeight(40)
                self.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.tableView.setShowGrid(True)
                self.tableView.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    products = QtWidgets.QDialog()
    products.setWindowTitle("Products")
    ui = Ui_Products()
    ui.setupUi(products)
    ui.tableView.setColumnHidden(0, True)
    products.setGeometry(40, 20, 1200, 620)
    products.show()
    sys.exit(app.exec_())
