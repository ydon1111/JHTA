import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100,100,900,900)
        self.setWindowTitle("제목 없음 - windows 메모장")
        self.setWindowIcon(QIcon("./img/note.jpeg"))

        newFile = QAction(QIcon("./img/notenew.png"),"새파일",self)
        newFile.setShortcut("Ctrl+N")
        newFile.setStatusTip("새 파일")
        newFile.triggered.connect(self.newFile)
        
        openFile = QAction(QIcon("./img/noteopen.png"),"열기",self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("새 파일 열기")
        openFile.triggered.connect(self.showDialog)

        closeFile = QAction(QIcon("./img/noteend.png"),"종료",self)
        closeFile.setShortcut("Ctrl+X")
        closeFile.setStatusTip("종료")
        closeFile.triggered.connect(QCoreApplication.instance().quit)

        saveFile = QAction(QIcon("./img/notesave.png"),"저장",self)
        saveFile.setShortcut("Ctrl+s")
        saveFile.setStatusTip("저장")
        saveFile.triggered.connect(self.saveDialog)
        


        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(newFile)      
        fileMenu.addAction(openFile)  
        fileMenu.addAction(saveFile)
        fileMenu.addAction(closeFile)
        

        fontMenu = QAction(QIcon("./img/font.png"),"글꼴",self)
        fontMenu.setShortcut("Ctrl+F")
        fontMenu.setStatusTip("글꼴")
        fontMenu.triggered.connect(self.changeFont)

        formMenu = menubar.addMenu("&서식")
        formMenu.addAction(fontMenu)


    def changeFont(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'open file',"./")
        print(fname)
        
        if fname[0]:
            f = open(fname[0],'r',encoding="utf-8")
            with f:
                data = f.read()
                self.textEdit.setText(data)
                name = fname[0].split("/")
                self.setWindowTitle(name[-1].split(".")[0]+ "- windows 메모장")

    
    def saveDialog(self):       
        sname = QFileDialog.getSaveFileName(self,'save file',"./")
        with open(sname[0],'w') as f:
            f.write(self.textEdit.toPlainText())
        
  
    def newFile(self):
        txt = self.textEdit.toPlainText()
        if len(txt) != 0:
            response = QMessageBox.question(self,"메시지","변경내용을 제목없음에 저장하시겠습니까?",QMessageBox.Yes | QMessageBox.No |QMessageBox.Cancel, QMessageBox.Cancel)
            if response == QMessageBox.Yes:
                self.saveDialog()

        self.textEdit.setText("")

        #textEdit 에 내용이 있는지를 판단해서
        #내용이 존재한다면
        #저장할것인지를 물어보기 저장한후에 지우기
        #내용이 없으면 그냥 지우기
        self.textEdit.setText("")

       




if __name__ == "__main__":
    app = QApplication(sys.argv)
    my = MyApp()
    sys.exit(app.exec_())