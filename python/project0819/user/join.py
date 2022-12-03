import sys
# sys.path.insert(0, 'E:/dev/python_workspace/project')

import re
from datetime import datetime
from common.DBconnect import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Join(object):
    def setupUI(self, HomeWindow):
        # HomeWindow.setFixedSize(400, 450)
        # 변수 선언
        self.chk_id = False
        self.ori_id = ""
        self.chk_email = False
        self.ori_email = ""
        
        HomeWindow.setWindowTitle("회원가입")
        
        self.centralwidget = QWidget(HomeWindow)
        HomeWindow.setCentralWidget(self.centralwidget)
        
        self.initUI(HomeWindow)
        
    def initUI (self, HomeWindow):
        # 컬럼 QLabel
        self.j_label_id = QLabel("아이디", self.centralwidget)
        self.j_label_id.move(50, 50)
        self.j_label_pw = QLabel("비밀번호", self.centralwidget)
        self.j_label_pw.move(50, 100)
        self.j_label_pw = QLabel("비밀번호 확인", self.centralwidget)
        self.j_label_pw.move(50, 150)
        self.j_label_email = QLabel("이메일", self.centralwidget)
        self.j_label_email.move(50, 200)
        self.j_label_birth = QLabel("생년월일", self.centralwidget)
        self.j_label_birth.move(50, 250)
        self.j_label_gender = QLabel("성별", self.centralwidget)
        self.j_label_gender.move(50, 300)
        
        # 경고 메시지 QLabel
        self.j_label_msg = QLabel("", self.centralwidget)
        self.j_label_msg.move(50, 350)
        self.j_label_msg.resize(300, 100)
        self.j_label_msg.setStyleSheet("color: red;")

        # 컬럼 QLineEdit 
        self.j_le_id = QLineEdit(self.centralwidget)
        self.j_le_id.move(150, 50)
        self.j_dchk_id = QPushButton("중복확인", self.centralwidget)
        self.j_dchk_id.move(300, 50)
        self.j_dchk_id.clicked.connect(lambda : self.double_chk("ID", self.j_le_id.text()))
        
        self.j_le_pw = QLineEdit(self.centralwidget)
        self.j_le_pw.move(150, 100)
        self.j_le_pwc = QLineEdit(self.centralwidget)
        self.j_le_pwc.move(150, 150)
        
        self.j_le_email = QLineEdit(self.centralwidget)
        self.j_le_email.move(150, 200)
        self.j_dchk_email = QPushButton("중복확인", self.centralwidget)
        self.j_dchk_email.move(300, 200)
        self.j_dchk_email.clicked.connect(lambda : self.double_chk("EMAIL", self.j_le_id.text()))
        
        self.j_le_birth = QDateEdit(self.centralwidget)
        self.j_le_birth.move(150, 250)
        self.j_le_birth.setDate(QDate.currentDate())
        self.j_le_birth.setMinimumDate(QDate(1900, 1, 1))
        self.j_le_birth.setMaximumDate(QDate(datetime.today().year, datetime.today().month, datetime.today().day))
        
        self.j_le_gender1 = QRadioButton('남자', self.centralwidget)
        self.j_le_gender1.move(150, 300)
        self.j_le_gender1.setChecked(True)
        
        self.j_le_gender2 = QRadioButton('여자', self.centralwidget)
        self.j_le_gender2.move(200, 300)
        
        self.j_sign_up = QPushButton("회원가입", self.centralwidget)
        self.j_sign_up.move(50, 450)
        self.j_sign_up.clicked.connect(lambda : self.sign_up(HomeWindow))
        
        self.j_sign_up = QPushButton("취소", self.centralwidget)
        self.j_sign_up.move(200, 450)
        self.j_sign_up.clicked.connect(HomeWindow.start_login)
        
        self.j_le_id.setFocus()
        
    def double_chk(self, type, type_data):
        res = excute("SELECT * FROM SM_USER_TB WHERE USER_" + type + " = :type_data", [type_data])
        
        if len(res) < 1:
            if type == "ID":
                self.call_msg("중복확인", "사용가능한 아이디 입니다.")
                self.chk_id = True
                self.ori_id =self.j_le_id.text()
            elif type == "EMAIL":
                self.call_msg("중복확인", "사용가능한 이메일 입니다.")
                self.chk_email = True
                self.ori_email = self.j_le_email.text()
            self.j_label_msg.setText("")
        else:
            if type == "ID":
                self.call_msg("중복확인", "이미 사용중인 아이디 입니다.")
                self.j_label_msg.setText("이미 사용중인 아이디 입니다.")
            elif type == "EMAIL":
                self.call_msg("중복확인", "이미 사용중인 이메일 입니다.")
                self.j_label_msg.setText("이미 사용중인 이메일 입니다.")
    
    def sign_up(self, HomeWindow):
        id = self.j_le_id.text()
        pw = self.j_le_pw.text()
        pwc = self.j_le_pwc.text()
        email = self.j_le_email.text()
        birth = "".join(self.j_le_birth.text().split("-"))
        gender = self.j_le_gender1.isChecked() and 1 or 2
        
        if self.chk_none(self.j_le_id) and self.chk_none(self.j_le_pw) and self.chk_none(self.j_le_pwc) and self.chk_none(self.j_le_email) and self.chk_none(self.j_le_birth):
            self.j_label_msg.setText("")
            if len(id) < 3 :
                self.j_label_msg.setText("아이디는 3자 이상 가능합니다.")
                self.j_le_id.setFocus()
                return
            if id != self.ori_id:
                self.j_label_msg.setText("아이디 중복확인을 완료해주세요.")
                self.j_le_id.setFocus()
                return
            if len(pw) < 4 :
                self.j_label_msg.setText("비밀번호는 4자 이상 가능합니다.")
                self.j_le_pw.setFocus()
                return
            if pw != pwc :
                self.j_label_msg.setText("비밀번호를 확인해 주세요.")
                self.j_le_pwc.setFocus()
                return
            
            email_re = re.compile('[A-z0-9._]+@[A-z0-9_]+.[A-z]+')
            email_list = email_re.findall(email)
            
            if len(email_list) < 1 :
                self.j_label_msg.setText("이메일 형식을 확인해 주세요.")
                self.j_le_email.setFocus()
                return
            if email != self.ori_email:
                self.j_label_msg.setText("이메일 중복확인을 완료해주세요.")
                self.j_le_email.setFocus()
                return
            
            res = excute("INSERT INTO SM_USER_TB(USER_NO, USER_ID, USER_PW, USER_EMAIL, USER_BIRTH, USER_STATE, USER_GENDER) VALUES(SM_USER_SEQ.NEXTVAL, :id, :pw, :email, :birth, 1, :gender)",
                        [id, pw, email, birth, gender])

            if res:
                self.call_msg("회원가입", "회원가입을 완료했습니다.")
                HomeWindow.start_login()
            else:
                self.call_msg("회원가입", "오류가 발생했습니다.")
        
    def chk_none(self, obj):
        if obj.text() == "" or obj.text() is None:
            obj.setFocus()
            self.j_label_msg.setText("모든 항목을 입력해주세요.")
            return False 
        return True
    
    def call_msg(self, title, content):
        QMessageBox.question(self.centralwidget, title, content, QMessageBox.Yes, QMessageBox.Yes)
        
        