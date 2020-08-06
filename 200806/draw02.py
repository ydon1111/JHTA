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
        qp.begin(self)   #페인트 준비 시작 

        qp.setPen(QPen(Qt.blue,8)) #펜 설정(팬객체(파랑색,8픽셀))
        qp.drawPoint(self.width()/2,self.height()/2)#팬위치
        qp.end()

        qp2 = QPainter()
        qp2.begin(self)

        qp2.setPen(QPen(Qt.red,8))
        qp2.drawPoint(self.width()/4,self.height()/4)
        qp2.end()






if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())