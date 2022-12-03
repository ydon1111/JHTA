import sys
# from PyQt5 import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
import time
from PyQt5.QtCore import QCoreApplication, Qt
    
class MyWindow2(QMainWindow):
    def __init__(self,parent):
        super().__init__(parent)
        self.setGeometry(100,100,300,300)  
        self.setWindowTitle("메롱~")
        p_img = QPixmap("./img/merong.gif")                
        self.label1 = QLabel("메롱",self)
        self.label1.setPixmap(p_img)   
        # self.label1.move(200,100)     
        # self.label1.resize(400,400)
        self.label1.setGeometry(0,0,500,500)
        self.show()



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("연애도우미")
        # self.move(200,200)
        # self.resize(300,300)
        self.setGeometry(200,200,600,600)


        self.btn = QPushButton("나의 애인보기",self)
        self.btn.move(100,100)
        self.btn.setToolTip("<h3>날 눌러봐!!</h3>")
        
        self.btn.clicked.connect(self.newWindow)

        self.show()

    def newWindow(self):    
        for i in range(5):
            time.sleep(0.2)
            # self.nw = QMainWindow(self)
            self.nw = MyWindow2(self)
            self.nw.move(100+i*100,100+i*100)
            self.nw.resize(600,600)     
            self.nw.show()
        # self.hide()  숨기기, 종류


# pip install pyinstaller 윈도우 실행파일 설치 
# cd 폴더위치
#PS E:\dev\python_workspace\200803> pyinstaller -w -F MyWindow.py 
# -w cmd 창 없애기
# -F 파일하나로 만들기 (부가폴더들 없앰)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())

