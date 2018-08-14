from PyQt5 import QtSql, QtGui, QtWidgets
from functions import *

db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('ims.db')


def connectDB():
    if not db.open():
        QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Cannot open database"),
                   QtWidgets.qApp.tr("Unable to establish a database connection.\n"
                                     "This example needs SQLite support. Please read "
                                     "the Qt SQL driver documentation for information "
                                     "how to build it.\n\n"
                                     "Click Cancel to exit."), QtWidgets.QMessageBox.Cancel)

        return False

    return True

def createDB():
    if connectDB():
        query = QtSql.QSqlQuery()

        query.exec_("create table if not exists users(id INTEGER AUTO_INCREMENT PRIMARY KEY, name varchar(255), "
                    "password varchar(255), username varchar(25),email varchar(255), phone varchar(15), "
                    "user_type varchar(25),status varchar(25))")

        query.exec_("select * from users where username = 'admin' or username = 'Admin'")

        if num_rows(query) < 1:
            query.exec_("insert into users(name, password, username, email, phone,user_type, status) values('IMS Admin',"
                    "'admin','admin','admin@example.com','0200000000','Admin','Active')")


        query.exec_("create table if not exists invoices(id INTEGER AUTO_INCREMENT PRIMARY KEY,customer_name varchar(255),"
                    "invoice_number varchar(100), product_code varchar(15),product_name varchar(255), sale_price REAL, "
                    "real_price real, amount_paid real, balance real, quantity integer, total real,"
                    " date_bought varchar(25))")

        query.exec_("create table if not exists customers(id INTEGER AUTO_INCREMENT PRIMARY KEY,name varchar(255), "
                    "phone VARCHAR(25), city varchar(255), region varchar(150), gender varchar(25), address TEXT, "
                    "post_office varchar(300), email varchar(225), date_registered varchar(200),remarks varchar(1000))")

        query.exec_("create table if not exists supplier_info(id INTEGER AUTO_INCREMENT PRIMARY KEY,name varchar(255), "
                    "contact VARCHAR(250), city varchar(255), region varchar(150), fax varchar(25), address TEXT, "
                    "postal_zip varchar(300),email varchar(225), registration_no varchar(200),products_instore INTEGER,"
                    "remarks varchar(1000), date_added varchar(25))")

        query.exec_("create table if not exists suppliers(id INTEGER AUTO_INCREMENT PRIMARY KEY,name varchar(255))")

        query.exec_("create table if not exists license(code text)")

        query.exec_("create table if not exists categories(id INTEGER AUTO_INCREMENT PRIMARY KEY,name varchar(255))")

        query.exec_("create table if not exists returns(id INTEGER AUTO_INCREMENT PRIMARY KEY,product_code varchar(200)"
                    ",product_name VARCHAR(250),returnee varchar(255),return_type varchar(150),price REAL,qty INTEGER,"
                    "date_returned varchar(200),reason varchar(1000))")

        query.exec_("create table if not exists debts(id INTEGER AUTO_INCREMENT PRIMARY KEY,customer_name varchar(255),"
                    "phone VARCHAR(25), city varchar(255), area varchar(150), address TEXT, product_name varchar(300), "
                    "amount_paid REAL, amount_owed REAL, total REAL, quantity INTEGER, due_date varchar(100))")

        query.exec_("create table if not exists creditors(id INTEGER AUTO_INCREMENT PRIMARY KEY,"
                    "creditor_name varchar(255),phone VARCHAR(25), product_name varchar(300), amount_paid REAL, "
                    "amount_owed REAL, total REAL, quantity INTEGER, due_date varchar(100))")

        query.exec_("create table if not exists products(id INTEGER AUTO_INCREMENT PRIMARY KEY, product_code TEXT,"
                    "product_name varchar(455),real_price REAL, sale_price REAL, total_price REAL,quantity INTEGER,"
                    "product_category varchar(500), date_added TEXT,supplier varchar(500))")

        query.exec_("create table if not exists sales(id INTEGER AUTO_INCREMENT PRIMARY KEY,customer_name varchar(500),"
                    " product_name varchar(900), amount_paid real, quantity integer, date_bought varchar(500))")

        query.exec_("CREATE TABLE IF NOT EXISTS logs(id INTEGER AUTO_INCREMENT PRIMARY KEY, name VARCHAR(200),"
                    "logged_date VARCHAR(25), operation VARCHAR(1000))")

        query.exec_("CREATE TABLE IF NOT EXISTS contacts(id INTEGER AUTO_INCREMENT PRIMARY KEY, contact_name VARCHAR(200),"
                    "contact_phone VARCHAR(25), date_added VARCHAR(20))")
        
        return True

def closeDB():
    if db.isOpen():
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    if createDB():
        print("Done!")
