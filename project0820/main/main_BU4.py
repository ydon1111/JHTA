import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from common.DBconnect import *

class main():
    def setupUI(self, HomeWindow):
        HomeWindow.setWindowTitle("날씨")
        
        self.centralwidget = QWidget(HomeWindow)
        HomeWindow.setCentralWidget(self.centralwidget)
        
        self.initUI(HomeWindow)
        
        self.weather_func()

        self.rw_btn_setting(HomeWindow)
    
    def logout(self, HomeWindow):
        res = QMessageBox.question(self.centralwidget, "로그아웃", "로그아웃 하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if res == QMessageBox.Yes: HomeWindow.start_login()
        
    def initUI(self, HomeWindow):
        self.vbox = QVBoxLayout()
        self.toolbarUI(HomeWindow)
        self.whUI()
        self.rcdUI()
        self.centralwidget.setLayout(self.vbox)
        self.set_style()
        self.music_play()
    
    def set_style(self):
        font = QFont("1훈정글북 Regular")
        logout_style = "width: 80px; height: 30px; color: #1E90FF; border: 2px #1E90FF solid; border-radius: 3px; background-color: #FFFFFF; font-size: 12pt;"
        loc_radio_style = "font-size: 12pt; color: #4C4C4C;"
        rw_lb_style = "font-size: 10pt; color: #4C4C4C; font-weight: bold;"
        rgt_style = "width: 80px; height: 30px; color: #006400; border: 2px #006400 solid; border-radius: 3px; background-color: #13C7A3; font-size: 12pt;"
        wrg_style = "width: 80px; height: 30px; color: #006400; border: 2px #006400 solid; border-radius: 3px; background-color: #E68282; font-size: 12pt;"
        rcd_title_style = "font-size: 14pt; color: #B9062F; font-weight: bold;border-style: solid; border-width: 2px; border-color: #B9062F; border-radius: 10px"
        music_style = "width: 80px; height: 30px; color: #FFFFFF; border: 2px #1E90FF solid; border-radius: 3px; background-color: #FF8C0A; font-size: 12pt;"
        food_style = "width: 80px; height: 30px; color: #FFFFFF; border: 2px #1E90FF solid; border-radius: 3px; background-color: #0064DC; font-size: 12pt;"
        activity_style = "width: 80px; height: 30px; color: #FFFFFF; border: 2px #1E90FF solid; border-radius: 3px; background-color: #5A5AFF; font-size: 12pt;"
        
        self.logout_btn.setStyleSheet(logout_style)
        self.logout_btn.setFont(font)
        self.m_ro_seoul.setStyleSheet(loc_radio_style)
        self.m_ro_seoul.setFont(font)
        self.m_ro_gangneung.setStyleSheet(loc_radio_style)
        self.m_ro_gangneung.setFont(font)
        self.m_ro_deajeon.setStyleSheet(loc_radio_style)
        self.m_ro_deajeon.setFont(font)
        self.m_ro_gwangju.setStyleSheet(loc_radio_style)
        self.m_ro_gwangju.setFont(font)
        self.m_ro_ulsan.setStyleSheet(loc_radio_style)
        self.m_ro_ulsan.setFont(font)
        
        self.rw_lb.setStyleSheet(rw_lb_style)
        self.rw_lb.setFont(font)
        self.rgt_btn.setStyleSheet(rgt_style)
        self.rgt_btn.setFont(font)
        self.wrg_btn.setStyleSheet(wrg_style)
        self.wrg_btn.setFont(font)
        
        self.rcd_title.setStyleSheet(rcd_title_style)
        self.rcd_title.setFont(font)
        self.music.setStyleSheet(music_style)
        self.music.setFont(font)
        self.food.setStyleSheet(food_style)
        self.food.setFont(font)
        self.activity.setStyleSheet(activity_style)
        self.activity.setFont(font)
        
    def toolbarUI(self, HomeWindow):
        # toolbar 박스
        self.tbar_box = QHBoxLayout()
        
        # LOGO 이미지
        self.m_img_logo = QLabel("title", self.centralwidget)
        m_logo_pixmap = QPixmap("./project0820/img/title.png")
        m_logo_pixmap = m_logo_pixmap.scaled(50, 30)
        self.m_img_logo.setPixmap(m_logo_pixmap)
        self.tbar_box.addWidget(self.m_img_logo)
        
        # 지역 라디오버튼
        self.loc_box = QHBoxLayout()
        self.m_ro_seoul = QRadioButton('서울', self.centralwidget)
        self.m_ro_seoul.setChecked(True)
        self.loc_box.addWidget(self.m_ro_seoul)
        self.m_ro_gangneung = QRadioButton('강릉', self.centralwidget)
        self.loc_box.addWidget(self.m_ro_gangneung)
        self.m_ro_deajeon = QRadioButton('대전', self.centralwidget)
        self.loc_box.addWidget(self.m_ro_deajeon)
        self.m_ro_gwangju = QRadioButton('광주', self.centralwidget)
        self.loc_box.addWidget(self.m_ro_gwangju)
        self.m_ro_ulsan = QRadioButton('울산', self.centralwidget)
        self.loc_box.addWidget(self.m_ro_ulsan)
        self.tbar_box.addLayout(self.loc_box)
        
        # 맞아, 틀려 버튼
        self.rw_btn_box = QHBoxLayout()
        self.rw_lb = QLabel("현재 날씨가 맞나요? ", self.centralwidget)
        self.rw_btn_box.addWidget(self.rw_lb)
        self.rgt_btn = QPushButton("맞아요", self.centralwidget)
        self.rgt_btn.clicked.connect(lambda: self.rgt_click("R", HomeWindow))
        self.rgt_btn.setFixedSize(100, 30)
        self.rw_btn_box.addWidget(self.rgt_btn)
        self.wrg_btn = QPushButton("틀려요", self.centralwidget)
        self.wrg_btn.clicked.connect(lambda: self.rgt_click("W", HomeWindow))
        self.wrg_btn.setFixedSize(100, 30)
        self.rw_btn_box.addWidget(self.wrg_btn)
        self.tbar_box.addLayout(self.rw_btn_box)
        
        self.tbar_box.addStretch(1)
        
        # 로그아웃 버튼
        self.logout_btn = QPushButton("로그아웃", self.centralwidget)
        self.logout_btn.setFixedSize(100, 30)
        self.logout_btn.clicked.connect(lambda: self.logout(HomeWindow))
        self.tbar_box.addWidget(self.logout_btn)

        self.vbox.addLayout(self.tbar_box)
        
    def whUI(self):
        p_img1 = QPixmap("./project0820/img/sun.png")
        p_img2 = QPixmap("./project0820/img/rain.png")
        
        #수평상자 레이아웃 객체         
        self.wh_box = QHBoxLayout() # 최상위 box
        self.wh_scrollArea = QScrollArea() # 스크롤
        self.wh_in_box = QHBoxLayout() # 스크롤 안 박스

        self.tn_box = QHBoxLayout() # 오늘, 내일, 모레 날씨 박스
        for i in range(3):
            self.lb = QLabel("aaaaaaaaaaa", self.centralwidget)
            self.lb.setPixmap(p_img1)
            self.lb.resize(300, 300)
            self.tn_box.addWidget(self.lb)
        
        self.wh_in_box.addLayout(self.tn_box)
        
        # 주간 날씨 박스
        self.week_box = QVBoxLayout()
        self.ko_week_box = QHBoxLayout()
        self.no_week_box = QHBoxLayout()
        
        for i in range(5):
            self.lb4 = QLabel("aaaaaaaaaaa", self.centralwidget)
            self.lb4.setPixmap(p_img2)
            self.lb4.resize(300, 300)
            self.ko_week_box.addWidget(self.lb4)
        self.week_box.addLayout(self.ko_week_box)
        
        for i in range(5):
            self.lb4 = QLabel("aaaaaaaaaaa", self.centralwidget)
            self.lb4.setPixmap(p_img2)
            self.lb4.resize(300, 300)
            self.no_week_box.addWidget(self.lb4)
        self.week_box.addLayout(self.no_week_box)
        
        self.wh_in_box.addLayout(self.week_box)
        
        self.wh_scrollArea.setLayout(self.wh_in_box)
        # wh_box.addStretch(1)
        self.wh_box.addWidget(self.wh_scrollArea)

        self.vbox.addLayout(self.wh_box)
        
    def rw_btn_setting(self, HomeWindow):
        self.temp_tnwh_no = 471
        res = excute("SELECT * FROM SM_RPU_TB WHERE RPU_TNWH_NO = :temp_tnwh_no ", [self.temp_tnwh_no])
        if len(res) > 0: self.hide_rw()
    
    def rgt_click(self, type, HomeWindow):
        self.temp_tnwh_no = 471
        rpu_res = 1
        if type == "W": rpu_res = 2
        
        res = excute("SELECT * FROM SM_RPU_TB WHERE RPU_TNWH_NO = :temp_tnwh_no ", [self.temp_tnwh_no])
        if len(res) < 1:
            res = excute("INSERT INTO SM_RPU_TB(RPU_NO, RPU_TNWH_NO, RPU_USER_NO, RPU_RES) VALUES(SM_RPU_SEQ.NEXTVAL, :temp_tnwh_no, :rpu_res)",
                   [self.temp_tnwh_no,rpu_res])
            if res: 
                QMessageBox.question(self.centralwidget, "현재 날씨", "소중한 의견 갑사합니다. 선택한 의견은 기상청 신뢰도에 반영됩니다.", QMessageBox.Yes, QMessageBox.Yes)
                self.hide_rw()
    
    def hide_rw(self):
        self.rw_lb.hide()
        self.rgt_btn.hide()
        self.wrg_btn.hide()
        
        
    def rcdUI(self):
        self.rcd_title = QLabel("이거\n어때요?", self.centralwidget)
        self.rcd_title.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        
        self.music = QPushButton("노래", self.centralwidget)
        self.music.clicked.connect(self.music_play)
        self.food = QPushButton("음식", self.centralwidget)
        self.food.clicked.connect(self.food_play)
        self.activity = QPushButton("활동", self.centralwidget)
        self.activity.clicked.connect(self.activity_play)
        
        # click_pixmap = QPixmap("./project0820/img/btn_click.png")
        # click_pixmap = click_pixmap.scaled(30, 30)
        
        # self.music_click_img = QLabel("MUSIC_CLICK", self.centralwidget)
        # self.music_click_img.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        # self.music_click_img.setPixmap(click_pixmap)
        
        # self.food_click_img = QLabel("FOOD_CLICK", self.centralwidget)
        # self.food_click_img.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        # self.food_click_img.setPixmap(click_pixmap)
        
        # self.activity_click_img = QLabel("ACTIVITY_CLICK", self.centralwidget)
        # self.activity_click_img.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        # self.activity_click_img.setPixmap(click_pixmap)
        
        self.scrollArea_box = QScrollArea()
        self.scrollArea_box.setWidgetResizable(True)
        self.grid1 = QGridLayout()
        
        self.temp_lab = QLabel("", self.centralwidget)
        self.temp_lab.resize(30, 30)
        
        self.grid1.addWidget(self.rcd_title, 0, 0, 1, 1)
        # self.grid1.addWidget(self.music_click_img, 1, 0, 2, 1)
        self.grid1.addWidget(self.music, 2, 0, 1, 1)
        # self.grid1.addWidget(self.food_click_img, 3, 0, 2, 1)
        self.grid1.addWidget(self.food, 4, 0, 1, 1)
        # self.grid1.addWidget(self.activity_click_img, 5, 0, 2, 1)
        self.grid1.addWidget(self.activity, 6, 0, 1, 1)
        self.grid1.addWidget(self.temp_lab, 7, 0, 2, 1)
        
        self.rcd_box = QHBoxLayout()
        self.rcd_box.addLayout(self.grid1)
        self.rcd_box.addWidget(self.scrollArea_box)

        self.widget_youtube1 = QWidget(self.centralwidget)
        self.webview1=QWebEngineView(self.widget_youtube1)
        self.widget_youtube2 = QWidget(self.centralwidget)
        self.webview2=QWebEngineView(self.widget_youtube2)
        self.widget_youtube3 = QWidget(self.centralwidget)
        self.webview3=QWebEngineView(self.widget_youtube3)
        self.widget_youtube4 = QWidget(self.centralwidget)
        self.webview4=QWebEngineView(self.widget_youtube4)
        self.widget_youtube5 = QWidget(self.centralwidget)
        self.webview5=QWebEngineView(self.widget_youtube5)
        
        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.webview1)
        self.h_box.addWidget(self.webview2)
        self.h_box.addWidget(self.webview3)
        self.h_box.addWidget(self.webview4)
        self.h_box.addWidget(self.webview5)
        self.scrollArea_box.setLayout(self.h_box)

        self.vbox.addLayout(self.rcd_box)
    
    def music_play(self):
        sql = "SELECT RCD_URL FROM SM_RCD_TB WHERE RCD_TYPE = :txt and RCD_TNWH_NO = :txt2"
        res = excute(sql, [1,555])
        # print(res)
        
        self.toggle("Y")
        self.webview1.setUrl(QUrl(res[0][0]))
        self.webview2.setUrl(QUrl(res[1][0])) 
        self.webview3.setUrl(QUrl(res[2][0]))  
        self.webview4.setUrl(QUrl(res[3][0]))  
        self.webview5.setUrl(QUrl(res[4][0]))  

    def food_play(self):
        sql = "SELECT RCD_URL FROM SM_RCD_TB WHERE RCD_TYPE = :txt and  RCD_TNWH_NO = :txt2"
        res = excute(sql, [3,555])
        # print(res)
        
        self.toggle("Y")
        self.webview1.setUrl(QUrl(res[0][0]))
        self.webview2.setUrl(QUrl(res[1][0])) 
        self.webview3.setUrl(QUrl(res[2][0]))  
        self.webview4.setUrl(QUrl(res[3][0]))  
        self.webview5.setUrl(QUrl(res[4][0]))  
        
    def activity_play(self):
        
        sql = "SELECT RCD_URL FROM SM_RCD_TB WHERE RCD_TYPE = :txt and RCD_TNWH_NO = :txt2"
        res = excute(sql, [2,555])
        # print(res)

        self.webview1.setUrl(QUrl(res[0][0]))
        self.webview2.setUrl(QUrl(res[0][0])) 
        self.webview3.setUrl(QUrl(res[0][0]))  
        self.webview4.setUrl(QUrl(res[0][0]))  
        self.webview5.setUrl(QUrl(res[0][0]))  


        self.toggle("N")
        
    def toggle(self, type):
        if type == "Y" :
            self.webview2.show()
            self.webview3.show()
            self.webview4.show()
            self.webview5.show()
        else:
            self.webview2.hide()
            self.webview3.hide()
            self.webview4.hide()
            self.webview5.hide()
        
    def weather_func(self):
        ##########################도현 steart###########################
        print("날씨")
        ############################도현 end############################
    

            
        
        