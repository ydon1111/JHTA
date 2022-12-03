import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setGeometry(0,0,2000,900)
        self.label1 = QLabel("1",self)
        self.label1.move(100,100)
        
        self.label2 = QLabel("2",self)
        self.label2.move(400,100)
        
        self.label3 = QLabel("3",self)
        self.label3.move(700,100)
        
        self.label4 = QLabel("4",self)
        self.label4.move(1000,100)
        
        self.label5 = QLabel("5",self)
        self.label5.move(1300,100)
        
        self.label6 = QLabel("6",self)
        self.label6.move(1600,100)


        p_img = QPixmap("./img/lotto/q.jpg")
        
         
        self.label1.setPixmap(p_img)
        self.label2.setPixmap(p_img)
        self.label3.setPixmap(p_img)
        self.label4.setPixmap(p_img)
        self.label5.setPixmap(p_img)
        self.label6.setPixmap(p_img)
        


        btn = QPushButton("로또번호 출력",self)
        btn.move(150,400)
        btn.resize(400,50)


        btn.clicked.connect(self.lotto)





        self.show()
    
    def lotto(self):
     
        lotto = []
        import random 
        i =0
        while i<6:
            num = random.randint(1,45)
            if num in lotto:
                continue                   #진행 안하고 처음으로 돌아감 continue
            else:
                lotto.append(num)
                i+=1
            lotto.sort()

        
        self.label1.setPixmap(QPixmap("./img/lotto/ball"+str(lotto[0])+".png"))
        self.label2.setPixmap(QPixmap("./img/lotto/ball"+str(lotto[1])+".png"))
        self.label3.setPixmap(QPixmap("./img/lotto/ball"+str(lotto[2])+".png"))
        self.label4.setPixmap(QPixmap("./img/lotto/ball"+str(lotto[3])+".png"))
        self.label5.setPixmap(QPixmap("./img/lotto/ball"+str(lotto[4])+".png"))
        self.label6.setPixmap(QPixmap("./img/lotto/ball"+str(lotto[5])+".png"))






if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())