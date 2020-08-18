import sys
import cx_Oracle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class main():
    def setupUI(self, HomeWindow):
        HomeWindow.setWindowTitle("날씨")
        
        self.centralwidget = QWidget(HomeWindow)
        HomeWindow.setCentralWidget(self.centralwidget)
        
        ###############날씨와 추첮 영역만 나눈거라 나중에 삭제 start####################
        qp = QPainter()
        qp.begin(HomeWindow)
        qp.setPen(QPen(Qt.blue, 8))
        qp.drawLine(30, 230, 200, 50)
        qp.end()
        
        
        self.division = QLabel("---------------------------------------------------------------------------------------------------------------------------", self.centralwidget)
        self.division.move(0, 550)
        ################날씨와 추첮 영역만 나눈거라 나중에 삭제 end####################
        
        self.weather_func()
        self.recomm_func(HomeWindow)
        
        
    def weather_func(self):
        ##########################도현 steart###########################
        print("날씨")
        ############################도현 end############################
    widget_List = []
    def recomm_func(self, HomeWindow):
        ##########################영돈 steart###########################
        self.centralwidget.setObjectName("centralwidget")

        self.widget_youtube = QWidget(self.centralwidget)        
        self.widget_List.append(self.widget_youtube)
        self.widget_youtube.setGeometry(QRect(2, 700, 2000, 1200))
        self.widget_youtube.setObjectName("widget_youtube")
        
        

        self.label1 = QLabel("제목",self.centralwidget)
        self.label1.setGeometry(QRect(2,600,71,31))
  
        self.label2 = QLabel("제목",self.centralwidget)
        self.label2.setGeometry(QRect(100,600,71,31))
        
        self.label3 = QLabel("제목",self.centralwidget)
        self.label3.setGeometry(QRect(200,600,71,31))

        font1 = self.label1.font()
        font2 = self.label2.font()
        font3 = self.label3.font()

        font1.setPointSize(10)
        font2.setPointSize(10)
        font3.setPointSize(10)

        # self.font1.setFamily('나눔손글씨 붓')
        # self.font2.setFamily('나눔손글씨 붓')
        # self.font3.setFamily('나눔손글씨 붓')

        self.label1.setFont(font1)
        self.label2.setFont(font2)
        self.label3.setFont(font3)
        


        self.webview=QWebEngineView(self.widget_youtube)
        self.webview.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) #유튜브 뮤직노래 가져오기(music값), 유튜브 요리 가져오기(embed값)
        self.webview.setGeometry(0,0,300,500)


        self.webview=QWebEngineView(self.widget_youtube)
        self.webview.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0")) # 유튜브 요리 가져오기(embed값)
        self.webview.setGeometry(300,0,500,500)


        self.webview=QWebEngineView(self.widget_youtube)
        self.webview.setUrl(QUrl("https://blog.naver.com/kyoo703?Redirect=Log&logNo=222040918884")) # 여행 블로그 주소 
        self.webview.setGeometry(800,0,1000,500)


        self.menubar = QMenuBar(HomeWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        HomeWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)
        QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        ############################영돈 end############################
        