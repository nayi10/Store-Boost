# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'returns.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql, sqlite3
from formreturn import *
class Ui_Returns(object):
    def setupUi(self, Returns):
        Returns.setObjectName("Returns")
        Returns.resize(919, 600)
        Returns.setMaximumSize(QtCore.QSize(1024, 615))
        self.groupBox = QtWidgets.QGroupBox(Returns)
        self.groupBox.setGeometry(QtCore.QRect(250, -10, 641, 91))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.search = QtWidgets.QLineEdit(self.groupBox)
        self.search.setGeometry(QtCore.QRect(20, 40, 250, 31))
        self.search.setObjectName("search")
        self.btnSearch = QtWidgets.QPushButton(self.groupBox)
        self.btnSearch.setGeometry(QtCore.QRect(270, 40, 75, 31))
        self.btnSearch.setObjectName("btnSearch")
        self.btnNewReturn = QtWidgets.QPushButton(self.groupBox)
        self.btnNewReturn.setGeometry(QtCore.QRect(360, 40, 125, 31))
        self.btnNewReturn.setStyleSheet("")
        self.btnNewReturn.setObjectName("btnNewReturn")
        self.btnEdit = QtWidgets.QPushButton(self.groupBox)
        self.btnEdit.setGeometry(QtCore.QRect(500, 40, 125, 31))
        self.btnEdit.setStyleSheet("")
        self.btnEdit.setObjectName("btnEdit")
        self.returnView = QtWidgets.QTableView(Returns)
        self.returnView.setGeometry(QtCore.QRect(250, 80, 641, 441))
        self.returnView.setObjectName("returnView")
        self.btnClose = QtWidgets.QPushButton(Returns)
        self.btnClose.setGeometry(QtCore.QRect(790, 530, 99, 41))
        self.btnClose.setObjectName("btnClose")
        self.formGroupBox = QtWidgets.QGroupBox(Returns)
        self.formGroupBox.setGeometry(QtCore.QRect(30, -10, 201, 531))
        self.formGroupBox.setTitle("")
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.formGroupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.productCode = QtWidgets.QLineEdit(self.formGroupBox)
        self.productCode.setObjectName("productCode")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.productCode)
        self.label = QtWidgets.QLabel(self.formGroupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.productName = QtWidgets.QLineEdit(self.formGroupBox)
        self.productName.setObjectName("productName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.productName)
        self.label_2 = QtWidgets.QLabel(self.formGroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.returnee = QtWidgets.QLineEdit(self.formGroupBox)
        self.returnee.setObjectName("returnee")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.returnee)
        self.label_3 = QtWidgets.QLabel(self.formGroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.returnType = QtWidgets.QLineEdit(self.formGroupBox)
        self.returnType.setObjectName("returnType")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.returnType)
        self.label_4 = QtWidgets.QLabel(self.formGroupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.price = QtWidgets.QLineEdit(self.formGroupBox)
        self.price.setObjectName("price")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.price)
        self.label_7 = QtWidgets.QLabel(self.formGroupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.quantity = QtWidgets.QLineEdit(self.formGroupBox)
        self.quantity.setObjectName("quantity")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.quantity)
        self.label_8 = QtWidgets.QLabel(self.formGroupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.returnDate = QtWidgets.QLineEdit(self.formGroupBox)
        self.returnDate.setObjectName("returnDate")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.returnDate)
        self.label_5 = QtWidgets.QLabel(self.formGroupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.reason = QtWidgets.QTextEdit(self.formGroupBox)
        self.reason.setMaximumSize(QtCore.QSize(146, 80))
        self.reason.setObjectName("reason")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.reason)
        self.btnUpdate = QtWidgets.QPushButton(Returns)
        self.btnUpdate.setGeometry(QtCore.QRect(57, 534, 151, 41))
        self.btnUpdate.setObjectName("btnUpdate")
        self.choose = QtWidgets.QComboBox(Returns)
        self.choose.setGeometry(QtCore.QRect(220, 534, 220, 40))
        self.choose.setObjectName("choose")
        self.btnNewEdit = QtWidgets.QPushButton(Returns)
        self.btnNewEdit.setGeometry(QtCore.QRect(445, 534, 121, 40))
        self.btnNewEdit.setObjectName("btnNewEdit")
        self.btnDelete = QtWidgets.QPushButton(Returns)
        self.btnDelete.setGeometry(QtCore.QRect(570, 534, 125, 40))
        self.btnDelete.setStyleSheet("")
        self.btnDelete.setObjectName("btnDelete")
        self.btnUpdate.setDisabled(True)
        self.update_view()

        self.retranslateUi(Returns)
        QtCore.QMetaObject.connectSlotsByName(Returns)

    def update_view(self):
        sql.connectDB()
        model = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        query.exec_("Select distinct product_code, product_name from returns")
        model.setQuery(query)
        self.choose.setModel(model)
        self.choose.setModelColumn(1)
        comp = QtWidgets.QCompleter()
        comp.setModel(model)
        comp.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        comp.setFilterMode(QtCore.Qt.MatchContains)
        comp.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.productCode.setCompleter(comp)
        complet = QtWidgets.QCompleter()
        complet.setFilterMode(QtCore.Qt.MatchContains)
        complet.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        complet.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        qery = QtSql.QSqlQuery()
        qery.exec_("select * from returns")
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(qery)
        self.search.setCompleter(complet)
        complet.setModel(modal)
        self.search.textChanged.connect(lambda: self.get_return())

        self.formGroupBox.setDisabled(True)

    def retranslateUi(self, Returns):
        _translate = QtCore.QCoreApplication.translate
        Returns.setWindowTitle(_translate("Returns", "Ahasaniya Enterprice | Returns"))
        self.btnSearch.setText(_translate("Returns", "Search"))
        self.btnDelete.setText(_translate("Returns", "Delete Selected"))
        self.btnNewReturn.setText(_translate("Returns", "New Return"))
        self.btnEdit.setText(_translate("Returns", "Edit Returns"))
        self.btnClose.setText(_translate("Returns", "Close"))
        self.label_9.setText(_translate("Returns", "Product Code:"))
        self.label.setText(_translate("Returns", "ProductName:"))
        self.label_2.setText(_translate("Returns", "Returnee:"))
        self.label_3.setText(_translate("Returns", "Type:"))
        self.label_4.setText(_translate("Returns", "Price:"))
        self.label_7.setText(_translate("Returns", "Quantity:"))
        self.label_8.setText(_translate("Returns", "Date:"))
        self.label_5.setText(_translate("Returns", "Reason:"))
        self.btnUpdate.setText(_translate("Returns", "Update"))
        self.btnNewEdit.setText(_translate("Returns", "Edit Selected"))

    def new_return(self, w):
        FormReturns = QtWidgets.QDialog(w)
        self.ui = Ui_FormReturns()
        self.ui.setupUi(FormReturns)
        self.ui.btnSave.clicked.connect(self.ui.validate)
        FormReturns.show()

    def display_returns(self):
        sql.connectDB()
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("returns")
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Product Code")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Product Name")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Returnee")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Return Type")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Price")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Quantity")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Date")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Reason")
        self.model.select()
        self.returnView.setModel(self.model)
        self.returnView.horizontalHeader().setMinimumHeight(40)
        self.returnView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.returnView.horizontalHeader().setDefaultSectionSize(120)
        self.returnView.setColumnWidth(8, 400)
        self.returnView.setColumnHidden(0, True)
        self.returnView.show()

    def showMessage(self):
        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Notice"), QtWidgets.qApp.tr("Please select from "
                                            "return chooser below and click <b>Edit selected</b> to edit the selected return."))
    def populate_fileds(self):
        connection = sqlite3.connect("ims.db")
        if connection:
            self.cursor = connection.cursor()
            self.cursor.execute("select * from returns where product_name = '{0}'".format(
                str(self.choose.currentText())))
            rows = self.cursor.fetchall()

            if rows:
                self.formGroupBox.setEnabled(True)
                self.productName.setText(rows[0][2])
                self.productCode.setText(rows[0][1])
                self.returnee.setText(str(rows[0][3]))
                self.returnType.setText(str(rows[0][4]))
                self.price.setText(str(rows[0][5]))
                self.quantity.setText(str(rows[0][6]))
                self.returnDate.setText(rows[0][7])
                self.reason.setPlainText(rows[0][8])
                self.btnUpdate.setEnabled(True)
                sql.connectDB()
                model = QtSql.QSqlQueryModel()
                query = QtSql.QSqlQuery()
                query.exec_("Select distinct product_name from returns")
                model.setQuery(query)
                self.choose.setModel(model)
            else:
                self.formGroupBox.setDisabled(True)
                self.btnUpdate.setDisabled(True)

    def del_row(self):
        if sql.connectDB():
            q = QtSql.QSqlQuery()
            q.prepare("delete from returns where product_name = ?")
            q.bindValue(0, self.choose.currentText())
            if q.exec_():
                self.update_view()
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Return deleted!"),
                                                  QtWidgets.qApp.tr("\n The return has been deleted successfully"),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Return not deleted!"),
                                                  QtWidgets.qApp.tr("Return couldn't be deleted"),
                                                  QtWidgets.QMessageBox.Ok)

    def delete_record(self):
        dlg = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Sure to delete?"),
                                    QtWidgets.qApp.tr("\nAre you sure you want delete this item?"),
                                    QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Cancel)

        if dlg == QtWidgets.QMessageBox.Yes:
            self.del_row()


    def update_records(self):
        self.update_view()
        if sql.connectDB():
            query = QtSql.QSqlQuery()
            query.prepare(
                "UPDATE returns SET product_code = ?,product_name = ?, returnee = ?, return_type = ?, price = ?,"
                "qty = ?, date_returned = ?, reason = ? WHERE product_name = ?")
            query.bindValue(0, self.productCode.text())
            query.bindValue(1, self.productName.text())
            query.bindValue(2, self.returnee.text())
            query.bindValue(3, self.returnType.text())
            query.bindValue(4, self.price.text())
            query.bindValue(5, self.quantity.text())
            query.bindValue(6, self.returnDate.text())
            query.bindValue(7, self.reason.toPlainText())
            query.bindValue(8, self.choose.currentText())
            if query.exec_():
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Updated Successfully"),
                                                  QtWidgets.qApp.tr("\nInformation has been successfully updated"),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Not Updated"),
                                                  QtWidgets.qApp.tr("Data update not successful"),
                                                  QtWidgets.QMessageBox.Ok)


    def get_return(self):
        sql.connectDB()
        if not self.search.text() == '' or not self.search.text().isspace():
            qry = QtSql.QSqlQuery()
            qry.prepare("select * from returns where product_code LIKE '%{0}%' or product_name LIKE '%{0}%' or returnee "
            "LIKE '%{0}%' or date_returned LIKE '%{0}%' or return_type LIKE '%{0}%'".format(str(self.search.text())))
            print(qry.lastError().text())
            if qry.exec_():
                self.model = QtSql.QSqlQueryModel()
                self.model.setQuery(qry)
                self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
                self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Product Code")
                self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Product Name")
                self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Returnee")
                self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Return Type")
                self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Price")
                self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Quantity")
                self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Date")
                self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Reason")
                self.returnView.setModel(self.model)
                self.returnView.horizontalHeader().setMinimumHeight(40)
                self.returnView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.returnView.setColumnHidden(0, True)
                self.returnView.show()
                self.returnView.setModel(self.model)
                self.returnView.setColumnHidden(0, True)
                self.returnView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.returnView.show()
                sql.closeDB()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Returns = QtWidgets.QDialog()
    ui = Ui_Returns()
    ui.setupUi(Returns)
    ui.display_returns()
    Returns.show()
    sys.exit(app.exec_())

