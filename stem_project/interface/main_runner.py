import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from stem_project.interface.test_ui import Ui_MainWindow


class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()
