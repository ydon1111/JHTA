import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton ,QLabel
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QCoreApplication


class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def umoveing(self):  
        x= self.label1.x() 
        y= self.label1.y() - 10
        self.label1.move(x,y) 
    
    def dmoveing(self):
        x= self.label1.x() 
        y= self.label1.y() + 10
        self.label1.move(x,y)

    def rmoveing(self):
        x= self.label1.x() + 10
        y= self.label1.y()
        self.label1.move(x,y)
    
    def lmoveing(self):
        x= self.label1.x() - 10
        y= self.label1.y() 
        self.label1.move(x,y) 
    


    def initUI(self):
        self.setWindowTitle("방향")
        self.resize(800,600)
        self.move(300,400)
        

        # QPixmap 객체
        p_img = QPixmap("turtle.gif")


        self.label1 = QLabel("움직일꺼다",self)
        self.label1.setPixmap(p_img)
        self.label1.move(200,100)

        font1 =self.label1.font()
        font1.setPointSize(50)


        self.label1.setFont(font1)

        
        
        btn1 = QPushButton("↑",self)
        btn1.resize(50,50)
        btn1.move(200,400)
        
        btn2 = QPushButton("↓",self)
        btn2.resize(50,50)
        btn2.move(200,450)
        
        btn3 = QPushButton("→",self)
        btn3.resize(50,50)
        btn3.move(250,450)
        
        btn4 = QPushButton("←",self)
        btn4.resize(50,50)
        btn4.move(150,450)


        btn1.clicked.connect(self.umoveing)
        btn2.clicked.connect(self.dmoveing)
        btn3.clicked.connect(self.rmoveing)
        btn4.clicked.connect(self.lmoveing)
        
        
        
    def keyPressEvent(self,e):
        print(e.key())  
        
        
        
        
        
        
        
        
        
        self.show()



if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())