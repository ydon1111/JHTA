
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def print(self):
        print("버튼이 눌림, 바보야")

    def initUI(self):
        #창의 타이틀 지정
        #푸쉬버튼 객체 생성
        self.setWindowTitle("와.. 금요일이다..불금불금")
        self.resize(1200,800)            #사이즈 조절
        self.move(300,400)               #창이동
        #화면에 나오게함
    
        btn1 = QPushButton("출력",self)
        btn1.setText("print")
        btn1.resize(100,100)
        btn1.move(300,200)
        
        btn1.clicked.connect(self.print)
        #이벤트 핸들러

        btn2 = QPushButton("exit",self)
        btn2.resize(100,100)
        btn2.move(500,200)

        btn2.clicked.connect(QCoreApplication.instance().quit)

        self.show()
if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
