import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import random


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Interface"
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Interface")
        self.setGeometry(200, 50, 750, 650)

        code = QLabel("Your Code")
        message_returned = QLabel("Message Returned")

        code_edit = QLineEdit()
        message_returned_edit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(code, 1, 0)
        grid.addWidget(code_edit, 1, 1)

        grid.addWidget(message_returned, 6, 0)
        grid.addWidget(message_returned_edit, 4, 1, 5, 1)

        self.setLayout(grid)


        """submit_button = QPushButton("Submit", self)
                submit_button.setToolTip("Submit to check your code")
                submit_button.clicked.connect(self.on_click)
                submit_button_h = QHBoxLayout()
                submit_button_h.addStretch(1)
                submit_button_h.addWidget(submit_button)
                submit_button_v = QVBoxLayout()
                submit_button_v.addStretch(1)
                submit_button_v.addLayout(submit_button_h)
                self.setLayout(submit_button_v)"""

        submit_button = QPushButton("Submit", self)
        submit_button.setToolTip("Submit to check your code")
        submit_button.move(600, 500)
        submit_button.clicked.connect(self.on_click)

        label = QLabel("interface system", self)
        label.move(350, 25)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)

        self.m = PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(750, 650)

        """main_menu = self.menuBar()

        file_menu = main_menu.addMenu('File')
        exit_button = QAction(QIcon('exit24.png'), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)

        open_button = QAction(QIcon('open24.png'), 'Open', self)
        open_button.setShortcut('Ctrl+O')
        open_button.setStatusTip('Open File')
        open_button.triggered.connect(self.open_file)
        file_menu.addAction(open_button)

        save_button = QAction(QIcon('save24.png'), 'Save', self)
        save_button.setShortcut('Ctrl+S')
        save_button.setStatusTip('Save File')
        # save_button.triggered.connect(self.save)
        file_menu.addAction(save_button)

        print_button = QAction(QIcon('print24.png'), 'Print', self)
        print_button.setShortcut('Ctrl+P')
        print_button.setStatusTip('Print')
        # print_button.triggered.connect(self.print)
        file_menu.addAction(print_button)

        edit_menu = main_menu.addMenu('Edit')

        undo_button = QAction(QIcon('undo24.png'), 'Undo', self)
        undo_button.setShortcut('Ctrl+Z')
        undo_button.setStatusTip('Undo last change')
        # undo_button.triggered.connect(self.undoStack.undo)
        edit_menu.addAction(undo_button)

        redo_button = QAction(QIcon('redo24.png'), 'Redo', self)
        redo_button.setShortcut('Ctrl+Y')
        redo_button.setStatusTip('Redo last change')
        # redo_button.triggered.connect(self.redo)
        edit_menu.addAction(redo_button)

        clear_button = QAction(QIcon('clear24.png'), 'Clear all', self)
        clear_button.setShortcut('Ctrl+z')
        clear_button.setStatusTip('Clear all')
        # clear_button.triggered.connect(self.clear)
        edit_menu.addAction(clear_button)

        copy_button = QAction(QIcon('copy24.png'), 'Copy', self)
        copy_button.setShortcut('Ctrl+C')
        copy_button.setStatusTip('Copy')
        edit_menu.addAction(copy_button)

        view_menu = main_menu.addMenu('View')
        search_menu = main_menu.addMenu('Search')
        tools_menu = main_menu.addMenu('Tools')
        help_menu = main_menu.addMenu('Help')"""


        self.show()

    @pyqtSlot()
    def on_click(self):
        print("Submitted")

    def open_file(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'w')
        self.editor()
        with file:
            text = file.write()
            self.textEdit.setText(text)


"""class code_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(440, 240))
        self.setWindowTitle("Code")
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("You can write your code in here.\n")
        self.b.move(10, 10)
        self.b.resize(400, 200)"""


class PaintWidget(QWidget):
    def paint_event(self):
        qp = QPainter(self)
        qp.setPen(Qt.black)
        size = self.size()
        for i in range(1024):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    """window = QtWidgets.QApplication(sys.argv)
    main_window = code_window()
    main_window.show()"""
    sys.exit(app.exec_())


"""closing_options = QMessageBox.question(self, 'PyQt5 message', "Do you want to save your changes?",
                                               QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
                                               | QMessageBox.Cancel, QMessageBox.Save)

        if exit_button.triggered.connect(self.close):
            print(int(closing_options))
            if closing_options == QMessageBox.Save:
                print("Saved")
            if closing_options == QMessageBox.Discard:
                print("Discarded")
            elif closing_options == QMessageBox.Cancel:
                print("Cancelled")"""