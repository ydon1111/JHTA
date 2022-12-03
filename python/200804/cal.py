import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class CalWidget(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.disp =  QLineEdit(self)
        
        self.btn7 =  QPushButton("7",self)
        self.btn8 =  QPushButton("8",self)
        self.btn9 =  QPushButton("9",self)
        self.btnp =  QPushButton("+",self)
        
        self.btn4 =  QPushButton("4",self)
        self.btn5 =  QPushButton("5",self)
        self.btn6 =  QPushButton("6",self)
        self.btnmi =  QPushButton("-",self)
        
        self.btn1 =  QPushButton("1",self)
        self.btn2 =  QPushButton("2",self)
        self.btn3 =  QPushButton("3",self)
        self.btnmal =  QPushButton("*",self)
        
        self.btn0 =  QPushButton("0",self)
        self.btn00 =  QPushButton("00",self)
        self.btnequ =  QPushButton("=",self)
        self.btndiv =  QPushButton("/",self)

        grid = QGridLayout()
        self.setLayout(grid)

        # gridList = []
        # cnt = 0
        # for i in range(1,3):
        #     for j in range(0,4):
        #         grid.addWidget(gridList[cnt],i,j)
        #         cnt += 1

        grid.addWidget(self.disp ,0,0,1,4)
        grid.addWidget(self.btn7 , 1,0)
        grid.addWidget(self.btn8 , 1,1)
        grid.addWidget(self.btn9 , 1,2)
        grid.addWidget(self.btnp , 1,3)
        
        grid.addWidget(self.btn4 , 2,0)
        grid.addWidget(self.btn5 , 2,1)
        grid.addWidget(self.btn6 , 2,2)
        grid.addWidget(self.btnmi , 2,3)
        
        grid.addWidget(self.btn1 , 3,0)
        grid.addWidget(self.btn2 , 3,1)
        grid.addWidget(self.btn3 , 3,2)
        grid.addWidget(self.btnmal, 3,3)
        
        grid.addWidget(self.btn0  ,4,0)
        grid.addWidget(self.btn00 , 4,1)
        grid.addWidget(self.btnequ , 4,2)
        grid.addWidget(self.btndiv , 4,3)
      
        # self.btn7.clicked.connect(self.f7)
        self.btn7.clicked.connect(lambda : self.func("7"))
        self.btn8.clicked.connect(lambda : self.func("8"))
        self.btn9.clicked.connect(lambda : self.func("9"))
        self.btnp.clicked.connect(lambda : self.func("+"))
        self.btn4.clicked.connect(lambda : self.func("4"))
        self.btn5.clicked.connect(lambda : self.func("5"))
        self.btn6.clicked.connect(lambda : self.func("6"))
        self.btnmi.clicked.connect(lambda : self.func("-"))
        self.btn1.clicked.connect(lambda : self.func("1"))
        self.btn2.clicked.connect(lambda : self.func("2"))
        self.btn3.clicked.connect(lambda : self.func("3"))
        self.btnmal.clicked.connect(lambda : self.func("*"))
        self.btn0.clicked.connect(lambda : self.func("0"))
        self.btn00.clicked.connect(lambda : self.func("00"))
        # self.btnequ.clicked.connect(lambda : self.func("="))
        self.btndiv.clicked.connect(lambda : self.func("/"))

        self.btnequ.clicked.connect(self.cal)


        # self.btn8.clicked.connect(self.f8)
        # self.btn9.clicked.connect(self.f9)
        # self.btnp.clicked.connect(self.fp)
        # self.btn4.clicked.connect(self.f4)
        # self.btn5.clicked.connect(self.f5)
        # self.btn6.clicked.connect(self.f6)
        # self.btnmi.clicked.connect(self.fmi)
        # self.btn1.clicked.connect(self.f1)
        # self.btn2.clicked.connect(self.f2)
        # self.btn3.clicked.connect(self.f3)
        # self.btnmal.clicked.connect(self.fmal)
        # self.btn0.clicked.connect(self.f0)
        # self.btn00.clicked.connect(self.f00)
        # self.btnequ.clicked.connect(self.fequ)
        # self.btndiv.clicked.connect(self.fdiv)



        self.show()

    def cal(self):
        print(eval(self.disp.text()))
        self.disp.setText(str(eval(self.disp.text())))

    def func(self,txt):
        self.disp.setText(self.disp.text()+txt)
    # def f8(self):
    #     print("8번눌림")
    #     self.disp.setText(self.disp.text()+'8')
    # def f9(self):
    #     self.disp.setText(self.disp.text()+'9')

    # def keyPressEvent(self,e):
    #     print("키보드가 눌릴때")

    # def keyReleaseEvent(self,e):
    #     print("키보드를 땔때")
    
    # def mouseMoveEvent(self,e):
    #     print("마우스 움직일때")

    # def mouseDoubleClickEvent(self,e):
    #     print("마우스 더블클릭")  

    # def mousePressEvent(self,e):
    #     print(e)
        
    # def resizeEvent(self,e):
    #     print("위젯의 크기를 변경할떄")




class CalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,400,400)
        self.setCentralWidget(CalWidget(self))
        self.setWindowTitle("계산기")
    
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cal = CalWindow()
    sys.exit(app.exec_())

# pip install pyinstaller 윈도우 실행파일 설치 
# cd 폴더위치
#PS E:\dev\python_workspace\200803> pyinstaller -w -F MyWindow.py 
# -w cmd 창 없애기
# -F 파일하나로 만들기 (부가폴더들 없앰)