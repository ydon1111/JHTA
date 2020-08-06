import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

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
        
        qp.setPen(QPen(QColor(225,0,0),5))
       
        qp.drawEllipse(QPoint(220.0,220.0),100,200)

        qp.drawEllipse(QPoint(600.0,220.0),200,100) #좌표,가로(너비),세로(높이) 


        qp.end()







if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())