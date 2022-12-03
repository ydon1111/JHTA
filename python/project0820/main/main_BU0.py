import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class main():
    def setupUI(self, HomeWindow):
        HomeWindow.setWindowTitle("날씨")
        
        self.centralwidget = QWidget(HomeWindow)
        HomeWindow.setCentralWidget(self.centralwidget)
        
        self.logout_btn = QPushButton("로그아웃", self.centralwidget)
        self.logout_btn.move(1500, 10)
        self.logout_btn.clicked.connect(lambda: self.logout(HomeWindow))
        
        self.initUI()
        
        self.weather_func(HomeWindow)
        self.recomm_func()
    
    def logout(self, HomeWindow):
        res = QMessageBox.question(self.centralwidget, "로그아웃", "로그아웃 하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if res == QMessageBox.Yes: HomeWindow.start_login()
        
    def weather_func(self, HomeWindow):
        ##########################도현 steart###########################
        print("날씨")
        ############################도현 end############################
    
    def recomm_func(self):
        ##########################영돈 steart###########################
        print("추천")
        ############################도현 end############################
        
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.whUI()
        self.rcdUI()
        self.centralwidget.setLayout(self.vbox)
        
    def whUI(self):
        #수평상자 레이아웃 객체         
        self.wh_scrollArea = QScrollArea()
        self.wh_box = QHBoxLayout()
        self.wh_scrollArea.setWidget(QLabel("날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨", self.centralwidget))
        # wh_box.addStretch(1)
        self.wh_box.addWidget(self.wh_scrollArea)

        self.vbox.addLayout(self.wh_box)
        
    def rcdUI(self):
        self.music = QPushButton("노래", self.centralwidget)
        self.music.clicked.connect(self.music_play)
        self.food = QPushButton("음식", self.centralwidget)
        self.food.clicked.connect(self.food_play)
        self.activity = QPushButton("활동", self.centralwidget)
        self.activity.clicked.connect(self.activity_play)
        self.test_labe = QLabel("", self.centralwidget)
        
        self.rcd_scrollArea = QScrollArea()
        self.rcd_scrollArea.setWidgetResizable(True)
        self.grid1 = QGridLayout()
        self.rcd_scrollArea.setWidget(self.test_labe)
        
        self.grid1.addWidget(self.music, 0, 0)
        self.grid1.addWidget(self.food, 1, 0)
        self.grid1.addWidget(self.activity, 2, 0)
        
        self.rcd_box = QHBoxLayout()
        self.rcd_box.addLayout(self.grid1)
        self.rcd_box.addWidget(self.rcd_scrollArea)

        self.vbox.addLayout(self.rcd_box)
    
    def music_play(self):
        self.test_labe.setText("노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래노래")
    
    def food_play(self):
        self.test_labe.setText("음식음식음식")
    
    def activity_play(self):
        self.test_labe.setText("활동활동활동")
        
        