# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/suppliers.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
import sqlite3


class Ui_SupplierInfo(object):
    def setupUi(self, SupplierInfo):
        SupplierInfo.setObjectName("SupplierInfo")
        SupplierInfo.resize(796, 663)
        self.tabSupplierInfo = QtWidgets.QWidget()
        self.tabSupplierInfo.setObjectName("tabSupplierInfo")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabSupplierInfo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.search = QtWidgets.QLineEdit(self.tabSupplierInfo)
        self.search.setStyleSheet("min-height:25px;\n"
"min-width:410px;")
        self.search.setObjectName("search")
        self.gridLayout_2.addWidget(self.search, 0, 0, 1, 1)
        self.btnSearch = QtWidgets.QPushButton(self.tabSupplierInfo)
        self.btnSearch.setStyleSheet("min-height:25px;\n"
"max-width:80px;")
        self.btnSearch.setObjectName("btnSearch")
        self.gridLayout_2.addWidget(self.btnSearch, 0, 1, 1, 1)
        self.btnCancel = QtWidgets.QPushButton(self.tabSupplierInfo)
        self.btnCancel.setStyleSheet("min-height:25px;\n"
"max-width:80px;")
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout_2.addWidget(self.btnCancel, 0, 2, 1, 1)
        self.btnNew = QtWidgets.QPushButton(self.tabSupplierInfo)
        self.btnNew.setStyleSheet("min-height:25px;\n"
"max-width:120px;")
        self.btnNew.setObjectName("btnNew")
        self.gridLayout_2.addWidget(self.btnNew, 0, 3, 1, 1)
        self.supplierView = QtWidgets.QTableView(self.tabSupplierInfo)
        self.supplierView.setObjectName("supplierView")
        self.gridLayout_2.addWidget(self.supplierView, 1, 0, 1, 4)
        SupplierInfo.addTab(self.tabSupplierInfo, "")
        self.tabEditSupplier = QtWidgets.QWidget()
        self.tabEditSupplier.setObjectName("tabEditSupplier")
        self.gridLayout = QtWidgets.QGridLayout(self.tabEditSupplier)
        self.gridLayout.setObjectName("gridLayout")
        self.groupSupplier = QtWidgets.QGroupBox(self.tabEditSupplier)
        self.groupSupplier.setStyleSheet("border:1px solid #ccc;")
        self.groupSupplier.setTitle("")
        self.groupSupplier.setObjectName("groupSupplier")
        self.label_2 = QtWidgets.QLabel(self.groupSupplier)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 51, 17))
        self.label_2.setStyleSheet("border:0;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupSupplier)
        self.label_3.setGeometry(QtCore.QRect(380, 23, 61, 17))
        self.label_3.setStyleSheet("border:0;")
        self.label_3.setObjectName("label_3")
        self.contact = QtWidgets.QLineEdit(self.groupSupplier)
        self.contact.setGeometry(QtCore.QRect(450, 19, 231, 28))
        self.contact.setObjectName("contact")
        self.label_4 = QtWidgets.QLabel(self.groupSupplier)
        self.label_4.setGeometry(QtCore.QRect(20, 74, 41, 17))
        self.label_4.setStyleSheet("border:0;")
        self.label_4.setObjectName("label_4")
        self.city = QtWidgets.QLineEdit(self.groupSupplier)
        self.city.setGeometry(QtCore.QRect(60, 70, 241, 27))
        self.city.setObjectName("city")
        self.label_5 = QtWidgets.QLabel(self.groupSupplier)
        self.label_5.setGeometry(QtCore.QRect(330, 77, 51, 17))
        self.label_5.setStyleSheet("border:0;")
        self.label_5.setObjectName("label_5")
        self.region = QtWidgets.QLineEdit(self.groupSupplier)
        self.region.setGeometry(QtCore.QRect(390, 73, 291, 27))
        self.region.setObjectName("region")
        self.label_6 = QtWidgets.QLabel(self.groupSupplier)
        self.label_6.setGeometry(QtCore.QRect(20, 136, 31, 17))
        self.label_6.setStyleSheet("border:0;")
        self.label_6.setObjectName("label_6")
        self.fax = QtWidgets.QLineEdit(self.groupSupplier)
        self.fax.setGeometry(QtCore.QRect(60, 130, 311, 27))
        self.fax.setObjectName("fax")
        self.label_7 = QtWidgets.QLabel(self.groupSupplier)
        self.label_7.setGeometry(QtCore.QRect(390, 130, 67, 17))
        self.label_7.setStyleSheet("border:0;")
        self.label_7.setObjectName("label_7")
        self.address = QtWidgets.QTextEdit(self.groupSupplier)
        self.address.setGeometry(QtCore.QRect(390, 150, 291, 71))
        self.address.setObjectName("address")
        self.label_8 = QtWidgets.QLabel(self.groupSupplier)
        self.label_8.setGeometry(QtCore.QRect(20, 194, 111, 17))
        self.label_8.setStyleSheet("border:0;")
        self.label_8.setObjectName("label_8")
        self.postalAddress = QtWidgets.QLineEdit(self.groupSupplier)
        self.postalAddress.setGeometry(QtCore.QRect(130, 190, 221, 27))
        self.postalAddress.setObjectName("postalAddress")
        self.label_9 = QtWidgets.QLabel(self.groupSupplier)
        self.label_9.setGeometry(QtCore.QRect(20, 250, 151, 17))
        self.label_9.setStyleSheet("border:0;")
        self.label_9.setObjectName("label_9")
        self.registrationNumber = QtWidgets.QLineEdit(self.groupSupplier)
        self.registrationNumber.setGeometry(QtCore.QRect(180, 246, 191, 27))
        self.registrationNumber.setObjectName("registrationNumber")
        self.label_11 = QtWidgets.QLabel(self.groupSupplier)
        self.label_11.setGeometry(QtCore.QRect(20, 305, 121, 17))
        self.label_11.setStyleSheet("border:0;")
        self.label_11.setObjectName("label_11")
        self.productsInStore = QtWidgets.QLineEdit(self.groupSupplier)
        self.productsInStore.setGeometry(QtCore.QRect(150, 300, 231, 27))
        self.productsInStore.setObjectName("productsInStore")
        self.label_13 = QtWidgets.QLabel(self.groupSupplier)
        self.label_13.setGeometry(QtCore.QRect(20, 350, 231, 17))
        self.label_13.setStyleSheet("border:0;")
        self.label_13.setObjectName("label_13")
        self.remarks = QtWidgets.QTextEdit(self.groupSupplier)
        self.remarks.setGeometry(QtCore.QRect(20, 370, 661, 75))
        self.remarks.setObjectName("remarks")
        self.name = QtWidgets.QLineEdit(self.groupSupplier)
        self.name.setGeometry(QtCore.QRect(70, 16, 281, 27))
        self.name.setObjectName("name")
        self.btnUpdate = QtWidgets.QPushButton(self.groupSupplier)
        self.btnUpdate.setGeometry(QtCore.QRect(430, 460, 251, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")
        self.email = QtWidgets.QLineEdit(self.groupSupplier)
        self.email.setGeometry(QtCore.QRect(470, 250, 211, 27))
        self.email.setObjectName("email")
        self.label_10 = QtWidgets.QLabel(self.groupSupplier)
        self.label_10.setGeometry(QtCore.QRect(420, 255, 41, 17))
        self.label_10.setStyleSheet("border:0;")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.groupSupplier)
        self.label_12.setGeometry(QtCore.QRect(400, 310, 91, 17))
        self.label_12.setStyleSheet("border:0;")
        self.label_12.setObjectName("label_12")
        self.dateAdded = QtWidgets.QLineEdit(self.groupSupplier)
        self.dateAdded.setGeometry(QtCore.QRect(500, 305, 181, 27))
        self.dateAdded.setObjectName("dateAdded")
        self.gridLayout.addWidget(self.groupSupplier, 1, 0, 1, 4)
        self.btnLoad = QtWidgets.QPushButton(self.tabEditSupplier)
        self.btnLoad.setStyleSheet("min-height:25px;\n"
"max-width:100px;")
        self.btnLoad.setObjectName("btnLoad")
        self.gridLayout.addWidget(self.btnLoad, 0, 2, 1, 1)
        self.btnExit = QtWidgets.QPushButton(self.tabEditSupplier)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet("min-height:25px;\n"
"max-width:90px;")
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 0, 3, 1, 1)
        self.supplierChoose = QtWidgets.QComboBox(self.tabEditSupplier)
        self.supplierChoose.setStyleSheet("min-height:25px;\n"
"max-width:410px;")
        self.supplierChoose.setObjectName("supplierChoose")
        self.gridLayout.addWidget(self.supplierChoose, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tabEditSupplier)
        self.label.setMaximumSize(QtCore.QSize(120, 30))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        SupplierInfo.addTab(self.tabEditSupplier, "")
        sql.connectDB()
        complet = QtWidgets.QCompleter()
        complet.setFilterMode(QtCore.Qt.MatchContains)
        complet.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        complet.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        qery = QtSql.QSqlQuery()
        qery.exec_("SELECT * FROM supplier_info")
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(qery)
        self.search.setCompleter(complet)
        complet.setModel(modal)
        self.model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        self.search.textChanged.connect(lambda: self.search_suppliers())
        self.groupSupplier.hide()
        query.prepare("SELECT DISTINCT name FROM supplier_info")
        if query.exec_():
            self.model.setQuery(query)
            self.supplierChoose.setModel(self.model)
            self.btnLoad.setEnabled(True)
        else:
            self.btnLoad.setDisabled(True)

        self.retranslateUi(SupplierInfo)
        SupplierInfo.setCurrentIndex(0)
        self.btnCancel.clicked.connect(SupplierInfo.close)
        self.get_suppliers()
        self.btnLoad.clicked.connect(lambda: self.populate_fileds())
        self.btnSearch.clicked.connect(lambda: self.search_suppliers())
        self.btnCancel.clicked.connect(SupplierInfo.close)
        self.btnExit.clicked.connect(SupplierInfo.close)
        self.btnUpdate.clicked.connect(self.update_records)
        QtCore.QMetaObject.connectSlotsByName(SupplierInfo)

    def retranslateUi(self, SupplierInfo):
        _translate = QtCore.QCoreApplication.translate
        SupplierInfo.setWindowTitle(_translate("SupplierInfo", "Supplier Information"))
        self.btnSearch.setText(_translate("SupplierInfo", "Search"))
        self.btnCancel.setText(_translate("SupplierInfo", "Cancel"))
        self.btnNew.setText(_translate("SupplierInfo", "New Supplier"))
        SupplierInfo.setTabText(SupplierInfo.indexOf(self.tabSupplierInfo), _translate("SupplierInfo", "Supplier Info"))
        self.label.setText(_translate("SupplierInfo", "Select supplier:"))
        self.btnLoad.setText(_translate("SupplierInfo", "Load Details"))
        self.label_2.setText(_translate("SupplierInfo", "Name:"))
        self.label_3.setText(_translate("SupplierInfo", "Contact:"))
        self.label_4.setText(_translate("SupplierInfo", "City:"))
        self.label_5.setText(_translate("SupplierInfo", "Region:"))
        self.label_6.setText(_translate("SupplierInfo", "Fax:"))
        self.label_7.setText(_translate("SupplierInfo", "Address:"))
        self.label_8.setText(_translate("SupplierInfo", "Postal Address:"))
        self.label_9.setText(_translate("SupplierInfo", "Registration Number:"))
        self.label_11.setText(_translate("SupplierInfo", "Products in store:"))
        self.label_13.setText(_translate("SupplierInfo", "Remarks about this supplier:"))
        self.btnUpdate.setText(_translate("SupplierInfo", "Update Supplier Information"))
        self.label_10.setText(_translate("SupplierInfo", "Email:"))
        self.label_12.setText(_translate("SupplierInfo", "Date Added:"))
        self.btnExit.setText(_translate("SupplierInfo", "Exit"))
        SupplierInfo.setTabText(SupplierInfo.indexOf(self.tabEditSupplier), _translate("SupplierInfo", "Edit Supplier"))

    def populate_fileds(self):
        self.groupSupplier.show()
        connection = sqlite3.connect("ims.db")
        if connection:
            self.cursor = connection.cursor()
            self.cursor.execute(
                "select * from supplier_info where name = '{0}'".format(str(self.supplierChoose.currentText())))
            rows = self.cursor.fetchall()
            if rows:
                self.name.setText(rows[0][1])
                self.contact.setText(rows[0][2])
                self.city.setText(rows[0][3])
                self.region.setText(rows[0][4])
                self.fax.setText(rows[0][5])
                self.address.setPlainText(rows[0][6])
                self.postalAddress.setText(rows[0][7])
                self.registrationNumber.setText(rows[0][8])
                self.email.setText(rows[0][9])
                self.productsInStore.setText(str(rows[0][10]))
                self.remarks.setPlainText(rows[0][11])
                self.dateAdded.setText(rows[0][12])
            else:
                self.groupSupplier.hide()

    def update_records(self):
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            query.prepare(
                "UPDATE supplier_info SET name = ?, contact = ?, city = ?, region = ?, fax = ?, address = ?, "
                "postal_zip = ?, email = ?, registration_no = ?, products_instore = ?, remarks = ?, date_added = ? "
                "WHERE name = ?")
            query.bindValue(0, self.name.text())
            query.bindValue(1, self.contact.text())
            query.bindValue(2, self.city.text())
            query.bindValue(3, self.region.text())
            query.bindValue(4, self.fax.text())
            query.bindValue(5, self.address.toPlainText())
            query.bindValue(6, self.postalAddress.text())
            query.bindValue(7, self.email.text())
            query.bindValue(8, self.registrationNumber.text())
            query.bindValue(9, self.productsInStore.text())
            query.bindValue(10, self.remarks.toPlainText())
            query.bindValue(11, self.dateAdded.text())
            query.bindValue(12, self.supplierChoose.currentText())
            query.exec_()
            if query.numRowsAffected() == 1:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Updated Successfully"),
                                                  QtWidgets.qApp.tr("\nSupplier has been successfully updated"),
                                                  QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Updated"),
                                                  QtWidgets.qApp.tr("Data update not successful"),
                                                  QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

    def get_suppliers(self):
        sql.connectDB()
        model = QtSql.QSqlTableModel()
        q = QtSql.QSqlQuery()
        model.setTable("supplier_info")
        model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Contact")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "City")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Region")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Fax")
        model.setHeaderData(6, QtCore.Qt.Horizontal, "Address")
        model.setHeaderData(7, QtCore.Qt.Horizontal, "Postal/Zip")
        model.setHeaderData(8, QtCore.Qt.Horizontal, "Email")
        model.setHeaderData(9, QtCore.Qt.Horizontal, "Registration No.")
        model.setHeaderData(10, QtCore.Qt.Horizontal, "No. of Products")
        model.setHeaderData(11, QtCore.Qt.Horizontal, "Remarks")
        model.setHeaderData(12, QtCore.Qt.Horizontal, "Date Added")
        model.select()
        self.supplierView.setModel(model)
        self.supplierView.horizontalHeader().setMinimumHeight(40)
        self.supplierView.horizontalHeader().setDefaultSectionSize(120)
        self.supplierView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.supplierView.setColumnHidden(0, True)
        self.supplierView.setShowGrid(True)
        self.supplierView.show()

    def search_suppliers(self):

        if not self.search.text() == '' or not self.search.text().isspace():
            qry = QtSql.QSqlQuery()
            qry.prepare("select * from supplier_info where id LIKE '%{0}%' or name LIKE '%{0}%' or "
                        "city LIKE '%{0}%' or region LIKE '%{0}%' or date_added LIKE '%{0}%' or email LIKE '%{0}%'"
                        " or postal_zip LIKE '%{0}%' or contact LIKE '%{0}%' or registration_no LIKE '%{0}%'".format(
                str(self.search.text())))
            # qry.bindValue(0, str(self.search.text()))
            if qry.exec_():
                model = QtSql.QSqlQueryModel()
                model.setQuery(qry)
                model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
                model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
                model.setHeaderData(2, QtCore.Qt.Horizontal, "Contact")
                model.setHeaderData(3, QtCore.Qt.Horizontal, "City")
                model.setHeaderData(4, QtCore.Qt.Horizontal, "Region")
                model.setHeaderData(5, QtCore.Qt.Horizontal, "Fax")
                model.setHeaderData(6, QtCore.Qt.Horizontal, "Address")
                model.setHeaderData(7, QtCore.Qt.Horizontal, "Postal/Zip")
                model.setHeaderData(8, QtCore.Qt.Horizontal, "Email")
                model.setHeaderData(9, QtCore.Qt.Horizontal, "Registration No.")
                model.setHeaderData(10, QtCore.Qt.Horizontal, "No. of Products")
                model.setHeaderData(11, QtCore.Qt.Horizontal, "Remarks")
                model.setHeaderData(12, QtCore.Qt.Horizontal, "Date Added")
                self.supplierView.setModel(model)
                self.supplierView.horizontalHeader().setMinimumHeight(40)
                self.supplierView.horizontalHeader().setDefaultSectionSize(120)
                self.supplierView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.supplierView.setColumnHidden(0, True)
                self.supplierView.setShowGrid(True)
                self.supplierView.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SupplierInfo = QtWidgets.QTabWidget()
    ui = Ui_SupplierInfo()
    ui.setupUi(SupplierInfo)
    ui.get_suppliers()
    ui.btnLoad.clicked.connect(ui.populate_fileds)
    ui.btnSearch.clicked.connect(ui.search_suppliers)
    SupplierInfo.show()
    sys.exit(app.exec_())

