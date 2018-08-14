from PyQt5 import QtWidgets, QtSql, QtCore
import sql

class QuickDelete(object):
    def setupUi(self, QuickDelete):
        self.widget = QtWidgets.QDialog(QuickDelete)
        self.widget.setGeometry(30 / 100 * QuickDelete.width(), 0.3 * QuickDelete.height(), 550, 300)
        self.widget.setWindowTitle("Choose self.item to delete")
        self.widget = QtWidgets.QLabel(self.widget)
        self.widget.setText("Select self.item category:")
        self.widget.setGeometry(20, 20, 150, 30)
        self.widget.show()
        self.selected = QtWidgets.QComboBox(self.widget)
        self.selected.setGeometry(172, 20, 250, 30)
        self.meta = ["Products", "Users", "Categories", "Debtors", "Suppliers", "Creditors", "Contacts", "Customers",
                "Returns",
                "Logs", "Supplier Information"]
        _translate = QtCore.QCoreApplication.translate
        self.selected.addItems(self.meta)
        self.selected.show()
        self.btnContinue = QtWidgets.QPushButton(self.widget)
        self.btnContinue.setGeometry(425, 20, 90, 30)
        self.btnContinue.setText("Continue")
        self.btnContinue.show()
        self.group = QtWidgets.QGroupBox(self.widget)
        self.group.setGeometry(20, 60, 499, 100)
        self.del_action = QtWidgets.QLabel(self.group)
        self.del_action.setGeometry(10, 20, 260, 30)
        self.name = QtWidgets.QComboBox(self.group)
        self.name.setGeometry(10, 60, 350, 30)
        self.btnDelete = QtWidgets.QPushButton(self.group)
        self.btnDelete.setGeometry(365, 60, 100, 30)
        self.btnDelete.setText("Delete self.item")
        self.group.hide()
        self.btn_close = QtWidgets.QPushButton(self.widget)
        self.btn_close.setGeometry(400, 220, 99, 45)
        self.btn_close.setText("Cancel")
        self.btn_close.clicked.connect(self.widget.close)

        QtCore.QMetaObject.connectSlotsByName(QuickDelete)

    def toggle_groupbox(self):
        self.group.show()
        sql.connectDB()
        self.lbltxt = self.selected.currentText()
        if self.lbltxt == "":
            self.del_action.setText("")
        else:
            self.item = self.lbltxt.rstrip("s")
            if self.item == "Categorie":
                i = "category"
            else:
                i = self.item.lower()
            self.del_action.setText("Select " + i + " to delete:")
        self.del_action.show()

        if self.lbltxt == "Products":
            string = "products"
            self.item_name = "product_name"
        elif self.lbltxt == "Users":
            string = "users"
            self.item_name = "username"
        elif self.lbltxt == "Categories":
            string = "categories"
            self.item_name = "name"
        elif self.lbltxt == "Creditors":
            string = "creditors"
            self.item_name = "creditor_name"
        elif self.lbltxt == "Debtors":
            string = "debts"
            self.item_name = "customer_name"
        elif self.lbltxt == "Suppliers":
            string = "suppliers"
            self.item_name = "name"
        elif self.lbltxt == "Supplier Information":
            string = "supplier_info"
            self.item_name = "name"
        elif self.lbltxt == "Returns":
            string = "returns"
            self.item_name = "product_name"
        elif self.lbltxt == "Customers":
            string = "customers"
            self.item_name = "name"
        elif self.lbltxt == "Contacts":
            string = "contacts"
            self.item_name = "contact_name"
        else:
            string = "logs"
            self.item_name = "name"

        query = QtSql.QSqlQuery()
        query.prepare("select {0} from {1}".format(str(self.item_name), str(string)))
        if query.exec_():
            model = QtSql.QSqlQueryModel()
            model.setQuery(query)
            self.name.setModel(model)

    def delete_record(self):
        self.lbltxt = self.selected.currentText()
        if self.lbltxt == "":
            self.del_action.setText("")

        sql.connectDB()
        query = QtSql.QSqlQuery()
        if self.lbltxt == "Products":
            string = "products"
            self.item_name = "product_name"
        elif self.lbltxt == "Users":
            string = "users"
            self.item_name = "username"
        elif self.lbltxt == "Categories":
            string = "categories"
            self.item_name = "name"
        elif self.lbltxt == "Creditors":
            string = "creditors"
            self.item_name = "creditor_name"
        elif self.lbltxt == "Debtors":
            string = "debts"
            self.item_name = "customer_name"
        elif self.lbltxt == "Suppliers":
            string = "suppliers"
            self.item_name = "name"
        elif self.lbltxt == "Supplier Information":
            string = "supplier_info"
            self.item_name = "name"
        elif self.lbltxt == "Returns":
            string = "returns"
            self.item_name = "product_name"
        elif self.lbltxt == "Customers":
            string = "customers"
            self.item_name = "name"
        elif self.lbltxt == "Contacts":
            string = "contacts"
            self.item_name = "contact_name"
        else:
            string = "logs"
            self.item_name = "name"

        def confirm(i):
            if i.text() == "&OK":
                if sql.connectDB():
                    q = QtSql.QSqlQuery()
                    q.prepare("delete from ? where ? = ?")
                    q.bindValue(0, string)
                    q.bindValue(1, self.item_name)
                    q.bindValue(2, self.name.currentText())
                    if q.exec_():
                        QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Deleted Successfully"),
                                                          QtWidgets.qApp.tr(
                                                              "\n" + self.name.currentText() + " has been deleted from " + string.capitalize()),
                                                          QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)
                    else:
                        QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Not able to delete"),
                                                       QtWidgets.qApp.tr("self.item couldn't be deleted"),
                                                       QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

        dlg = QtWidgets.QMessageBox()
        dlg.setIcon(QtWidgets.QMessageBox.Question)
        dlg.setWindowTitle("Sure to delete?")
        dlg.setInformativeText("Are you sure you want delete this self.item?")
        dlg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        dlg.buttonClicked.connect(lambda: confirm())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete = QtWidgets.QDialog()
    ui = QuickDelete()
    ui.setupUi(delete)
    delete.show()
    sys.exit(app.exec_())


