import sys
from user.login import *
from user.join import *
from main.main import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 1600, 900)
        
        self.m_login = Login() # 로그인 클래스
        self.m_join = Join() # 회원가입 클래스
        self.m_main = main() # 날씨, 추천 클래스 (메인)
        
        self.start_main() # 처음 시작 화면

    def start_join(self):
        self.m_join.setupUI(self)
        self.show()

    def start_login(self):
        self.m_login.setupUI(self)
        self.show()
        
    def start_main(self):
        self.m_main.setupUI(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomeWindow()
    sys.exit(app.exec_())