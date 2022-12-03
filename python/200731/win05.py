import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton ,QLabel
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QCoreApplication, Qt
import time 
import threading
import math



class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def keyPressEvent(self,e):
        # print(e.key())  
        if e.key() == Qt.Key_Left:
            x= self.label1.x() - 10
            y= self.label1.y() 
            self.label1.move(x,y)           
        
        elif e.key() == Qt.Key_Right:
            x= self.label1.x() + 10
            y= self.label1.y()
            self.label1.move(x,y)        
        
        elif e.key() == Qt.Key_Down:
            x= self.label1.x() 
            y= self.label1.y() + 10
            self.label1.move(x,y)

        elif e.key() == Qt.Key_Up:
            x= self.label1.x() 
            y= self.label1.y() - 10
            self.label1.move(x,y) 

        elif e.key() == Qt.Key_Space:      
            t= threading.Thread(target=self.moveTurtle)
            t.start()
    
    def moveTurtle(self):
        
        for i in range(10):
            time.sleep(0.01)
            self.label1.move(self.label1.x()+5,self.label1.y() - 10) 
        for r in range(10):
            time.sleep(0.01)
            self.label1.move(self.label1.x()+5,self.label1.y() + 10)         

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

        
        
        
        
        

        
        
        
        
        
        
    
        
        
        self.show()



if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())