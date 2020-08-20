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
        
        
        # self.division = QLabel("---------------------------------------------------------------------------------------------------------------------------", self.centralwidget)
        # self.division.move(0, 550)
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
        self.widget_youtube.setGeometry(QRect(2, 500, 2000, 1200))
        self.widget_youtube.setObjectName("widget_youtube")
         
   
        
        self.musicbtn = QPushButton("지금 날씨 음악추천",self.centralwidget)
        self.musicbtn.setGeometry(QRect(2,600,150,50))

        self.cookbtn = QPushButton("지금 날씨 요리추천",self.centralwidget)
        self.cookbtn.setGeometry(QRect(2,700,150,50))

        self.tripbtn = QPushButton("지금 날씨 여행추천",self.centralwidget)
        self.tripbtn.setGeometry(QRect(2,800,150,50))


        self.musicbtn.clicked.connect(self.musicView)
        
     
        
    
    def musicView(self):
        print("눌림")
        self.centralwidget.webviewBig = QWebEngineView(self.centralwidget)
        self.centralwidget.webviewBig.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0")) # 유튜브 요리 가져오기(embed값)
        self.centralwidget.webviewBig.setGeometry(450,0,850,850)
        self.centralwidget.show()
    
    





        #그리드가 안먹음
        # grid = QGridLayout()
        # self.centralwidget.setLayout(grid)
        # grid.centralwidget.addWidget(self.musicbtn,0,0)
        # grid.centralwidget.addWidget(self.cookbtn,1,0)
        # grid.centralwidget.addWidget(self.tripbtn,2,0)

        
        #나중에 라벨 필요하면 사용 
        # self.label1 = QLabel("제목",self.centralwidget)
        # self.label1.setGeometry(QRect(2,600,71,31))
        # self.label2 = QLabel("제목",self.centralwidget)
        # self.label2.setGeometry(QRect(100,600,71,31))
        # self.label3 = QLabel("제목",self.centralwidget)
        # self.label3.setGeometry(QRect(200,600,71,31))
        # font1 = self.label1.font()
        # font2 = self.label2.font()
        # font3 = self.label3.font()
        # font1.setPointSize(10)
        # font2.setPointSize(10)
        # font3.setPointSize(10)
        # # self.font1.setFamily('나눔손글씨 붓')
        # # self.font2.setFamily('나눔손글씨 붓')
        # # self.font3.setFamily('나눔손글씨 붓')
        # self.label1.setFont(font1)
        # self.label2.setFont(font2)
        # self.label3.setFont(font3)
        

        #버튼 안되면 각 view 사용예정  
        # self.webview1=QWebEngineView(self.widget_youtube)
        # self.webview1.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) #유튜브 뮤직노래 가져오기(music값), 유튜브 요리 가져오기(embed값)
        # self.webview1.setGeometry(0,0,50,50)
        # self.webview2=QWebEngineView(self.widget_youtube)
        # self.webview2.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0")) # 유튜브 요리 가져오기(embed값)
        # self.webview2.setGeometry(80,0,50,50)
        # self.webview3=QWebEngineView(self.widget_youtube)
        # self.webview3.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468")) # 여행 블로그 주소 
        # self.webview3.setGeometry(160,0,60,60)
        # self.webview4=QWebEngineView(self.widget_youtube)
        # self.webview4.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) #유튜브 뮤직노래 가져오기(music값), 유튜브 요리 가져오기(embed값)
        # self.webview4.setGeometry(0,80,50,50)
        # self.webview5=QWebEngineView(self.widget_youtube)
        # self.webview5.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0")) # 유튜브 요리 가져오기(embed값)
        # self.webview5.setGeometry(80,80,50,50)
        # self.webview6=QWebEngineView(self.widget_youtube)
        # self.webview6.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468")) # 여행 블로그 주소 
        # self.webview6.setGeometry(160,80,60,60)
        # self.webview4=QWebEngineView(self.widget_youtube)
        # self.webview4.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) #유튜브 뮤직노래 가져오기(music값), 유튜브 요리 가져오기(embed값)
        # self.webview4.setGeometry(0,160,50,50)
        # self.webview5=QWebEngineView(self.widget_youtube)
        # self.webview5.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0")) # 유튜브 요리 가져오기(embed값)
        # self.webview5.setGeometry(80,160,50,50)
        # self.webview6=QWebEngineView(self.widget_youtube)
        # self.webview6.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468")) # 여행 블로그 주소 
        # self.webview6.setGeometry(160,160,60,60)



        # self.menubar = QMenuBar(HomeWindow)
        # self.menubar.setGeometry(QRect(0, 0, 800, 21))
        # self.menubar.setObjectName("menubar")

        # HomeWindow.setMenuBar(self.menubar)

        # self.statusbar = QStatusBar(HomeWindow)
        # self.statusbar.setObjectName("statusbar")
        # HomeWindow.setStatusBar(self.statusbar)

        # self.retranslateUi(HomeWindow)
        # QMetaObject.connectSlotsByName(HomeWindow)
        
     
    # def retranslateUi(self, MainWindow):
    #     _translate = QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        


        ############################영돈 end############################
        