from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5 import QtWidgets
import sys
from bs4 import BeautifulSoup as bs
import requests as req


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 100, 840, 940)
        self.setWindowTitle("Music Query")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Music Prompt")
        self.label.move(10, 10)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Clickable")
        self.button.clicked.connect(self.clicked)
        self.button.move(50, 50)

    def clicked(self):
        self.label.setText("Pressed!")
