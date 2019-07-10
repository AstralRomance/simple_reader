from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import sys

from m_win import *

import fb_parser


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.prs = fb_parser.Parser()

        self.ui.change_book.clicked.connect(self.prs.parse_res)




if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
