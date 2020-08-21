import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from common.DBconnect import *
import cx_Oracle

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

    
    def logout(self, HomeWindow):
        res = QMessageBox.question(self.centralwidget, "로그아웃", "로그아웃 하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if res == QMessageBox.Yes: HomeWindow.start_login()
        
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.whUI()
        self.rcdUI()
        self.centralwidget.setLayout(self.vbox)
        self.music_play()
        
    def whUI(self):
        p_img1 = QPixmap("./project0820/img/sun.png")
        p_img2 = QPixmap("./project0820/img/rain.png")
        
        #수평상자 레이아웃 객체         
        self.wh_box = QHBoxLayout() # 최상위 box
        self.wh_scrollArea = QScrollArea() # 스크롤
        self.wh_in_box = QHBoxLayout() # 스크롤 안 박스

        self.tn_box = QHBoxLayout() # 오늘, 내일, 모레 날씨 박스
        for i in range(3):
            self.lb = QLabel("aaaaaaaaaaa", self.centralwidget)
            self.lb.setPixmap(p_img1)
            self.lb.resize(300, 300)
            self.tn_box.addWidget(self.lb)
        
        self.wh_in_box.addLayout(self.tn_box)
        
        # 주간 날씨 박스
        self.week_box = QVBoxLayout()
        self.ko_week_box = QHBoxLayout()
        self.no_week_box = QHBoxLayout()
        
        for i in range(5):
            self.lb4 = QLabel("aaaaaaaaaaa", self.centralwidget)
            self.lb4.setPixmap(p_img2)
            self.lb4.resize(300, 300)
            self.ko_week_box.addWidget(self.lb4)
        self.week_box.addLayout(self.ko_week_box)
        
        for i in range(5):
            self.lb4 = QLabel("aaaaaaaaaaa", self.centralwidget)
            self.lb4.setPixmap(p_img2)
            self.lb4.resize(300, 300)
            self.no_week_box.addWidget(self.lb4)
        self.week_box.addLayout(self.no_week_box)
        
        self.wh_in_box.addLayout(self.week_box)
        
        self.wh_scrollArea.setLayout(self.wh_in_box)
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
        sql = "SELECT RCD_URL FROM SM_RCD_TB WHERE RCD_TYPE = :txt and RCD_TNWH_NO = :txt2"
        res = excute(sql, [1,555])
        print(res)
        
        self.toggle("Y")
        self.webview1.setUrl(QUrl(res[0][0]))
        self.webview2.setUrl(QUrl(res[1][0])) 
        self.webview3.setUrl(QUrl(res[2][0]))  
        self.webview4.setUrl(QUrl(res[3][0]))  
        self.webview5.setUrl(QUrl(res[4][0]))  

    def food_play(self):
        sql = "SELECT RCD_URL FROM SM_RCD_TB WHERE RCD_TYPE = :txt and  RCD_TNWH_NO = :txt2"
        res = excute(sql, [3,555])
        print(res)
        
        self.toggle("Y")
        self.webview1.setUrl(QUrl(res[0][0]))
        self.webview2.setUrl(QUrl(res[1][0])) 
        self.webview3.setUrl(QUrl(res[2][0]))  
        self.webview4.setUrl(QUrl(res[3][0]))  
        self.webview5.setUrl(QUrl(res[4][0]))  
        
    def activity_play(self):
        
        sql = "SELECT RCD_URL FROM SM_RCD_TB WHERE RCD_TYPE = :txt and RCD_TNWH_NO = :txt2"
        res = excute(sql, [2,555])
        print(res)

        self.webview1.setUrl(QUrl(res[0][0]))
        self.webview2.setUrl(QUrl(res[0][0])) 
        self.webview3.setUrl(QUrl(res[0][0]))  
        self.webview4.setUrl(QUrl(res[0][0]))  
        self.webview5.setUrl(QUrl(res[0][0]))  
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
        
    def weather_func(self, HomeWindow):
        ##########################도현 steart###########################
        print("날씨")
        ############################도현 end############################
    

            
        
        