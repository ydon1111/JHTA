import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from common.DBconnect import *
from datetime import date,datetime,timedelta 
today=date.today().isoformat()

class main():
    def setupUI(self, HomeWindow):
        HomeWindow.setWindowTitle("날씨")
        
        self.centralwidget = QWidget(HomeWindow)
        HomeWindow.setCentralWidget(self.centralwidget)
        
        self.initUI(HomeWindow)
        
        self.weather_func()
        self.recomm_func()
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
        self.set_base_style()
        self.set_tnw_style()
        self.music_play()
        
    
    def set_base_style(self):
        logout_style = "width: 80px; height: 30px; color: #1E90FF; border: 2px #1E90FF solid; border-radius: 3px; background-color: #FFFFFF; font-size: 12pt;"
        loc_radio_style = "font-size: 12pt;"
        rw_lb_style = "font-size: 10pt; color: #4C4C4C; font-weight: bold;"
        rgt_style = "width: 80px; height: 30px; color: #006400; border: 2px #006400 solid; border-radius: 3px; background-color: #13C7A3; font-size: 12pt;"
        wrg_style = "width: 80px; height: 30px; color: #006400; border: 2px #006400 solid; border-radius: 3px; background-color: #E68282; font-size: 12pt;"
        rcd_title_style = "font-size: 14pt; color: #B9062F; font-weight: bold;border-style: solid; border-width: 2px; border-color: #B9062F; border-radius: 10px"
        music_style = "width: 80px; height: 30px; color: #FFFFFF; border: 2px #1E90FF solid; border-radius: 3px; background-color: #FF8C0A; font-size: 12pt;"
        food_style = "width: 80px; height: 30px; color: #FFFFFF; border: 2px #1E90FF solid; border-radius: 3px; background-color: #0064DC; font-size: 12pt;"
        activity_style = "width: 80px; height: 30px; color: #FFFFFF; border: 2px #1E90FF solid; border-radius: 3px; background-color: #5A5AFF; font-size: 12pt;"
        
        self.logout_btn.setStyleSheet(logout_style)
        self.m_ro_seoul.setStyleSheet(loc_radio_style)
        self.m_ro_gangneung.setStyleSheet(loc_radio_style)
        self.m_ro_deajeon.setStyleSheet(loc_radio_style)
        self.m_ro_gwangju.setStyleSheet(loc_radio_style)
        self.m_ro_ulsan.setStyleSheet(loc_radio_style)
        
        self.rw_lb.setStyleSheet(rw_lb_style)
        self.rgt_btn.setStyleSheet(rgt_style)
        self.wrg_btn.setStyleSheet(wrg_style)
        
        self.rcd_title.setStyleSheet(rcd_title_style)
        self.music.setStyleSheet(music_style)
        self.food.setStyleSheet(food_style)
        self.activity.setStyleSheet(activity_style)
        
    def toolbarUI(self, HomeWindow):
        # toolbar 박스
        self.tbar_box = QHBoxLayout()
        
        # LOGO 이미지
        self.m_img_logo = QLabel("title", self.centralwidget)
        m_logo_pixmap = QPixmap("./project/img/title.png")
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
        
    def set_tnw_style(self):
        t_title_lb_style = "font-family: '1훈정글북 Regular'; font-size: 12pt; color: #FFFFFF; font-weight: bold; background-color: #FF3232; border-radius: 3px;"
        to_title_lb_style = "font-family: '1훈정글북 Regular'; font-size: 12pt; color: #FFFFFF; font-weight: bold; background-color: #FFB400; border-radius: 3px; padding:0px;"
        dat_title_lb_style = "font-family: '1훈정글북 Regular'; font-size: 12pt; color: #FFFFFF; font-weight: bold; background-color: #FFD228; border-radius: 3px; padding:0px;"
        tn_lb_style = "font-family: '1훈정글북 Regular'; font-size: 10pt; color: #4C4C4C;"
        tn_s_lb_style = "font-family: '나눔고딕'; font-size: 9pt; color: #505050;"

        self.line1.setStyleSheet("color: red; font-size: 2pt; padding: 0; margin: 0;")
        
        # 오늘 현재 label style
        self.tdate_lb.setStyleSheet(t_title_lb_style)
        self.tdate_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        self.tdraw_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        self.ttemp_lb.setStyleSheet(tn_lb_style)
        self.ttemp_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        self.train_lb.setStyleSheet(tn_lb_style)
        self.train_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        self.twind_lb.setStyleSheet(tn_lb_style)
        self.twind_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        # 오늘 시간별 label style
        self.tfull1_lb.setStyleSheet(tn_lb_style)
        self.tfull1_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        self.tfull2_lb.setStyleSheet(tn_lb_style)
        self.tfull2_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        self.tfull3_lb.setStyleSheet(tn_lb_style)
        self.tfull3_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        self.tfull4_lb.setStyleSheet(tn_lb_style)
        self.tfull4_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        # 오늘 00:00 - 06:00 label style
        self.tfull_0w_tlb.setStyleSheet(tn_s_lb_style)
        # self.tfull_0w_plb.setStyleSheet(tn_s_lb_style)
        self.tfull_0w_rlb.setStyleSheet(tn_s_lb_style)
        self.tfull_0w_wlb.setStyleSheet(tn_s_lb_style)
        
        # 오늘 06:00 - 12:00 albel style
        self.tfull_6w_tlb.setStyleSheet(tn_s_lb_style)
        # self.tfull_6w_plb.setStyleSheet(tn_s_lb_style)
        self.tfull_6w_rlb.setStyleSheet(tn_s_lb_style)
        self.tfull_6w_wlb.setStyleSheet(tn_s_lb_style)
        
        # 오늘 12:00 - 18:00 albel style
        self.tfull_12w_tlb.setStyleSheet(tn_s_lb_style)
        # self.tfull_12w_plb.setStyleSheet(tn_s_lb_style)
        self.tfull_12w_rlb.setStyleSheet(tn_s_lb_style)
        self.tfull_12w_wlb.setStyleSheet(tn_s_lb_style)
        
        # 오늘 18:00 - 24:00 albel style
        self.tfull_18w_tlb.setStyleSheet(tn_s_lb_style)
        # self.tfull_18w_plb.setStyleSheet(tn_s_lb_style)
        self.tfull_18w_rlb.setStyleSheet(tn_s_lb_style)
        self.tfull_18w_wlb.setStyleSheet(tn_s_lb_style)
        
        # 내일 날씨
        self.todate_lb.setStyleSheet(to_title_lb_style)
        self.todate_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        self.tm1_tlb.setStyleSheet(tn_lb_style)
        
        # // tm1_telb tm1_rlb tm1_wlb
        
        # 모래 날씨
        self.datdate_lb.setStyleSheet(dat_title_lb_style)
        self.datdate_lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
    def whUI(self):
        p_img1 = QPixmap("./project/img/sun.png")
        p_img2 = QPixmap("./project/img/rain.png")
        p_cloud_L = QPixmap("./project/img/weather/w3.png").scaled(50, 35)
        p_cloud_S = QPixmap("./project/img/weather/w3.png").scaled(50, 35)
        
        self.line1 = QLabel("--------------------------------------------------------------------------------------------------------------------", self.centralwidget)
        
        #수평상자 레이아웃 객체         
        self.wh_box = QHBoxLayout() # 최상위 box
        self.wh_scrollArea = QScrollArea() # 스크롤
        self.wh_in_box = QHBoxLayout() # 스크롤 안 박스

        ######
        self.today_box=QVBoxLayout() #오늘 전체박스
        
        self.now_box=QVBoxLayout() #오늘=>현재시간대 날씨박스

        self.tn_box = QHBoxLayout() # 오늘, 내일, 모레 날씨 박스

        now=excute("select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND from SM_TNWH_TB where tnwh_no = (select max(tnwh_no) from sm_tnwh_tb where tnwh_type = :num)", [3])

        ######################################################################오늘=>현재
        self.tdate_lb=QLabel("오늘",self.centralwidget)
        self.tdraw_lb=QLabel(str(now[0][0]),self.centralwidget) # 흐림
        self.tdraw_lb.setPixmap(p_cloud_L)
        self.ttemp_lb=QLabel(str(now[0][1])+"℃",self.centralwidget)
        self.train_lb=QLabel(str(now[0][2])+"mm",self.centralwidget)
        self.twind_lb=QLabel(str(now[0][3])+"m/s",self.centralwidget)

        self.now_box.addWidget(self.tdate_lb)
        self.now_box.addWidget(self.ttemp_lb)
        self.now_box.addWidget(self.tdraw_lb)
        self.now_box.addWidget(self.train_lb)
        self.now_box.addWidget(self.twind_lb)
        self.now_box.addWidget(self.line1)

        
        ######################################################################오늘=>전체시간대 날씨박스
        self.full_box=QHBoxLayout()

        # 시간
        self.tfull_box1=QVBoxLayout()
        self.tfull1_lb=QLabel("00:00\n-\n06:00",self.centralwidget)
        self.tfull2_lb=QLabel("06:00\n-\n12:00",self.centralwidget)
        self.tfull3_lb=QLabel("12:00\n-\n18:00",self.centralwidget)
        self.tfull4_lb=QLabel("18:00\n-\n24:00",self.centralwidget)
        self.tfull_box1.addWidget(self.tfull1_lb)
        self.tfull_box1.addWidget(self.tfull2_lb)
        self.tfull_box1.addWidget(self.tfull3_lb)
        self.tfull_box1.addWidget(self.tfull4_lb)

        self.tfull_box2=QVBoxLayout()

        self.tfull_0box=QHBoxLayout()
        self.tfull_6box=QHBoxLayout()
        self.tfull_12box=QHBoxLayout()
        self.tfull_18box=QHBoxLayout()

        # 00:00 - 06:00
        self.tfull_0box1=QVBoxLayout()
        self.tfull_0d_lb=QLabel("00:06 날씨그림",self.centralwidget)
        self.tfull_0d_lb.setPixmap(p_cloud_S)
        self.tfull_0box1.addWidget(self.tfull_0d_lb)
        
        #왼 그림//오 기온,강수확률,강수량,풍속
        # self.tfull_0box2.
        
        
        self.tfull_0box2=QVBoxLayout()
        self.tfull_0w_tlb=QLabel("25℃",self.centralwidget)
        # self.tfull_0w_plb=QLabel("",self.centralwidget)
        self.tfull_0w_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.tfull_0w_wlb=QLabel("10m/s",self.centralwidget)
        self.tfull_0box2.addWidget(self.tfull_0w_tlb)
        # self.tfull_0box2.addWidget(self.tfull_0w_plb)
        self.tfull_0box2.addWidget(self.tfull_0w_rlb)
        self.tfull_0box2.addWidget(self.tfull_0w_wlb)
        self.tfull_0box.addLayout(self.tfull_0box1)
        self.tfull_0box.addLayout(self.tfull_0box2)

        # 06:00 - 12:00
        self.tfull_6box1=QVBoxLayout()
        self.tfull_6d_lb=QLabel("06:12 날씨그림",self.centralwidget)
        self.tfull_6d_lb.setPixmap(p_cloud_S)
        self.tfull_6box1.addWidget(self.tfull_6d_lb)

        self.tfull_6box2=QVBoxLayout()
        self.tfull_6w_tlb=QLabel("25℃",self.centralwidget)
        # self.tfull_6w_plb=QLabel("",self.centralwidget)
        self.tfull_6w_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.tfull_6w_wlb=QLabel("10m/s",self.centralwidget)
        self.tfull_6box2.addWidget(self.tfull_6w_tlb)
        # self.tfull_6box2.addWidget(self.tfull_6w_plb)
        self.tfull_6box2.addWidget(self.tfull_6w_rlb)
        self.tfull_6box2.addWidget(self.tfull_6w_wlb)
        self.tfull_6box.addLayout(self.tfull_6box1)
        self.tfull_6box.addLayout(self.tfull_6box2)

        # 12:00 - 18:00
        self.tfull_12box1=QVBoxLayout()
        self.tfull_12d_lb=QLabel("12:18 날씨그림",self.centralwidget)
        self.tfull_12d_lb.setPixmap(p_cloud_S)
        self.tfull_12box1.addWidget(self.tfull_12d_lb)

        self.tfull_12box2=QVBoxLayout()
        self.tfull_12w_tlb=QLabel("25℃",self.centralwidget)
        # self.tfull_12w_plb=QLabel("12:18 강수확률",self.centralwidget)
        self.tfull_12w_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.tfull_12w_wlb=QLabel("10m/s",self.centralwidget)
        self.tfull_12box2.addWidget(self.tfull_12w_tlb)
        # self.tfull_12box2.addWidget(self.tfull_12w_plb)
        self.tfull_12box2.addWidget(self.tfull_12w_rlb)
        self.tfull_12box2.addWidget(self.tfull_12w_wlb)

        self.tfull_12box.addLayout(self.tfull_12box1)
        self.tfull_12box.addLayout(self.tfull_12box2)

        # 18:00 - 24:00
        self.tfull_18box1=QVBoxLayout()
        self.tfull_18d_lb=QLabel("18:24 날씨그림",self.centralwidget)
        self.tfull_18d_lb.setPixmap(p_cloud_S)
        self.tfull_18box1.addWidget(self.tfull_18d_lb)

        self.tfull_18box2=QVBoxLayout()
        self.tfull_18w_tlb=QLabel("25℃",self.centralwidget)
        # self.tfull_18w_plb=QLabel("18:24 강수확률",self.centralwidget)
        self.tfull_18w_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.tfull_18w_wlb=QLabel("10m/s",self.centralwidget)
        self.tfull_18box2.addWidget(self.tfull_18w_tlb)
        # self.tfull_18box2.addWidget(self.tfull_18w_plb)
        self.tfull_18box2.addWidget(self.tfull_18w_rlb)
        self.tfull_18box2.addWidget(self.tfull_18w_wlb)

        self.tfull_18box.addLayout(self.tfull_18box1)
        self.tfull_18box.addLayout(self.tfull_18box2)

        self.tfull_box2.addLayout(self.tfull_0box)
        self.tfull_box2.addLayout(self.tfull_6box)
        self.tfull_box2.addLayout(self.tfull_12box)
        self.tfull_box2.addLayout(self.tfull_18box)

        self.full_box.addLayout(self.tfull_box1)
        self.full_box.addLayout(self.tfull_box2)

        self.today_box.addLayout(self.now_box)
        self.today_box.addLayout(self.full_box)

        ######################################################################내일 전체박스
        self.tomorrow_box=QVBoxLayout()

        self.tomorrow_inbox1=QHBoxLayout()
        self.tm1_tlb=QLabel("00:00\n-\n06:00",self.centralwidget)
        self.tm1_dlb=QLabel("내일 00:06 날씨그림",self.centralwidget)
        self.tm1_dlb.setPixmap(p_cloud_S)
        
        self.tm1_wbox=QVBoxLayout()
        self.tm1_telb=QLabel("25℃",self.centralwidget)
        # self.tm1_plb=QLabel("내일 00:06 강수확률",self.centralwidget)
        self.tm1_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.tm1_wlb=QLabel("10m/s",self.centralwidget)
        self.tm1_wbox.addWidget(self.tm1_telb)
        # self.tm1_wbox.addWidget(self.tm1_plb)
        self.tm1_wbox.addWidget(self.tm1_rlb)
        self.tm1_wbox.addWidget(self.tm1_wlb)
        self.tomorrow_inbox1.addWidget(self.tm1_tlb)
        self.tomorrow_inbox1.addWidget(self.tm1_dlb)
        self.tomorrow_inbox1.addLayout(self.tm1_wbox)

        self.tomorrow_inbox2=QHBoxLayout()
        self.tm2_tlb=QLabel("06:00\n-\n12:00",self.centralwidget)
        self.tm2_dlb=QLabel("내일 06:12 날씨그림",self.centralwidget)
        self.tm2_dlb.setPixmap(p_cloud_S)
        
        self.tm2_wbox=QVBoxLayout()
        self.tm2_telb=QLabel("25℃",self.centralwidget)
        # self.tm2_plb=QLabel("내일 06:12 강수확률",self.centralwidget)
        self.tm2_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.tm2_wlb=QLabel("10m/s",self.centralwidget)
        self.tm2_wbox.addWidget(self.tm2_telb)
        # self.tm2_wbox.addWidget(self.tm2_plb)
        self.tm2_wbox.addWidget(self.tm2_rlb)
        self.tm2_wbox.addWidget(self.tm2_wlb)
        self.tomorrow_inbox2.addWidget(self.tm2_tlb)
        self.tomorrow_inbox2.addWidget(self.tm2_dlb)
        self.tomorrow_inbox2.addLayout(self.tm2_wbox)

        self.tomorrow_inbox3=QHBoxLayout()
        self.tm3_tlb=QLabel("12:00\n-\n18:00",self.centralwidget)
        self.tm3_dlb=QLabel("내일 12:18 날씨그림",self.centralwidget)
        self.tm3_dlb.setPixmap(p_cloud_S)
        
        self.tm3_wbox=QVBoxLayout()
        self.tm3_telb=QLabel("25℃",self.centralwidget)
        # self.tm3_plb=QLabel("내일 12:18 강수확률",self.centralwidget)
        self.tm3_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.tm3_wlb=QLabel("10m/s",self.centralwidget)
        self.tm3_wbox.addWidget(self.tm3_telb)
        # self.tm3_wbox.addWidget(self.tm3_plb)
        self.tm3_wbox.addWidget(self.tm3_rlb)
        self.tm3_wbox.addWidget(self.tm3_wlb)
        self.tomorrow_inbox3.addWidget(self.tm3_tlb)
        self.tomorrow_inbox3.addWidget(self.tm3_dlb)
        self.tomorrow_inbox3.addLayout(self.tm3_wbox)

        self.tomorrow_inbox4=QHBoxLayout()
        self.tm4_tlb=QLabel("18:00\n-\n24:00",self.centralwidget)
        self.tm4_dlb=QLabel("내일 18:24 날씨그림",self.centralwidget)
        self.tm4_dlb.setPixmap(p_cloud_S)
        
        self.tm4_wbox=QVBoxLayout()
        self.tm4_telb=QLabel("25℃",self.centralwidget)
        # self.tm4_plb=QLabel("내일 18:24 강수확률",self.centralwidget)
        self.tm4_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.tm4_wlb=QLabel("10m/s",self.centralwidget)
        self.tm4_wbox.addWidget(self.tm4_telb)
        # self.tm4_wbox.addWidget(self.tm4_plb)
        self.tm4_wbox.addWidget(self.tm4_rlb)
        self.tm4_wbox.addWidget(self.tm4_wlb)
        self.tomorrow_inbox4.addWidget(self.tm4_tlb)
        self.tomorrow_inbox4.addWidget(self.tm4_dlb)
        self.tomorrow_inbox4.addLayout(self.tm4_wbox)
        
        self.todate_lb=QLabel("내일",self.centralwidget)
        self.todate_lb.setFixedSize(238, 16)
        self.tomorrow_box.addWidget(self.todate_lb) 
        self.tomorrow_box.addLayout(self.tomorrow_inbox1)
        self.tomorrow_box.addLayout(self.tomorrow_inbox2)
        self.tomorrow_box.addLayout(self.tomorrow_inbox3)
        self.tomorrow_box.addLayout(self.tomorrow_inbox4)

        ###################################################################### 모레 전체박스
        self.dat_box=QVBoxLayout() 

        self.dat_inbox1=QHBoxLayout()
        self.dat1_tlb=QLabel("00:00\n-\n06:00",self.centralwidget)
        self.dat1_dlb=QLabel("내일모레 00:06 날씨그림",self.centralwidget)
        self.dat1_dlb.setPixmap(p_cloud_S)
        
        self.dat1_wbox=QVBoxLayout()
        self.dat1_telb=QLabel("25℃",self.centralwidget)
        # self.dat1_plb=QLabel("내일모레 00:06 강수확률",self.centralwidget)
        self.dat1_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.dat1_wlb=QLabel("10m/s",self.centralwidget)
        self.dat1_wbox.addWidget(self.dat1_telb)
        # self.dat1_wbox.addWidget(self.dat1_plb)
        self.dat1_wbox.addWidget(self.dat1_rlb)
        self.dat1_wbox.addWidget(self.dat1_wlb)
        self.dat_inbox1.addWidget(self.dat1_tlb)
        self.dat_inbox1.addWidget(self.dat1_dlb)
        self.dat_inbox1.addLayout(self.dat1_wbox)

        self.dat_inbox2=QHBoxLayout()
        self.dat2_tlb=QLabel("06:00\n-\n12:00",self.centralwidget)
        self.dat2_dlb=QLabel("내일모레 06:12 날씨그림",self.centralwidget)
        self.dat2_dlb.setPixmap(p_cloud_S)
        
        self.dat2_wbox=QVBoxLayout()
        self.dat2_telb=QLabel("25℃",self.centralwidget)
        # self.dat2_plb=QLabel("내일모레 06:12 강수확률",self.centralwidget)
        self.dat2_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.dat2_wlb=QLabel("10m/s",self.centralwidget)
        self.dat2_wbox.addWidget(self.dat2_telb)
        # self.dat2_wbox.addWidget(self.dat2_plb)
        self.dat2_wbox.addWidget(self.dat2_rlb)
        self.dat2_wbox.addWidget(self.dat2_wlb)
        self.dat_inbox2.addWidget(self.dat2_tlb)
        self.dat_inbox2.addWidget(self.dat2_dlb)
        self.dat_inbox2.addLayout(self.dat2_wbox)

        self.dat_inbox3=QHBoxLayout()
        self.dat3_tlb=QLabel("12:00\n-\n18:00",self.centralwidget)
        self.dat3_dlb=QLabel("내일모레 12:18 날씨그림",self.centralwidget)
        self.dat3_dlb.setPixmap(p_cloud_S)
        
        self.dat3_wbox=QVBoxLayout()
        self.dat3_telb=QLabel("25℃",self.centralwidget)
        # self.dat3_plb=QLabel("내일모레 12:18 강수확률",self.centralwidget)
        self.dat3_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.dat3_wlb=QLabel("10m/s",self.centralwidget)
        self.dat3_wbox.addWidget(self.dat3_telb)
        # self.dat3_wbox.addWidget(self.dat3_plb)
        self.dat3_wbox.addWidget(self.dat3_rlb)
        self.dat3_wbox.addWidget(self.dat3_wlb)
        self.dat_inbox3.addWidget(self.dat3_tlb)
        self.dat_inbox3.addWidget(self.dat3_dlb)
        self.dat_inbox3.addLayout(self.dat3_wbox)

        self.dat_inbox4=QHBoxLayout()
        self.dat4_tlb=QLabel("18:00\n-\n24:00",self.centralwidget)
        self.dat4_dlb=QLabel("내일모레 18:24 날씨그림",self.centralwidget)
        self.dat4_dlb.setPixmap(p_cloud_S)
        
        self.dat4_wbox=QVBoxLayout()
        self.dat4_telb=QLabel("25℃",self.centralwidget)  
        # self.dat4_plb=QLabel("내일모레 18:24 강수확률",self.centralwidget)
        self.dat4_rlb=QLabel("100mm(20%)",self.centralwidget)
        self.dat4_wlb=QLabel("10m/s",self.centralwidget)
        self.dat4_wbox.addWidget(self.dat4_telb)
        # self.dat4_wbox.addWidget(self.dat4_plb)
        self.dat4_wbox.addWidget(self.dat4_rlb)
        self.dat4_wbox.addWidget(self.dat4_wlb)
        self.dat_inbox4.addWidget(self.dat4_tlb)
        self.dat_inbox4.addWidget(self.dat4_dlb)
        self.dat_inbox4.addLayout(self.dat4_wbox)
        
        self.datdate_lb=QLabel("모레",self.centralwidget)
        self.datdate_lb.setFixedSize(238, 16)
        self.dat_box.addWidget(self.datdate_lb)
        self.dat_box.addLayout(self.dat_inbox1)
        self.dat_box.addLayout(self.dat_inbox2)
        self.dat_box.addLayout(self.dat_inbox3)
        self.dat_box.addLayout(self.dat_inbox4)
        
        self.tn_box_frame = QFrame()
        self.tn_box_frame.setObjectName("tn_frame")
        self.tn_box_frame.setLayout(self.today_box)
        self.tn_box_frame.setStyleSheet("#tn_frame{border:1px solid #FF3232; background-color: #FFDCDC; border-radius: 5px;}")

        # self.tn_box.addLayout(self.today_box)
        self.tn_box.addWidget(self.tn_box_frame)
        
        self.to_box_frame = QFrame()
        self.to_box_frame.setObjectName("tn_frame")
        self.to_box_frame.setLayout(self.tomorrow_box)
        self.to_box_frame.setStyleSheet("#tn_frame{border:1px solid #FF3232; background-color: #FDE6BE; border-radius: 5px;}")
        
        self.tn_box.addWidget(self.to_box_frame)
        
        self.dat_box_frame = QFrame()
        self.dat_box_frame.setObjectName("tn_frame")
        self.dat_box_frame.setLayout(self.dat_box)
        self.dat_box_frame.setStyleSheet("#tn_frame{border:1px solid #FF3232; background-color: #FAFAD2; border-radius: 5px;}")
        
        self.tn_box.addWidget(self.dat_box_frame)

        self.wh_in_box.addLayout(self.tn_box)
        
        ###################################################################### 주간 날씨 박스
        self.week_box = QVBoxLayout()
        
        self.korea_box=QHBoxLayout()
        self.korea_lb=QLabel("기\n상\n청")

        # 기상청 주간 날씨
        self.kday1_box=QVBoxLayout()
        self.kday1_lb=QLabel("day1",self.centralwidget)
        self.kday1_dlb=QLabel("day1 날씨그림",self.centralwidget)
        self.kday1_tlb=QLabel("day1 온도",self.centralwidget)
        self.kday1_plb=QLabel("day1 강수확률",self.centralwidget)
        self.kday1_box.addWidget(self.kday1_lb)
        self.kday1_box.addWidget(self.kday1_dlb)
        self.kday1_box.addWidget(self.kday1_tlb)
        self.kday1_box.addWidget(self.kday1_plb)

        self.kday2_box=QVBoxLayout()
        self.kday2_lb=QLabel("day2",self.centralwidget)
        self.kday2_dlb=QLabel("day2 날씨그림",self.centralwidget)
        self.kday2_tlb=QLabel("day2 온도",self.centralwidget)
        self.kday2_plb=QLabel("day2 강수확률",self.centralwidget)
        self.kday2_box.addWidget(self.kday2_lb)
        self.kday2_box.addWidget(self.kday2_dlb)
        self.kday2_box.addWidget(self.kday2_tlb)
        self.kday2_box.addWidget(self.kday2_plb)

        self.kday3_box=QVBoxLayout()
        self.kday3_lb=QLabel("day3",self.centralwidget)
        self.kday3_dlb=QLabel("day3 날씨그림",self.centralwidget)
        self.kday3_tlb=QLabel("day3 온도",self.centralwidget)
        self.kday3_plb=QLabel("day3 강수확률",self.centralwidget)
        self.kday3_box.addWidget(self.kday3_lb)
        self.kday3_box.addWidget(self.kday3_dlb)
        self.kday3_box.addWidget(self.kday3_tlb)
        self.kday3_box.addWidget(self.kday3_plb)

        self.kday4_box=QVBoxLayout()
        self.kday4_lb=QLabel("day4",self.centralwidget)
        self.kday4_dlb=QLabel("day4 날씨그림",self.centralwidget)
        self.kday4_tlb=QLabel("day4 온도",self.centralwidget)
        self.kday4_plb=QLabel("day4 강수확률",self.centralwidget)
        self.kday4_box.addWidget(self.kday4_lb)
        self.kday4_box.addWidget(self.kday4_dlb)
        self.kday4_box.addWidget(self.kday4_tlb)
        self.kday4_box.addWidget(self.kday4_plb)

        self.kday5_box=QVBoxLayout()
        self.kday5_lb=QLabel("day5",self.centralwidget)
        self.kday5_dlb=QLabel("day5 날씨그림",self.centralwidget)
        self.kday5_tlb=QLabel("day5 온도",self.centralwidget)
        self.kday5_plb=QLabel("day5 강수확률",self.centralwidget)
        self.kday5_box.addWidget(self.kday5_lb)
        self.kday5_box.addWidget(self.kday5_dlb)
        self.kday5_box.addWidget(self.kday5_tlb)
        self.kday5_box.addWidget(self.kday5_plb)

        self.korea_box.addWidget(self.korea_lb)
        self.korea_box.addLayout(self.kday1_box)
        self.korea_box.addLayout(self.kday2_box)
        self.korea_box.addLayout(self.kday3_box)
        self.korea_box.addLayout(self.kday4_box)
        self.korea_box.addLayout(self.kday5_box)

        self.norway_box=QHBoxLayout()
        self.norway_lb=QLabel("노\n르\n웨\n이")

        # 노르웨이 주간 날씨
        self.nday1_box=QVBoxLayout()
        self.nday1_lb=QLabel("day1",self.centralwidget)
        self.nday1_dlb=QLabel("day1 날씨그림",self.centralwidget)
        self.nday1_tlb=QLabel("day1 온도",self.centralwidget)
        self.nday1_rlb=QLabel("day1 강수량",self.centralwidget)
        self.nday1_wlb=QLabel("day1 풍속",self.centralwidget)
        self.nday1_box.addWidget(self.nday1_lb)
        self.nday1_box.addWidget(self.nday1_dlb)
        self.nday1_box.addWidget(self.nday1_tlb)
        self.nday1_box.addWidget(self.nday1_rlb)
        self.nday1_box.addWidget(self.nday1_wlb)

        self.nday2_box=QVBoxLayout()
        self.nday2_lb=QLabel("day2",self.centralwidget)
        self.nday2_dlb=QLabel("day2 날씨그림",self.centralwidget)
        self.nday2_tlb=QLabel("day2 온도",self.centralwidget)
        self.nday2_rlb=QLabel("day2 강수량",self.centralwidget)
        self.nday2_wlb=QLabel("day2 풍속",self.centralwidget)
        self.nday2_box.addWidget(self.nday2_lb)
        self.nday2_box.addWidget(self.nday2_dlb)
        self.nday2_box.addWidget(self.nday2_tlb)
        self.nday2_box.addWidget(self.nday2_rlb)
        self.nday2_box.addWidget(self.nday2_wlb)

        self.nday3_box=QVBoxLayout()
        self.nday3_lb=QLabel("day3",self.centralwidget)
        self.nday3_dlb=QLabel("day3 날씨그림",self.centralwidget)
        self.nday3_tlb=QLabel("day3 온도",self.centralwidget)
        self.nday3_rlb=QLabel("day3 강수량",self.centralwidget)
        self.nday3_wlb=QLabel("day3 풍속",self.centralwidget)
        self.nday3_box.addWidget(self.nday3_lb)
        self.nday3_box.addWidget(self.nday3_dlb)
        self.nday3_box.addWidget(self.nday3_tlb)
        self.nday3_box.addWidget(self.nday3_rlb)
        self.nday3_box.addWidget(self.nday3_wlb)

        self.nday4_box=QVBoxLayout()
        self.nday4_lb=QLabel("day4",self.centralwidget)
        self.nday4_dlb=QLabel("day4 날씨그림",self.centralwidget)
        self.nday4_tlb=QLabel("day4 온도",self.centralwidget)
        self.nday4_rlb=QLabel("day4 강수량",self.centralwidget)
        self.nday4_wlb=QLabel("day4 풍속",self.centralwidget)
        self.nday4_box.addWidget(self.nday4_lb)
        self.nday4_box.addWidget(self.nday4_dlb)
        self.nday4_box.addWidget(self.nday4_tlb)
        self.nday4_box.addWidget(self.nday4_rlb)
        self.nday4_box.addWidget(self.nday4_wlb)

        self.nday5_box=QVBoxLayout()
        self.nday5_lb=QLabel("day5",self.centralwidget)
        self.nday5_dlb=QLabel("day5 날씨그림",self.centralwidget)
        self.nday5_tlb=QLabel("day5 온도",self.centralwidget)
        self.nday5_rlb=QLabel("day5 강수량",self.centralwidget)
        self.nday5_wlb=QLabel("day5 풍속",self.centralwidget)
        self.nday5_box.addWidget(self.nday5_lb)
        self.nday5_box.addWidget(self.nday5_dlb)
        self.nday5_box.addWidget(self.nday5_tlb)
        self.nday5_box.addWidget(self.nday5_rlb)
        self.nday5_box.addWidget(self.nday5_wlb)


        self.norway_box.addWidget(self.norway_lb)
        self.norway_box.addLayout(self.nday1_box)
        self.norway_box.addLayout(self.nday2_box)
        self.norway_box.addLayout(self.nday3_box)
        self.norway_box.addLayout(self.nday4_box)
        self.norway_box.addLayout(self.nday5_box)

        self.week_box.addLayout(self.korea_box)
        self.week_box.addLayout(self.norway_box)        
        
        #####
        self.wh_in_box.addLayout(self.week_box)
        
        self.wh_scrollArea.setLayout(self.wh_in_box)
        # wh_box.addStretch(1)
        self.wh_box.addWidget(self.wh_scrollArea)

        self.vbox.addLayout(self.wh_box)
        
    def rw_btn_setting(self, HomeWindow):
        self.temp_tnwh_no = 471
        res = excute("SELECT * FROM SM_RPU_TB WHERE RPU_TNWH_NO = :temp_tnwh_no AND RPU_USER_NO = :user_no", [self.temp_tnwh_no, HomeWindow.user_info["user_no"]])
        if len(res) > 0: self.hide_rw()
    
    def rgt_click(self, type, HomeWindow):
        self.temp_tnwh_no = 471
        rpu_res = 1
        if type == "W": rpu_res = 2
        
        res = excute("SELECT * FROM SM_RPU_TB WHERE RPU_TNWH_NO = :temp_tnwh_no AND RPU_USER_NO = :user_no", [self.temp_tnwh_no, HomeWindow.user_info["user_no"]])
        if len(res) < 1:
            res = excute("INSERT INTO SM_RPU_TB(RPU_NO, RPU_TNWH_NO, RPU_USER_NO, RPU_RES) VALUES(SM_RPU_SEQ.NEXTVAL, :temp_tnwh_no, :user_no, :rpu_res)",
                   [self.temp_tnwh_no, HomeWindow.user_info["user_no"], rpu_res])
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
        
        click_pixmap = QPixmap("./project/img/btn_click.png")
        click_pixmap = click_pixmap.scaled(30, 30)
        
        self.music_click_img = QLabel("MUSIC_CLICK", self.centralwidget)
        self.music_click_img.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.music_click_img.setPixmap(click_pixmap)
        
        self.food_click_img = QLabel("FOOD_CLICK", self.centralwidget)
        self.food_click_img.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.food_click_img.setPixmap(click_pixmap)
        
        self.activity_click_img = QLabel("ACTIVITY_CLICK", self.centralwidget)
        self.activity_click_img.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.activity_click_img.setPixmap(click_pixmap)
        
        self.scrollArea_box = QScrollArea()
        self.scrollArea_box.setWidgetResizable(True)
        self.grid1 = QGridLayout()
        
        self.temp_lab = QLabel("", self.centralwidget)
        self.temp_lab.resize(30, 30)
        
        self.grid1.addWidget(self.rcd_title, 0, 0, 1, 1)
        self.grid1.addWidget(self.music_click_img, 1, 0, 2, 1)
        self.grid1.addWidget(self.music, 2, 0, 1, 1)
        self.grid1.addWidget(self.food_click_img, 3, 0, 2, 1)
        self.grid1.addWidget(self.food, 4, 0, 1, 1)
        self.grid1.addWidget(self.activity_click_img, 5, 0, 2, 1)
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
        self.toggle("Y")
        self.music_click_img.show()
        self.food_click_img.hide()
        self.activity_click_img.hide()
        self.music.setStyleSheet("width: 80px; height: 30px; color: #FFFFFF; border: 5px red solid; border-radius: 3px; background-color: #FF8C0A; font-size: 12pt;")
        self.webview1.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
        self.webview2.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
        self.webview3.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
        self.webview4.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
        self.webview5.setUrl(QUrl("https://i.ytimg.com/vi/rRi_1D97FBs/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCr5LLXMdAsgzIhNBba7pS7-eUoFw")) 
      
    def food_play(self):
        self.toggle("Y")
        self.music_click_img.hide()
        self.food_click_img.show()
        self.activity_click_img.hide()
        self.webview1.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0"))
        self.webview2.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0"))
        self.webview3.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0"))
        self.webview4.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0"))
        self.webview5.setUrl(QUrl("https://www.youtube.com/embed/CT-Qm6nbOko?autoplay=0"))
    
    def activity_play(self):
        self.music_click_img.hide()
        self.food_click_img.hide()
        self.activity_click_img.show()
        self.webview1.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468"))
        self.webview2.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468")) 
        self.webview3.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468")) 
        self.webview4.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468")) 
        self.webview5.setUrl(QUrl("https://blog.naver.com/min-meme8569?Redirect=Log&logNo=222049704468"))
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
    
    def recomm_func(self):
        ##########################영돈 steart###########################
        print("추천")
        ############################도현 end############################
            
            
        
        