# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/logs.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sql
from functions import num_rows

class Ui_Logs(object):
    def setupUi(self, Contacts):
        Contacts.setObjectName("Contacts")
        Contacts.resize(723, 591)
        Contacts.setMaximumSize(QtCore.QSize(723, 591))
        self.groupBox_3 = QtWidgets.QGroupBox(Contacts)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 0, 681, 76))
        self.groupBox_3.setStyleSheet("border:1px solid #ccc;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 30, 171, 51))
        self.groupBox_5.setStyleSheet("border:0;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 68, 17))
        self.label_5.setStyleSheet("border:0;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(310, 10, 31, 20))
        self.label_6.setStyleSheet("border:0;")
        self.label_6.setObjectName("label_6")
        self.startDate = QtWidgets.QLineEdit(self.groupBox_3)
        self.startDate.setGeometry(QtCore.QRect(20, 30, 520, 31))
        self.startDate.setStyleSheet("border:1px solid #999; border-radius:3px;")
        self.startDate.setObjectName("startDate")
        self.btnGetData = QtWidgets.QPushButton(self.groupBox_3)
        self.btnGetData.setGeometry(QtCore.QRect(580, 30, 81, 31))
        self.btnGetData.setStyleSheet("")
        self.btnGetData.setObjectName("btnGetData")
        self.logsView = QtWidgets.QTableView(Contacts)
        self.logsView.setGeometry(QtCore.QRect(20, 170, 681, 371))
        self.logsView.setGridStyle(QtCore.Qt.NoPen)
        self.logsView.setObjectName("logsView")
        self.logsView.horizontalHeader().setDefaultSectionSize(130)
        self.logsView.horizontalHeader().setMinimumSectionSize(100)
        self.logsView.horizontalHeader().setSortIndicatorShown(True)
        self.logsView.horizontalHeader().setStretchLastSection(True)
        self.logsView.verticalHeader().setMinimumSectionSize(30)
        self.groupBox_2 = QtWidgets.QGroupBox(Contacts)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 90, 371, 71))
        self.groupBox_2.setStyleSheet("border:1px solid #ccc;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.usernameFilter = QtWidgets.QComboBox(self.groupBox_2)
        self.usernameFilter.setGeometry(QtCore.QRect(20, 23, 251, 31))
        self.usernameFilter.setObjectName("usernameFilter")
        self.btnLoad = QtWidgets.QPushButton(self.groupBox_2)
        self.btnLoad.setGeometry(QtCore.QRect(280, 23, 71, 31))
        self.btnLoad.setObjectName("btnLoad")
        self.groupBox_4 = QtWidgets.QGroupBox(Contacts)
        self.groupBox_4.setGeometry(QtCore.QRect(410, 90, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("border:1px solid #ccc;")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.btnDelete = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDelete.setGeometry(QtCore.QRect(20, 43, 121, 31))
        self.btnDelete.setObjectName("btnDelete")
        self.selectLog = QtWidgets.QComboBox(self.groupBox_4)
        self.selectLog.setGeometry(QtCore.QRect(20, 10, 251, 27))
        self.selectLog.setObjectName("selectLog")
        self.btnDeleteAll = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDeleteAll.setGeometry(QtCore.QRect(150, 43, 121, 31))
        self.btnDeleteAll.setObjectName("btnDeleteAll")
        self.btnClose = QtWidgets.QPushButton(Contacts)
        self.btnClose.setGeometry(QtCore.QRect(618, 550, 81, 31))
        self.btnClose.setObjectName("btnClose")

        self.btnDeleteAll.clicked.connect(lambda: self.delete_all())
        self.btnDelete.clicked.connect(lambda: self.delete_log())
        self.btnGetData.clicked.connect(lambda: self.get_data())
        self.btnLoad.clicked.connect(lambda: self.get_user_logs())
        self.retranslateUi(Contacts)
        self.btnClose.clicked.connect(Contacts.close)
        QtCore.QMetaObject.connectSlotsByName(Contacts)
        Contacts.setTabOrder(self.startDate, self.btnGetData)
        Contacts.setTabOrder(self.btnGetData, self.usernameFilter)
        Contacts.setTabOrder(self.usernameFilter, self.btnLoad)
        Contacts.setTabOrder(self.btnLoad, self.selectLog)
        Contacts.setTabOrder(self.selectLog, self.btnDelete)
        Contacts.setTabOrder(self.btnDelete, self.btnDeleteAll)
        Contacts.setTabOrder(self.btnDeleteAll, self.logsView)
        Contacts.setTabOrder(self.logsView, self.btnClose)
        sql.connectDB()
        model = QtSql.QSqlQueryModel()
        q = QtSql.QSqlQuery()
        q.exec_("select operation from logs")
        model.setQuery(q)
        self.selectLog.setModel(model)

        qry = QtSql.QSqlQuery()
        qry.prepare("select distinct name from logs")
        qry.exec_()
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(qry)
        self.usernameFilter.setModel(modal)
        self.get_logs()

    def retranslateUi(self, Contacts):
        _translate = QtCore.QCoreApplication.translate
        Contacts.setWindowTitle(_translate("Contacts", "Activity Logs"))
        self.label_5.setText(_translate("Contacts", "Date:"))
        self.btnGetData.setText(_translate("Contacts", "Get Data"))
        self.groupBox_2.setTitle(_translate("Contacts", "Filter by username"))
        self.btnLoad.setText(_translate("Contacts", "Load"))
        self.btnDelete.setText(_translate("Contacts", "Delete Selected"))
        self.btnDeleteAll.setText(_translate("Contacts", "Delete All Logs"))
        self.btnClose.setText(_translate("Contacts", "Close"))

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

    def get_logs(self):
        sql.connectDB()
        global model
        model = QtSql.QSqlTableModel()
        model.setTable("logs")
        model.select()
        model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "User")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Date")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Operation")
        self.logsView.setModel(model)
        qry = QtSql.QSqlQuery()
        qry.prepare("select distinct name from logs")
        qry.exec_()
        modal = QtSql.QSqlQueryModel()
        modal.setQuery(qry)
        self.usernameFilter.setModel(modal)
        self.logsView.setColumnHidden(0, True)
        self.logsView.show()

    def get_data(self):
        sql.connectDB()
        qry = QtSql.QSqlQuery()
        start_date = self.startDate.text()
        qry.prepare("select * from logs where logged_date = ?")
        qry.bindValue(0, start_date)
        qry.exec_()
        modl = QtSql.QSqlTableModel()
        modl.setQuery(qry)
        modl.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        modl.setHeaderData(1, QtCore.Qt.Horizontal, "User")
        modl.setHeaderData(2, QtCore.Qt.Horizontal, "Date")
        modl.setHeaderData(3, QtCore.Qt.Horizontal, "Operation")
        self.selectLog.setModel(modl)
        self.selectLog.setModelColumn(3)
        self.usernameFilter.setModel(modl)
        self.usernameFilter.setModelColumn(1)
        self.logsView.setModel(modl)
        self.logsView.setColumnHidden(0, True)
        self.logsView.show()

    def get_user_logs(self):
        sql.connectDB()
        qry = QtSql.QSqlQuery()
        start_date = self.startDate.text()
        qry.prepare("select * from logs where name = ?")
        qry.bindValue(0, self.usernameFilter.currentText())
        qry.exec_()
        modl = QtSql.QSqlTableModel()
        modl.setQuery(qry)
        modl.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        modl.setHeaderData(1, QtCore.Qt.Horizontal, "User")
        modl.setHeaderData(2, QtCore.Qt.Horizontal, "Date")
        modl.setHeaderData(3, QtCore.Qt.Horizontal, "Operation")
        self.selectLog.setModel(modl)
        self.selectLog.setModelColumn(3)
        self.usernameFilter.setModel(modl)
        self.usernameFilter.setModelColumn(1)
        self.logsView.setModel(modl)
        self.logsView.setColumnHidden(0, True)
        self.logsView.show()

    def delete_all(self):
        sql.connectDB()
        querry = QtSql.QSqlQuery()
        querry.exec_("select name from logs")
        if num_rows(querry) > 0:
            ask = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Confirm"),
                                                 QtWidgets.qApp.tr("\nAre you sure you want to delete all logs?"),
                                                 QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            if ask == QtWidgets.QMessageBox.Yes:
                query = QtSql.QSqlQuery()
                if query.exec_("delete from logs"):
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Deleted successfully"),
                                        QtWidgets.qApp.tr("\nAll logs have been deleted!"),QtWidgets.QMessageBox.Close)
                    self.get_logs()
        else:
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Logs empty"),
                                           QtWidgets.qApp.tr("\nThere are no logs available to delete"),
                                           QtWidgets.QMessageBox.Ok)

    def delete_log(self):
        sql.connectDB()
        querry = QtSql.QSqlQuery()
        querry.exec_("select name from logs")
        if not len(self.selectLog.currentText()) < 5 or not self.selectLog.currentText().isspace() or \
                not self.selectLog.currentText() != '':
            ask = QtWidgets.QMessageBox.question(None, QtWidgets.qApp.tr("Confirm delete"),
                                                 QtWidgets.qApp.tr("\nAre you sure you want to delete this activity log?"),
                                                 QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            if ask == QtWidgets.QMessageBox.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("delete from logs where operation = ?")
                query.bindValue(0, self.selectLog.currentText())
                if query.exec_():
                    self.get_logs()
                    QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Deleted successfully"),
                                        QtWidgets.qApp.tr("\nThe log has been successfully deleted"),
                                        QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, QtWidgets.qApp.tr("Logs empty"),
                                           QtWidgets.qApp.tr("\nPlease select a log to delete"),
                                           QtWidgets.QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Contacts = QtWidgets.QDialog()
    ui = Ui_Logs()
    ui.setupUi(Contacts)
    Contacts.show()
    sys.exit(app.exec_())

