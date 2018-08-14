# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editproduct.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql, sqlite3

class Ui_EditProduct(object):
    def setupUi(self, EditProduct):
        EditProduct.setObjectName("EditProduct")
        EditProduct.resize(516, 530)
        self.label = QtWidgets.QLabel(EditProduct)
        self.label.setGeometry(QtCore.QRect(0, 0, 521, 41))
        EditProduct.setStyleSheet(
            "QLineEdit{"
                "min-height:28px;}"
            "QComboBox{"
                "min-height:28px;}"
            "QPushButton{"
            "background-color:#ededed;color:#111;"
            "min-height:28px;}"
        )
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.product = QtWidgets.QComboBox(EditProduct)
        self.product.setGeometry(QtCore.QRect(150, 56, 301, 27))
        self.product.setObjectName("product")
        self.label_3 = QtWidgets.QLabel(EditProduct)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 111, 17))
        self.label_3.setObjectName("label_3")
        self.btnRefresh = QtWidgets.QPushButton(EditProduct)
        self.btnRefresh.setGeometry(QtCore.QRect(450, 56, 31, 27))
        self.btnRefresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/Apply_16x16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon)
        self.btnRefresh.setObjectName("btnRefresh")
        self.hideBox = QtWidgets.QGroupBox(EditProduct)
        self.hideBox.setEnabled(False)
        self.hideBox.setGeometry(QtCore.QRect(20, 85, 475, 435))
        self.hideBox.setTitle("")
        self.hideBox.setObjectName("hideBox")
        self.lblTotal = QtWidgets.QLabel(self.hideBox)
        self.lblTotal.setGeometry(QtCore.QRect(30, 280, 51, 27))
        self.lblTotal.setObjectName("lblTotal")
        self.lblDate = QtWidgets.QLabel(self.hideBox)
        self.lblDate.setGeometry(QtCore.QRect(250, 280, 41, 27))
        self.lblDate.setObjectName("lblDate")
        self.lblRealPrice = QtWidgets.QLabel(self.hideBox)
        self.lblRealPrice.setGeometry(QtCore.QRect(30, 180, 92, 27))
        self.lblRealPrice.setToolTip("")
        self.lblRealPrice.setProperty("toolTipDuration", 2)
        self.lblRealPrice.setObjectName("lblRealPrice")
        self.lblSalePrice = QtWidgets.QLabel(self.hideBox)
        self.lblSalePrice.setGeometry(QtCore.QRect(30, 230, 81, 27))
        self.lblSalePrice.setObjectName("lblSalePrice")
        self.lblQuantity = QtWidgets.QLabel(self.hideBox)
        self.lblQuantity.setGeometry(QtCore.QRect(30, 130, 64, 27))
        self.lblQuantity.setObjectName("lblQuantity")
        self.realPrice = QtWidgets.QLineEdit(self.hideBox)
        self.realPrice.setGeometry(QtCore.QRect(130, 180, 311, 27))
        self.realPrice.setObjectName("realPrice")
        self.productCode = QtWidgets.QLineEdit(self.hideBox)
        self.productCode.setGeometry(QtCore.QRect(140, 80, 301, 27))
        self.productCode.setObjectName("productCode")
        self.productName = QtWidgets.QLineEdit(self.hideBox)
        self.productName.setGeometry(QtCore.QRect(140, 30, 301, 27))
        self.productName.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.productName.setObjectName("productName")
        self.lblProductName = QtWidgets.QLabel(self.hideBox)
        self.lblProductName.setGeometry(QtCore.QRect(30, 30, 102, 27))
        self.lblProductName.setObjectName("lblProductName")
        self.btnSave = QtWidgets.QPushButton(self.hideBox)
        self.btnSave.setGeometry(QtCore.QRect(310, 394, 81, 31))
        self.btnSave.setObjectName("btnSave")
        self.quantity = QtWidgets.QLineEdit(self.hideBox)
        self.quantity.setGeometry(QtCore.QRect(100, 130, 121, 27))
        self.quantity.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.quantity.setObjectName("quantity")
        self.total = QtWidgets.QLineEdit(self.hideBox)
        self.total.setGeometry(QtCore.QRect(70, 280, 171, 27))
        self.total.setObjectName("total")
        self.lblSupplier = QtWidgets.QLabel(self.hideBox)
        self.lblSupplier.setGeometry(QtCore.QRect(30, 330, 61, 27))
        self.lblSupplier.setObjectName("lblSupplier")
        self.btnAddSupplier = QtWidgets.QPushButton(self.hideBox)
        self.btnAddSupplier.setGeometry(QtCore.QRect(400, 330, 41, 27))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddSupplier.setFont(font)
        self.btnAddSupplier.setStyleSheet("color:#000")
        self.btnAddSupplier.setAutoDefault(True)
        self.btnAddSupplier.setDefault(False)
        self.btnAddSupplier.setObjectName("btnAddSupplier")
        self.lblProductCode = QtWidgets.QLabel(self.hideBox)
        self.lblProductCode.setGeometry(QtCore.QRect(30, 80, 111, 27))
        self.lblProductCode.setObjectName("lblProductCode")
        self.category = QtWidgets.QComboBox(self.hideBox)
        self.category.setGeometry(QtCore.QRect(310, 130, 131, 27))
        self.category.setObjectName("category")
        self.supplier = QtWidgets.QComboBox(self.hideBox)
        self.supplier.setGeometry(QtCore.QRect(104, 330, 281, 27))
        self.supplier.setObjectName("supplier")
        self.salePrice = QtWidgets.QLineEdit(self.hideBox)
        self.salePrice.setGeometry(QtCore.QRect(130, 230, 311, 27))
        self.salePrice.setObjectName("salePrice")
        self.btnCancel = QtWidgets.QPushButton(self.hideBox)
        self.btnCancel.setGeometry(QtCore.QRect(60, 394, 99, 31))
        self.btnCancel.setObjectName("btnCancel")
        self.dateAdded = QtWidgets.QDateEdit(self.hideBox)
        self.dateAdded.setGeometry(QtCore.QRect(300, 280, 141, 27))
        self.dateAdded.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dateAdded.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.dateAdded.setMinimumDate(QtCore.QDate(2018, 6, 20))
        self.dateAdded.setCalendarPopup(True)
        self.dateAdded.setObjectName("dateAdded")
        self.label_2 = QtWidgets.QLabel(self.hideBox)
        self.label_2.setGeometry(QtCore.QRect(240, 134, 68, 17))
        self.label_2.setObjectName("label_2")
        self.btnCancel.clicked.connect(EditProduct.close)
        self.hideBox.hide()
        self.retranslateUi(EditProduct)
        QtCore.QMetaObject.connectSlotsByName(EditProduct)

    def retranslateUi(self, EditProduct):
        _translate = QtCore.QCoreApplication.translate
        EditProduct.setWindowTitle(_translate("EditProduct", "Edit Product"))
        self.label.setText(_translate("EditProduct", "Edit Product"))
        self.label_3.setText(_translate("EditProduct", "Select product:"))
        self.lblTotal.setText(_translate("EditProduct", "Total:"))
        self.lblDate.setText(_translate("EditProduct", "Date:"))
        self.lblRealPrice.setText(_translate("EditProduct", "Real Price:"))
        self.lblSalePrice.setText(_translate("EditProduct", "Sale Price:"))
        self.lblQuantity.setText(_translate("EditProduct", "Quantity:"))
        self.lblProductName.setText(_translate("EditProduct", "Product Name:"))
        self.btnSave.setText(_translate("EditProduct", "Save"))
        self.lblSupplier.setText(_translate("EditProduct", "Supplier:"))
        self.btnAddSupplier.setToolTip(_translate("EditProduct", "Add new supplier"))
        self.btnAddSupplier.setText(_translate("EditProduct", "+"))
        self.lblProductCode.setText(_translate("EditProduct", "Product Code:"))
        self.btnCancel.setText(_translate("EditProduct", "Cancel"))
        self.label_2.setText(_translate("EditProduct", "Category:"))

        sql.connectDB()
        self.model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        self.hideBox.setDisabled(True)
        query.prepare("SELECT DISTINCT product_name FROM products")
        if query.exec_():
            self.hideBox.setEnabled(True)
            self.model.setQuery(query)
            self.product.setModel(self.model)
            self.btnRefresh.setEnabled(True)
        else:
            self.btnRefresh.setDisabled(True)

    def populate_fileds(self):
        self.hideBox.show()
        connection = sqlite3.connect("ims.db")
        if connection:
            self.cursor = connection.cursor()
            self.cursor.execute("select * from products where product_name = '{0}'".format(
                str(self.product.currentText())))
            rows = self.cursor.fetchall()
            model = QtSql.QSqlQueryModel()
            qry = QtSql.QSqlQuery()
            qry.exec_("select distinct name from categories")
            model.setQuery(qry)
            mod = QtSql.QSqlQueryModel()
            q = QtSql.QSqlQuery()
            q.exec_("select distinct name from suppliers")
            mod.setQuery(q)

            if rows:
                self.productName.setText(rows[0][2])
                self.productCode.setText(rows[0][1])
                self.realPrice.setText(str(rows[0][3]))
                self.salePrice.setText(str(rows[0][4]))
                self.total.setText(str(rows[0][5]))
                self.quantity.setText(str(rows[0][6]))
                self.category.setModel(model)
                self.dateAdded.setCalendarPopup(True)
                self.supplier.setModel(mod)
            else:
                self.hideBox.hide()
                self.btnCancel.show()

    def validate(self):
        error = 0
        if (self.productName.text() == '' or self.productName.text().isspace()) or (self.productCode.text() == '' or
                                                                       self.productCode.text().isspace()) or (
                self.realPrice.text() == '' or self.realPrice.text().isspace()) and \
                (self.salePrice.text() == '' or self.salePrice.text().isspace()) or (self.category.currentText() == '' or
                                                                            self.category.currentText().isspace()) or (
                self.dateAdded.text() == '' or self.dateAdded.text().isspace()) and \
                (self.self.supplier.currentText() == '' or self.self.supplier.currentText().isspace()) or (
                self.quantity.text() == '' or self.quantity.text().isspace()) or (self.total.text() == '' or
                                                                                   self.total.text().isspace()):
            error = 1

        if error == 0:
            self.update_records()
        else:
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("There are blank fields"),
                                           QtWidgets.qApp.tr(
                                               "\nPlease all fields are required, make sure to fill them"),
                                           QtWidgets.QMessageBox.Ok)

    def update_records(self):
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            query.prepare(
                "UPDATE products SET product_code = ?,product_name = ?,real_price = ?,sale_price = ?, total_price = ?,"
                "quantity = ?, product_category = ?, date_added = ?, supplier = ? WHERE product_name = ?")
            query.bindValue(0, self.productCode.text())
            query.bindValue(1, self.productName.text())
            query.bindValue(2, self.realPrice.text())
            query.bindValue(3, self.salePrice.text())
            query.bindValue(4, self.total.text())
            query.bindValue(5, self.quantity.text())
            query.bindValue(6, self.category.currentText())
            query.bindValue(7, self.dateAdded.date())
            query.bindValue(8, self.supplier.currentText())
            query.bindValue(9, self.product.currentText())
            if query.exec_():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Updated Successfully"),
                                                  QtWidgets.qApp.tr("\nProduct has been successfully edited"),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Updated"),
                                                  QtWidgets.qApp.tr("Data update not successful"),
                                                  QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditProduct = QtWidgets.QDialog()
    ui = Ui_EditProduct()
    ui.setupUi(EditProduct)
    ui.btnRefresh.clicked.connect(ui.populate_fileds)
    ui.btnSave.clicked.connect(ui.validate)
    EditProduct.show()
    sys.exit(app.exec_())

