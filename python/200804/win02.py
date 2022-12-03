import sys

from PyQt5.QtWidgets import *


#윈도우를 생성하는 클래스 : QMainWindow, Qwidget , QDialog
# 메인윈도우를 생성하기 위한 클래스 QMainWindow ,QDialog
# QMainWindow : QHBoxLayout,QVBoxLayout 같은 layout 사용 할 수 없다.


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.show()




if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())

