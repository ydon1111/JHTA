import sys
from user.login import *
from user.join import *
from main.main import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1600, 900)
        self.move(170, 50)
        self.setWindowIcon(QIcon('./project/img/icon2.png'))
        
        self.user_info = dict() # 임시 user 정보 : {"user_no": USER_NO, "id": USER_ID, "email": USER_EMAIL, "birth": USER_BIRTH, "gender": USER_GENDER}

        self.font_style() # 공통 font style
        
        self.m_login = Login() # 로그인 클래스
        self.m_join = Join() # 회원가입 클래스
        self.m_main = main() # 날씨, 추천 클래스 (메인)
        
        self.start_login() # 처음 시작 화면
    
    def font_style(self):
        fontt = QFont("1훈정글북 Regular")
        self.setFont(fontt)

    def start_join(self):
        self.set_background_img("./project/img/join.png")
        self.m_join.setupUI(self)
        self.show()

    def start_login(self):
        self.set_background_img("./project/img/login.png")
        self.user_info = dict()
        self.m_login.setupUI(self)
        self.show()
        
    def start_main(self, loc = 1):
        self.set_background_img("./project/img/main.png")
        # self.setStyleSheet("background-color: #FFFFFF;")
        self.m_main.setupUI(self, loc)
        self.show()
        
    def set_background_img(self, url):
        oImage = QImage(url)
        sImage = oImage.scaled(QSize(self.width(),self.height()))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomeWindow()
    sys.exit(app.exec_())