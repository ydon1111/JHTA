
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("내가 만든 윈도우창")
        self.move(10,10)
        self.setWindowIcon(QIcon("./img/instagram.png"))
        self.resize(1200,600)
        self.show()

if __name__== "__main__":
    app = QApplication(sys.argv)
    ex =Myapp()
    sys.exit(app.exec_())

