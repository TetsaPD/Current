from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5 import QtWidgets
import sys
from bs4 import BeautifulSoup as bs
import requests as req
import QtClass


def main_app():
    app = QApplication(sys.argv)
    win = QtClass.MyWindow()

    win.show()
    sys.exit(app.exec_())


main_app()
