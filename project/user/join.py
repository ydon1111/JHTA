import sys
import cx_Oracle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Join(object):
    def setupUI(self, HomeWindow):
        # HomeWindow.setFixedSize(400, 450)
        HomeWindow.setWindowTitle("회원가입")
        
        self.centralwidget = QWidget(HomeWindow)
        HomeWindow.setCentralWidget(self.centralwidget)
        
        self.j_ok = QPushButton("회원가입", self.centralwidget)
        self.j_ok.move(100, 350)
        self.j_ok.clicked.connect(lambda : self.ok(HomeWindow))
    
    def ok(self, HomeWindow):
        HomeWindow.start_login()
        
        