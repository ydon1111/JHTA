import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.drawType = 1  #1.직선 2.사각형
        self.initUI()        #함수 실행할꺼임


    def initUI(self):                                      #함수만듬
        self.setGeometry(100,100,1000,800) #창크기 위치 설정 x y w h
        #전체 폼
        frmbox = QHBoxLayout()         
        self.setLayout(frmbox)

        #좌측 레이아웃
        leftbox = QVBoxLayout()
        rightbox = QVBoxLayout()

        #좌측 레이아웃 
        gb = QGroupBox("타입")
        leftbox.addWidget(gb)

        box1 = QVBoxLayout()
        gb.setLayout(box1)

        self.rbtnLine = QRadioButton("직선",self)
        self.rbtnRect = QRadioButton("사각형",self)
        self.rbtnCurve = QRadioButton("곡선",self)
        self.rbtnEllipse = QRadioButton("타원",self)
       
        box1.addWidget(self.rbtnLine)
        box1.addWidget(self.rbtnRect)
        box1.addWidget(self.rbtnCurve)
        box1.addWidget(self.rbtnEllipse)
        
        self.rbtnLine.clicked.connect(self.radioBtnClicked)
        self.rbtnCurve.clicked.connect(self.radioBtnClicked)
        self.rbtnRect.clicked.connect(self.radioBtnClicked)
        self.rbtnEllipse.clicked.connect(self.radioBtnClicked)
        
        
        self.rbtnLine.setChecked(True)
        self.drawType = 1


        #그룹박스2

        gb2 = QGroupBox("Pen setting")
        leftbox.addWidget(gb2)

        grid = QGridLayout()
        gb2.setLayout(grid)

        label = QLabel("선굵기")
        grid.addWidget(label,0,0)

        self.combo = QComboBox()
        grid.addWidget(self.combo,0,1)

        for i in range(1,21):
            self.combo.addItem(str(i))

        label2 = QLabel("선색")
        grid.addWidget(label2,1,0)

        #펜 색상
        self.pencolor = QColor(0,0,0)
        self.penbtn = QPushButton()
        self.penbtn.setStyleSheet("background-color: rgb(0,0,0)")
        grid.addWidget(self.penbtn,1,1) 
        #선 색상선택 버튼 누르면

        self.penbtn.clicked.connect(self.selectColor)

        
        #그룹박스 3
        #붓 설정

        gb3 = QGroupBox("붓 설정")
        leftbox.addWidget(gb3)

        hbox =QHBoxLayout()
        gb3.setLayout(hbox)

        label3 = QLabel("붓색상")
        hbox.addWidget(label3)

        self.brushcolor = QColor(255,255,255)
        self.brushbtn = QPushButton()
        self.brushbtn.setStyleSheet("background-color: rgb(255,255,255)")
        hbox.addWidget(self.brushbtn)

        self.brushbtn.clicked.connect(self.selectColor)
        #우측 레이아웃 박스에 그래픽 뷰 추가 

        self.view = CGView(self)
        rightbox.addWidget(self.view)


        
        frmbox.addLayout(leftbox)
        frmbox.addLayout(rightbox)


        self.show()

    def radioBtnClicked(self):
        #어떤것이 선택되었는지 확인

        if self.rbtnLine.isChecked():
            self.drawType = 1 
        elif self.rbtnRect.isChecked(): 
            self.drawType = 2
        elif self.rbtnCurve.isChecked():
            self.drawType = 3 
        elif self.rbtnEllipse.isChecked():
            self.drawType = 4
        # print("선택한 타입은 : ", self.drawType)

    def selectColor(self):
        
        #색상 대화상자 생성
        color = QColorDialog.getColor()
        who = self.sender()

        if who == self.penbtn:
            self.pencolor = color
            self.penbtn.setStyleSheet("background-color:{}".format(color.name()))
          
            # print("펜버튼")
        elif who == self.brushbtn:
            self.brushcolor =color
            self.brushbtn.setStyleSheet("background-color:{}".format(color.name()))
            # print("붓 색상버튼")





# QGraphics 는 시각적 객체의 복잡한 자염을 쉽게 처리 할 수 있는 프레임 워크로 구성하는데 사용 할 수 있다.

# QGraphicsView,QGraphicsScne, QGraphicsItem

class CGView(QGraphicsView):
    def __init__(self,parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.items = []
        self.start = QPointF()
        self.end = QPointF()

    def moveEvent(self,e):
        # print("moveEvent 창움직일때")
        rect = QRectF(self.rect())
        rect.adjust(0,0,-3,-3)
        self.scene.setSceneRect(rect)
    def mousePressEvent(self,e):
        # print("mousePressEvent 클릭")
        if e.button() == Qt.LeftButton:   # 마우스 버튼 누르면 숫자가 나와서 코딩가능함 , 영어 철자변경해 코드 읽기 편하게함
            #시작점을 저장
            self.start=e.pos()
            self.end=e.pos()
            # print(e.pos())     

    def mouseMoveEvent(self,e):
        # print("mouseMoveEvent 드래그")
        self.end = e.pos()
        
        pen =QPen(self.parent().pencolor,self.parent().combo.currentIndex()+1)
        
        
       
        # # scene에 그려진 선을 지움
        # if len(self.items) > 0:
        #     print("aaaa")
        #     self.scene.removeItem(self.items[-1])
        #     del(self.items[-1])


        # #현재 선을 그림
        if self.parent().drawType == 1:  
            line= QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
            self.items.append(self.scene.addLine(line,pen))
            if len(self.items) > 0:
                self.scene.removeItem(self.items[-1])
                del(self.items[-1])
        #사각형그리기
        elif self.parent().drawType == 2: 
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start,self.end)
            self.items.append(self.scene.addRect(rect,pen,brush))

        #곡선그리기
        elif self.parent().drawType == 3:
            line= QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
            self.items.append(self.scene.addLine(line,pen))
            #끝점을 다시 시작점으로
            self.start=e.pos()

        #타원그리기 
        elif self.parent().drawType == 4:
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start,self.end)
            self.items.append(self.scene.addEllipse(rect,pen,brush))
            if len(self.items) > 0:
                self.scene.removeItem(self.items[-1])
                del(self.items[-1])
           


    def mouseReleaseEvent(self,e):
        # print("마우스 땔때")    
        self.end = e.pos()
        pen =QPen(self.parent().pencolor,self.parent().combo.currentIndex()+1)
        if self.parent().drawType == 1:  
            line= QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
            self.scene.addLine(line,pen)
        elif self.parent().drawType == 2: 
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start,self.end)
            self.scene.addRect(rect,pen,brush)

        elif self.parent().drawType == 4:
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start,self.end)
            self.items.append(self.scene.addEllipse(rect,pen,brush))



if __name__ =="__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())