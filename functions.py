from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from time import strftime, gmtime
from customers import *
import sys
import os

def num_rows(query):
    import sql
    if sql.db.driver().hasFeature(QtSql.QSqlDriver.QuerySize):
        num_rows = query.size()
    else:
        query.last()
        num_rows = query.at() + 1
    return num_rows

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def new_log(user, operation):
    day = strftime("%d/%m/%Y", gmtime())
    time = strftime("%I:%M:%S%p")
    sql.connectDB()
    query = QtSql.QSqlQuery()
    query.prepare("insert into logs(name, logged_date, operation) values(?,?,?)")
    query.bindValue(0,user)
    query.bindValue(1, day)
    query.bindValue(2, operation + " at " + time)
    if query.exec_():
        print("Successfully logged...")
    else:
        print(query.lastError().text())

def addExcelSheet(self, sheet):
    for currentColumn in range(self.tableWidget.columnCount()):
        for currentRow in range(self.tableWidget.rowCount()):
            try:
                teext = str(self.tableWidget.item(currentRow, currentColumn).text())
                sheet.write(currentRow, currentColumn, teext)
            except AttributeError:
                pass