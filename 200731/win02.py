
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLineEdit,QMessageBox
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def print(self):
        id = self.leId.text()
        pw = self.lePw.text()
        # print(id,type(id))
        # print(pw,type(pw))
        if id == 'aaa' and pw == 'bbb':
            print("로그인되었습니다.")
        else: 
            print("로그인에 실패했습니다.")
        self.leId.setText("")
        self.lePw.setText("")
        
    def close(self):
        # QMessageBox 클래스 
        #사용자에게 정보를 제공 질문과 응답을 할 수 있는 대화창
         
 response = QMessageBox.question(self,"메세지","정말 나가려구?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)          print(response)
        if response == QMessageBox.Yes:
            print("나가지마")
            QCoreApplication.instance().quit()


    def initUI(self):
        #창의 타이틀 지정
        #푸쉬버튼 객체 생성
        labelId = QLabel("ID",self)
        labelPw = QLabel("PW",self)
        

        labelId.move(400,330)
        labelPw.move(400,430)
        labelId.resize(120,50)
        labelPw.resize(120,50)
        
        font1 =labelId.font()
        font1.setPointSize(30)

        font2 =labelPw.font()
        font2.setPointSize(30)

        labelId.setFont(font1)
        labelPw.setFont(font2)

        #qlineedit
        self.leId = QLineEdit(self)
        self.lePw = QLineEdit(self)
        
        self.leId.move(500,340)
        self.lePw.move(500,440)
        self.leId.resize(320,30)
        self.lePw.resize(320,30)

        
        self.setWindowTitle("와.. 금요일이다..불금불금")
        self.resize(1200,800)            #사이즈 조절
        self.move(300,400)               #창이동
        #화면에 나오게함
  
        btn1 = QPushButton("출력",self)
        btn1.setText("Login")
        btn1.resize(120,80)
        btn1.move(500,500)
        
        btn1.clicked.connect(self.print)
        #이벤트 핸들러

        btn2 = QPushButton("exit",self)
        btn2.resize(120,80)
        btn2.move(700,500)

        # btn2.clicked.connect(QCoreApplication.instance().quit)
        btn2.clicked.connect(self.close)  # close 함수에 연결

    


        self.show()
if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
