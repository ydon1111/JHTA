import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #창 타이틀 (점찍기)
        #크기와 위치
        #화면에 보이게 설정
        self.setWindowTitle("점찍기")
        self.setGeometry(100,100,800,600)
        self.show()
    def paintEvent(self,e):
        # print("페인트 이벤트 발생")
        qp = QPainter()  #QPaint 인스턴스 생성

 
      
        qp.begin(self)
       
        qp.setBrush(QColor(255,0,255)) #색채우기 
       
        qp.setPen(QPen(QColor(100,100,100),5))
        qp.drawRect(30,30,100,150)   #x,y, 너비 , 높이
       
        qp.setPen(QPen(QColor(100,0,0),5))
        qp.drawLine(200,100,600,100)


        qp.setBrush(QColor(0,255,255))
        qp.setPen(QPen(Qt.blue,5))
        qp.drawRect(200,200,60,75)


        qp.setBrush(QColor(300,100,30))
        qp.setPen(QPen(Qt.blue,5))
        qp.drawRect(300,200,60,75)

        qp.setBrush(QColor(224,40,40))
        qp.setPen(QPen(Qt.blue,5))
        qp.drawRect(400,200,60,75)

        qp.setBrush(QColor(110,30,60))
        qp.setPen(QPen(Qt.green,5))
        qp.drawRect(200,400,300,75)


        qp.drawEllipse(QPoint(20.0,20.0),100,200)

        qp.end()






if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())