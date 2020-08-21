import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class main():
    def setupUI(self, HomeWindow):
        HomeWindow.setWindowTitle("날씨")
        
        self.centralwidget = QWidget(HomeWindow)
        HomeWindow.setCentralWidget(self.centralwidget)
        
        self.logout_btn = QPushButton("로그아웃", self.centralwidget)
        self.logout_btn.move(1500, 10)
        self.logout_btn.clicked.connect(lambda: self.logout(HomeWindow))
        
        ###############날씨와 추첮 영역만 나눈거라 나중에 삭제 start####################
        self.division = QLabel("----------------------------------------------------------------------------", self.centralwidget)
        self.division.move(0, 550)
        ################날씨와 추첮 영역만 나눈거라 나중에 삭제 end####################
        
        #수평상자 레이아웃 객체         
        wh_scrollArea = QScrollArea()
        wh_box = QHBoxLayout()
        wh_scrollArea.setWidget(QLabel("날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨날씨", self.centralwidget))
        # wh_box.addStretch(1)
        wh_box.addWidget(wh_scrollArea)
        




        rcd_scrollArea = QScrollArea()
        rcd_box = QHBoxLayout()
        rcd_scrollArea.setWidget(QLabel("추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천추천", self.centralwidget))
        rcd_box.addWidget(rcd_scrollArea)
        rcd_box.addWidget(QPushButton("버튼",self.centralwidget))
        rcd_box.addWidget(QPushButton("버튼1",self.centralwidget))
        rcd_box.addWidget(QPushButton("버튼2",self.centralwidget))


        vbox = QVBoxLayout()
        vbox.addLayout(wh_box)
        vbox.addLayout(rcd_box)
    
        
        
        self.centralwidget.setLayout(vbox)
        
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
        rcd_scrollArea = QScrollArea()
        
        self.widget_youtube = QWidget(self.centralwidget)        
        self.widget_youtube.setGeometry(QRect(10, 550, 2000, 1200))


        self.webview1=QWebEngineView(self.widget_youtube)
        self.webview1.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
        self.webview1.setGeometry(0,0,300,300)

        self.webview1=QWebEngineView(self.widget_youtube)
        self.webview1.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
        self.webview1.setGeometry(500,0,300,300)






        # self.musicbtn = QPushButton("지금 날씨 음악추천",self.centralwidget)
        # self.musicbtn.setGeometry(QRect(10,550,150,50))

        # self.cookbtn = QPushButton("지금 날씨 요리추천",self.centralwidget)
        # self.cookbtn.setGeometry(QRect(10,650,150,50))

        # self.tripbtn = QPushButton("지금 날씨 여행추천",self.centralwidget)
        # self.tripbtn.setGeometry(QRect(10,750,150,50))

        
        
        
        
        
        ############################영돈 end############################
    
        
        