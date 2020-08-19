  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QUrl, pyqtSlot
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

class Ui_MainWindow(object):
    widget_List = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("날씨별 추천")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.widget_youtube = QtWidgets.QWidget(self.centralwidget)        
        self.widget_List.append(self.widget_youtube)
        self.widget_youtube.setGeometry(QtCore.QRect(2, 100, 2000, 1200))
        # self.widget_youtube.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.widget_youtube.setObjectName("widget_youtube")

        self.webview=QtWebEngineWidgets.QWebEngineView(self.widget_youtube)
        self.webview.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) #유튜브 뮤직노래 가져오기(music값), 유튜브 요리 가져오기(embed값)
        self.webview.setGeometry(0,0,300,500)



        self.webview=QtWebEngineWidgets.QWebEngineView(self.widget_youtube)
        self.webview.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0")) # 유튜브 요리 가져오기(embed값)
        self.webview.setGeometry(300,0,500,500)


        self.webview=QtWebEngineWidgets.QWebEngineView(self.widget_youtube)
        self.webview.setUrl(QUrl("https://blog.naver.com/kyoo703?Redirect=Log&logNo=222040918884")) # 여행 블로그 주소 
        self.webview.setGeometry(800,0,1000,500)




        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())