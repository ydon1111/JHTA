import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
import random
import time
import threading

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
        qp = QPainter()
        qp.begin(self)
        self.shape()
        threading.Thread(target=self.shpae)
        time.sleep(0.01)
        qp.end()


    def shape(self):
        for i in range(1,100):
            time.sleep(0.01)
            red = random.randint(1,255)
            green = random.randint(1,255)
            blue = random.randint(1,255)
            porintsize = random.randint(0,10) 
            x1 = random.randint(1,800)
            y1 = random.randint(1,800)
            x2 = random.randint(1,800)
            y2 = random.randint(1,800)

            qp.setPen(QPen(QColor(red,green,blue),porintsize))        
            qp.drawLine(x1,y1,x2,y2)
    





if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())