import sys
from user.login import *
from user.join import *
from main.main import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1600, 900)
        self.move(170, 50)
        
        self.user_info = dict() # 임시 user 정보 : {"id": USER_ID, "email": USER_EMAIL, "birth": USER_BIRTH, "gender": USER_GENDER}
        
        self.m_login = Login() # 로그인 클래스
        self.m_join = Join() # 회원가입 클래스
        self.m_main = main() # 날씨, 추천 클래스 (메인)
        
        self.start_main() # 처음 시작 화면

    def start_join(self):
        self.set_background_img("./project/img/back1.png")
        self.m_join.setupUI(self)
        self.show()

    def start_login(self):
        self.set_background_img("./project/img/back4.png")
        self.user_info = dict()
        self.m_login.setupUI(self)
        self.show()
        
    def start_main(self):
        self.set_background_img("./project/img/back1.png")
        self.m_main.setupUI(self)
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