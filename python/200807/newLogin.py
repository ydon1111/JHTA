# python -m PyQt5.uic.pyuic -x login.ui -o login.py

# 에디터로 만든 파일 파이썬으로 변경
#변경하지 않고 하려면 아래처럼 파일을 가져오면 됨 


from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("e:/Login.ui",self)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())
