import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cx_Oracle
from DbConnect import DbConnect


class WindowWidget(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI2()
    # QWidget
    # 위젯은 화면에 표시할 수 있는 것을 목적으로 한다. 
    # 윈도우나 버튼 모든 위젯 화면에 무언가를 표시하거나 키보드 or 마우스에서
    # 사용자의 입력을 받아들이는것 , 버튼, 슬라이드 ,뷰, 대화상자등등 사용자의 상호 작용을 나타내는 사각형영역


    # QMainWindow
    # 메인 창에서는 최상위 위젯이고 메뉴바, 도구모음, 상태표시줄 을 포함하는
    # 미리 정의된 레이아웃을 가지고 있다.
    # 창은 부모/자식의 상단이며 일반적으로 제목 표시줄과 테두리를 표시

    # QDialog
    # 특수한 종류의 창 으로 보통 일시적 
    # 알림, 입력, 선택
    

    def initUI2(self):
        
        self.leIdRg = QLineEdit(self)
        self.lePwRg = QLineEdit(self)
        self.leNaRg = QLineEdit(self)     
     
        self.labelIdRg = QLabel("ID",self)
        self.labelPwRg = QLabel("PW",self)
        self.labelNaRg = QLabel("NAME",self)

        self.btnRegDa = QPushButton("가입하기",self)
        self.btnCancel  = QPushButton("취소",self)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.leIdRg,0,1)
        grid.addWidget(self.labelIdRg,0,0)
        grid.addWidget(self.lePwRg,1,1)
        grid.addWidget(self.labelPwRg,1,0)
        grid.addWidget(self.leNaRg,2,1)
        grid.addWidget(self.labelNaRg,2,0)
        grid.addWidget(self.btnRegDa,3,0)
        grid.addWidget(self.btnCancel,3,1)
   

   
        
        self.btnRegDa.clicked.connect(self.registerDa)
        self.btnCancel.clicked.connect(self.Cancel)
        
        self.show()
    
    def registerDa(self):
        connection = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
        cur = connection.cursor()
        sql="""
            INSERT INTO member(id,pw,name) VALUES (:id,:pw,:name)
        """
        cur.execute(sql,id=self.leIdRg.text(),pw=self.lePwRg.text(),name=self.leNaRg.text())
        connection.commit()
        connection.close()
        self.parent.hide()
        
    def Cancel(self):    
        self.parent.hide()
        # QCoreApplication.instance().quit()
        #이거 창만 꺼지게는 어떻게하지?
        #parent 값을 만들어서 연결시켜줌
        



class WindowReg(QMainWindow):
    def __init__(self,parent):
        super().__init__(parent)
        self.setGeometry(50,50,300,400)
        self.setCentralWidget(WindowWidget(self)) #외부에서 위젯가져오기
        
        self.setWindowTitle("회원가입")
        # self.initUI2() #내부에서 만들기 
       

    def initUI2(self):
        self.setWindowTitle("회원가입")
        self.setGeometry(200,200,600,600)

        self.leIdRg = QLineEdit(self)
        self.lePwRg = QLineEdit(self)
        self.leNaRg = QLineEdit(self)     
     
        self.labelIdRg = QLabel("ID",self)
        self.labelPwRg = QLabel("PW",self)
        self.labelNaRg = QLabel("NAME",self)


        self.btnRegDa = QPushButton("가입하기",self)
        self.btnCancel  = QPushButton("취소",self)

        self.leIdRg.move(50,50)
        self.lePwRg.move(50,100)
        self.leNaRg.move(50,150)   
     
        self.labelIdRg.move(10,50)
        self.labelPwRg.move(10,100)
        self.labelNaRg.move(10,150)


        self.btnRegDa.move(150,200)
        self.btnCancel.move(150,250)

        self.btnRegDa.clicked.connect(self.registerDa)
        self.btnCancel.clicked.connect(self.Cancel)
        
        self.show()  
   
   
    def registerDa(self):
        connection = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
        cur = connection.cursor()
        sql="""
            INSERT INTO member(id,pw,name) VALUES (:id,:pw,:name)
        """
        cur.execute(sql,id=self.leIdRg.text(),pw=self.lePwRg.text(),name=self.leNaRg.text())
        connection.commit()
        connection.close()
        self.hide()

    def Cancel(self):
        self.hide()



class MyApp(QWidget):
    #. LayOut : BoxLayout , 수평 상자, 수직 상자


    def __init__(self):
        super().__init__()
        self.initUI()

    def dbCheck(self):
        print("id")
        connection = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
        print(connection)   
#1. connection  객체 생성
#2. cursor 객체
        cur = connection.cursor()
#3. 사용할 sql문 객
#  :  <== 바인드변수  매개변수 입력 
        sql = """select id,pw,name,grade 
                from member
                where id = :id and pw = :pw
                """ 
#4. 실행
        cur.execute(sql,id=self.leId.text(),pw=self.lePw.text())
        #print(cur)
#5. 로직처리 
        for dbid,dbpw,name,grade in cur:
            # print(id,pw)
            if dbid!=None:
                rep = QMessageBox.question(self,"로그인 성공",'환영합니다',QMessageBox.Yes)  #Yes 앞에 대문자로 해야 나옴 No 도 같음
                
                # print("로그인성공")


#6. 자원반납 
        connection.close()




    
    def register(self):
        self.rg = WindowReg(self)

        self.rg.show()       
    




    def initUI(self):
        #수평상자 레이아웃 객체

     
        self.leId = QLineEdit(self)
        self.lePw = QLineEdit(self)     
     
        self.labelId = QLabel("ID",self)
        self.labelPw = QLabel("PW",self)



    #QLineEdit


        self.btnLogin = QPushButton("로그인",self)
        self.btnReg  = QPushButton("회원가입",self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.labelId)
        hbox.addWidget(self.leId)
        hbox.addStretch(1)
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.labelPw)
        hbox2.addWidget(self.lePw)
        hbox2.addStretch(1)
        
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.btnLogin)
        hbox3.addWidget(self.btnReg)
        hbox3.addStretch(1)
        
        vbox = QVBoxLayout()
        
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)              
        vbox.addLayout(hbox3) 
   
        self.setLayout(vbox)
        


        
        self.btnLogin.clicked.connect(self.dbCheck)
        self.btnReg.clicked.connect(self.register)


        self.setWindowTitle("로그인")
        self.resize(300,300)
        
        

        
        self.show()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
       
        


    #창 타이틀 지정
    #창 사이즈 결정
    #창 위치 결정

    #화면에 보여지게 설정

    #현재 파일에서 호출시에만 실행가능하게 설정 