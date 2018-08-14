from PyQt5.QtCore import QFileSystemWatcher, Qt
from PyQt5 import QtSql, QtWidgets, QtCore
import sql
import sqlite3
from functions import num_rows

# class FileWatcher(object):
#     def db_changed(self):
#         self.watcher = QFileSystemWatcher(self)
#         self.watcher.addPath("ims.db")
#         self.watcher.fileChanged.connect(self.show_popup, Qt.QueuedConnection)
#
#     def show_popup(self):
#         print("Database has been changed")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    licence_dialog()
    sys.exit(app.exec_())