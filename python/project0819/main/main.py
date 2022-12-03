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
        self.music_play()
        
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
        
        self.scrollArea_box = QScrollArea()
        self.scrollArea_box.setWidgetResizable(True)
        self.grid1 = QGridLayout()
        
        self.grid1.addWidget(self.music, 0, 0)
        self.grid1.addWidget(self.food, 1, 0)
        self.grid1.addWidget(self.activity, 2, 0)
        
        self.rcd_box = QHBoxLayout()
        self.rcd_box.addLayout(self.grid1)
        self.rcd_box.addWidget(self.scrollArea_box)

        self.widget_youtube1 = QWidget(self.centralwidget)
        self.webview1=QWebEngineView(self.widget_youtube1)
        self.widget_youtube2 = QWidget(self.centralwidget)
        self.webview2=QWebEngineView(self.widget_youtube2)
        self.widget_youtube3 = QWidget(self.centralwidget)
        self.webview3=QWebEngineView(self.widget_youtube3)
        self.widget_youtube4 = QWidget(self.centralwidget)
        self.webview4=QWebEngineView(self.widget_youtube4)
        self.widget_youtube5 = QWidget(self.centralwidget)
        self.webview5=QWebEngineView(self.widget_youtube5)
        
        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.webview1)
        self.h_box.addWidget(self.webview2)
        self.h_box.addWidget(self.webview3)
        self.h_box.addWidget(self.webview4)
        self.h_box.addWidget(self.webview5)
        self.scrollArea_box.setLayout(self.h_box)

        self.vbox.addLayout(self.rcd_box)
    
    def music_play(self):
        
        #db에 넣은 자료를 가져와야함 
        self.toggle("Y")
        
        self.webview1.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
        self.webview2.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
        self.webview3.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
        self.webview4.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
        self.webview5.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
      
    def food_play(self):
        #db에 넣은 자료를 가져와야함 
        self.toggle("Y")
        self.webview1.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0"))
        self.webview2.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0"))
        self.webview3.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0"))
        self.webview4.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0"))
        self.webview5.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0"))
    
    def activity_play(self):
        #db에 넣은 자료를 가져와야함 
        self.webview1.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468"))
        self.webview2.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468")) 
        self.webview3.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468")) 
        self.webview4.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468")) 
        self.webview5.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468"))
        self.toggle("N")
        
    def toggle(self, type):
        if type == "Y" :
            self.webview2.show()
            self.webview3.show()
            self.webview4.show()
            self.webview5.show()
        else:
            self.webview2.hide()
            self.webview3.hide()
            self.webview4.hide()
            self.webview5.hide()
            
            
        
        