import sys
from PyQt5 import QtWidgets
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(QtWidgets.QVBoxLayout(self.centralwidget))

        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.centralwidget.layout().addWidget(self.mdiArea)

        subWindow = QtWidgets.QMdiSubWindow(self)

        widget = QtWidgets.QWidget()
        widget.setLayout(QtWidgets.QVBoxLayout())
        btn = QtWidgets.QPushButton("close", widget)
        widget.layout().addWidget(btn)

        btn.clicked.connect(subWindow.close)

        subWindow.setWidget(widget)
        subWindow.setObjectName("New_Window")
        subWindow.setWindowTitle("New SubWindow")
        self.mdiArea.addSubWindow(subWindow)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
