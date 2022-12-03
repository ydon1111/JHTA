import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit
from PyQt5.QtCore import QCoreApplication

class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def print(self):
        num = self.btnnm.text()
        for i in range(1,10):
         print(num ,"*", i,"=" ,num*i)
        self.btnnm.setText("")

    def initUI(self):
        self.setWindowTitle("구구단 출력")
        self.resize(800,600)
        self.move(300,400)

        
        btn1 = QPushButton("입력 단 출력",self)
        btn1.resize(100,100)
        btn1.move(350,220)

        btn1.clicked.connect(self.print)

        self.btnnm = QLineEdit(self)
        self.btnnm.move(100,100)
        self.btnnm.resize(320,30)

        self.show()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())