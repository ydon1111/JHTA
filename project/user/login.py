import sys
from user.join import *
from main.main import *
from common.DBconnect import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Login():
    def setupUI(self, HomeWindow):
        # HomeWindow.setFixedSize(400, 450)
        HomeWindow.setWindowTitle("로그인")
        
        self.centralwidget = QWidget(HomeWindow)
        HomeWindow.setCentralWidget(self.centralwidget)
        # HomeWindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        
        self.initUI(HomeWindow)
        
    def initUI (self, HomeWindow):
        self.l_label_id = QLabel("ID", self.centralwidget)
        self.l_label_id.move(50, 150)
        self.l_label_pw = QLabel("PW", self.centralwidget)
        self.l_label_pw.move(50, 250)

        # QLineEdit 
        self.l_le_id = QLineEdit(self.centralwidget)
        self.l_le_id.move(150, 150)
        self.l_le_pw = QLineEdit(self.centralwidget)
        self.l_le_pw.setEchoMode(QLineEdit.Password)
        self.l_le_pw.move(150, 250)
        

        self.l_login_btn = QPushButton("로그인", self.centralwidget)
        self.l_login_btn.move(50, 350)
        self.l_join_btn  = QPushButton("회원가입", self.centralwidget)
        self.l_join_btn.move(250, 350)
        
        self.l_login_btn.clicked.connect(lambda : self.login(HomeWindow))
        self.l_join_btn.clicked.connect(HomeWindow.start_join)
        
    def login(self, HomeWindow):
        res = excute("select * from SM_USER_TB where USER_ID = :id and USER_PW = :pw", [self.l_le_id.text(), self.l_le_pw.text()])
        if len(res) > 0 :
            HomeWindow.start_main()
        else:
            QMessageBox.question(self.centralwidget, "로그인", "아이디 혹은 비밀번호를 확인하세요.", QMessageBox.Yes, QMessageBox.Yes)
        