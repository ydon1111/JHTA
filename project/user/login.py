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
        # QLineEdit 
        self.l_le_id = QLineEdit(self.centralwidget)
        self.l_le_id.setPlaceholderText("아이디")
        self.l_le_id.move(700, 370)
        
        self.l_le_pw = QLineEdit(self.centralwidget)
        self.l_le_pw.setPlaceholderText("비밀번호")
        self.l_le_pw.move(700, 420)
        self.l_le_pw.setEchoMode(QLineEdit.Password)
        

        self.l_login_btn = QPushButton("로그인", self.centralwidget)
        self.l_login_btn.move(700, 470)
        self.l_join_btn  = QPushButton("회원가입", self.centralwidget)
        self.l_join_btn.move(815, 470)
        
        self.l_login_btn.clicked.connect(lambda : self.login(HomeWindow))
        self.l_join_btn.clicked.connect(HomeWindow.start_join)
        
        self.l_le_id.setText("user1")
        self.l_le_pw.setText("test")
        self.l_le_id.setFocus()

        self.set_style()
    
    def set_style(self):
        le_style = "font-size: 12pt; width: 200px; height: 30px; color: #1E90FF; border-radius: 3px;"
        btn_style = "font-size: 12pt; width: 80px; height: 30px; color: #FFFFFF; border-style: solid; border-width: 2px; border-color: #FFFFFF; border-radius: 3px; font-weight: bold;"
        
        self.l_le_id.setStyleSheet(le_style)
        self.l_le_pw.setStyleSheet(le_style)
        self.l_login_btn.setStyleSheet(btn_style)
        self.l_join_btn.setStyleSheet(btn_style)
        
    def login(self, HomeWindow):
        if self.l_le_id.text() != "" and self.l_le_id.text() != None and self.l_le_pw.text() != "" and self.l_le_pw.text() != None:
            res = excute("select USER_NO, USER_ID, USER_EMAIL, USER_BIRTH, USER_GENDER, USER_LOC from SM_USER_TB where USER_ID = :id and USER_PW = :pw", [self.l_le_id.text(), self.l_le_pw.text()])
            if len(res) > 0 :
                user_no, id, email, birth, gender, loc = res[0]
                HomeWindow.user_info = {"user_no": user_no, "id": id, "email": email, "birth": birth, "gender": gender, "loc": loc}
                HomeWindow.start_main(int(HomeWindow.user_info["loc"]))
            else:
                QMessageBox.question(self.centralwidget, "로그인", "아이디 혹은 비밀번호를 확인하세요.", QMessageBox.Yes, QMessageBox.Yes)
                self.l_le_pw.setFocus()
        elif self.l_le_id.text() == "" or self.l_le_id.text() == None:
            QMessageBox.question(self.centralwidget, "로그인", "아이디를 입력하세요", QMessageBox.Yes, QMessageBox.Yes)
            self.l_le_id.setFocus()
        elif self.l_le_pw.text() == "" or self.l_le_pw.text() == None:
            QMessageBox.question(self.centralwidget, "로그인", "비밀번호를 입력하세요", QMessageBox.Yes, QMessageBox.Yes)
            self.l_le_pw.setFocus()
            
        