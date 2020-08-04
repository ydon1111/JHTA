import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton ,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication



class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        label1 = QLabel("집에가자~~",self)
        label1.move(400,100)
        
        font1 =label1.font()
        font1.setPointSize(100)


        label1.setFont(font1)

        
        btn = QPushButton("Go",self)
        btn.move(400,400)
        btn.resize(400,50)

        btn.clicked.connect(QCoreApplication.instance().quit)


        self.setWindowTitle("집에가기")
        self.move(10,10)
        self.setWindowIcon(QIcon("./turtle.gif"))
        self.resize(1200,600)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())