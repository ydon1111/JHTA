import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from common.DBconnect import *
from datetime import date,datetime,timedelta 
from common.spinner import *
import time

t=date.today()
today=t.isoformat()
tom=t+timedelta(days=+1)
tomorrow=tom.isoformat() 
d=tom+timedelta(days=+1)
dat=d.isoformat()

now_hour = time.localtime().tm_hour

d1=(t+timedelta(days=+3)).isoformat()
d2=(t+timedelta(days=+4)).isoformat()
d3=(t+timedelta(days=+5)).isoformat()
d4=(t+timedelta(days=+6)).isoformat()
d5=(t+timedelta(days=+7)).isoformat()

dtitle1=str((t+timedelta(days=+3)).day)
dtitle2=str((t+timedelta(days=+4)).day)
dtitle3=str((t+timedelta(days=+5)).day)
dtitle4=str((t+timedelta(days=+6)).day)
dtitle5=str((t+timedelta(days=+7)).day)

class main():

    def setupUI(self, HomeWindow, chk_loc):
        HomeWindow.setWindowTitle("날씨")
        
        self.centralwidget = QWidget(HomeWindow)
        HomeWindow.setCentralWidget(self.centralwidget)
        
        self.chk_loc = chk_loc
        
        self.initUI(HomeWindow)
        
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
        self.set_rcd_url()
        self.music_play()
        
        # spinner
        self.overlay = Overlay(self.centralwidget)
        self.overlay.show()
        self.overlay.resize(HomeWindow.width(), HomeWindow.height())
        
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
        if self.chk_loc == 1: self.m_ro_seoul.setChecked(True)
        self.loc_box.addWidget(self.m_ro_seoul)
        self.m_ro_seoul.clicked.connect(lambda : HomeWindow.start_main(1))

        self.m_ro_gangneung = QRadioButton('강릉', self.centralwidget)
        if self.chk_loc == 2: self.m_ro_gangneung.setChecked(True)
        self.loc_box.addWidget(self.m_ro_gangneung)
        self.m_ro_gangneung.clicked.connect(lambda : HomeWindow.start_main(2))

        self.m_ro_deajeon = QRadioButton('대전', self.centralwidget)
        if self.chk_loc == 3: self.m_ro_deajeon.setChecked(True)
        self.loc_box.addWidget(self.m_ro_deajeon)
        self.m_ro_deajeon.clicked.connect(lambda : HomeWindow.start_main(3))

        self.m_ro_gwangju = QRadioButton('광주', self.centralwidget)
        if self.chk_loc == 4: self.m_ro_gwangju.setChecked(True)
        self.loc_box.addWidget(self.m_ro_gwangju)
        self.m_ro_gwangju.clicked.connect(lambda : HomeWindow.start_main(4))

        self.m_ro_ulsan = QRadioButton('울산', self.centralwidget)
        if self.chk_loc == 5: self.m_ro_ulsan.setChecked(True)
        self.loc_box.addWidget(self.m_ro_ulsan)
        self.m_ro_ulsan.clicked.connect(lambda : HomeWindow.start_main(5))

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
        
        self.rlb_lb = QLabel("", self.centralwidget)
        
        self.rw_btn_box.addWidget(self.wrg_btn)
        self.rw_btn_box.addWidget(self.rlb_lb)
        self.tbar_box.addLayout(self.rw_btn_box)
        
        self.tbar_box.addStretch(1)
        
        # 로그아웃 버튼
        self.logout_btn = QPushButton("로그아웃", self.centralwidget)
        self.logout_btn.setFixedSize(100, 30)
        self.logout_btn.clicked.connect(lambda: self.logout(HomeWindow))
        self.tbar_box.addWidget(self.logout_btn)

        self.vbox.addLayout(self.tbar_box)
        
    def get_img(self, type, hour, width, height): # 50, 35
        img_url = "./project/img/weather/w1.png"

        if type in ("맑음", 'Clear sky'):
            img_url = "./project/img/weather/w1.png"
            if hour >= 18: img_url = "./project/img/weather/w2.png"
        elif type in ("구름조금", "구름 조금", 'Fair'):
            img_url = "./project/img/weather/w3.png"
            if hour >= 18: img_url = img_url = "./project/img/weather/w4.png"
        elif type in ("구름많음", "구름 많음", 'Partly cloudy'):
            img_url = "./project/img/weather/w5.png"
            if hour >= 18: img_url = img_url = "./project/img/weather/w6.png"
        elif type in ("흐림", "Cludy", "Fog", "Cloudy"):
            img_url = "./project/img/weather/w7.png"
        elif type in ("소나기", 'Heavy rain showers', 'Light rain showers',  'Rain showers'):
            img_url = "./project/img/weather/w8.png"
        elif type in ("비", "구름많고 비", "흐리고 비", "빗방울", 'Light rain', 'Heavy rain', 'Rain'):
            img_url = "./project/img/weather/w9.png"
        elif type in ("가끔 비", "한때 비", "가끔 눈", "한때 눈", "가끔 비 또는 눈", "한때 비 또는 눈", "가끔 눈 또는 비", "한때 눈 또는 비"):
            img_url = "./project/img/weather/w10.png"
        elif type in ("천둥번개", 'Light rain and thunder'):
            img_url = "./project/img/weather/w18.png"

        return QPixmap(img_url).scaled(width, height)
        
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

        now=excute("select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND, TNWH_NO from SM_TNWH_TB where tnwh_no = (select max(tnwh_no) from sm_tnwh_tb where TNWH_LOC = :loc and tnwh_type = :num)", [self.chk_loc,3])
        self.now_tnwh_no=now[0][4] #지금 날씨 정보의 고유번호

        ######################################################################오늘=>현재
        self.tdate_lb=QLabel("오늘",self.centralwidget)
        self.tdraw_lb=QLabel(str(now[0][0]),self.centralwidget)
        self.tdraw_lb.setPixmap(self.get_img(str(now[0][0]), now_hour, 50, 35))
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
        self.full_box=QHBoxLayout() #오늘=>전체시간대 날씨박스

        # 시간
        self.tfull_box1=QVBoxLayout()
        self.tfull1_lb=QLabel("00:00\n-\n06:00",self.centralwidget)
        self.line2 = QLabel("--------------------------------------------", self.centralwidget)
        self.tfull2_lb=QLabel("06:00\n-\n12:00",self.centralwidget)
        self.line3 = QLabel("--------------------------------------------", self.centralwidget)
        self.tfull3_lb=QLabel("12:00\n-\n18:00",self.centralwidget)
        self.line4 = QLabel("--------------------------------------------", self.centralwidget)
        self.tfull4_lb=QLabel("18:00\n-\n24:00",self.centralwidget)
        
        self.tfull_box1.addWidget(self.tfull1_lb)
        self.tfull_box1.addWidget(self.line2)
        self.tfull_box1.addWidget(self.tfull2_lb)
        self.tfull_box1.addWidget(self.line3)
        self.tfull_box1.addWidget(self.tfull3_lb)
        self.tfull_box1.addWidget(self.line4)
        self.tfull_box1.addWidget(self.tfull4_lb)

        self.tfull_box2=QVBoxLayout()

        self.tfull_0box=QHBoxLayout()
        self.tfull_6box=QHBoxLayout()
        self.tfull_12box=QHBoxLayout()
        self.tfull_18box=QHBoxLayout()

        self.tfull_0box_frame=QFrame()
        self.tfull_0box_frame.setObjectName("tfull_0box_frame")
        self.tfull_0box_frame.setLayout(self.tfull_0box)

        self.tfull_6box_frame=QFrame()
        self.tfull_6box_frame.setObjectName("tfull_6box_frame")
        self.tfull_6box_frame.setLayout(self.tfull_6box)

        self.tfull_12box_frame=QFrame()
        self.tfull_12box_frame.setObjectName("tfull_12box_frame")
        self.tfull_12box_frame.setLayout(self.tfull_12box)

        now_full=excute("select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC_PROB, TNWH_PREC, TNWH_WIND from SM_TNWH_TB where TNWH_DATE = :today and TNWH_LOC = :loc and TNWH_TYPE = :num", [today, self.chk_loc, 1])

        # 00:00 - 06:00
        self.tfull_0box1=QVBoxLayout()
        self.tfull_0d_lb=QLabel(now_full[0][0],self.centralwidget)
        self.tfull_0d_lb.setPixmap(self.get_img(str(now_full[0][0]), now_hour, 50, 35))
        self.tfull_0box1.addWidget(self.tfull_0d_lb)
        
        self.tfull_0box2=QVBoxLayout()
        self.tfull_0w_tlb=QLabel(now_full[0][1] + "℃",self.centralwidget)
        self.tfull_0w_rlb=QLabel(str(now_full[0][3]) + "mm(" + str(now_full[0][2]) + "%)",self.centralwidget)
        self.tfull_0w_wlb=QLabel(str(now_full[0][4]) + "m/s",self.centralwidget)
        self.tfull_0box2.addWidget(self.tfull_0w_tlb)
        self.tfull_0box2.addWidget(self.tfull_0w_rlb)
        self.tfull_0box2.addWidget(self.tfull_0w_wlb)
        self.tfull_0box.addLayout(self.tfull_0box1)
        self.tfull_0box.addLayout(self.tfull_0box2)

        # 06:00 - 12:00
        self.tfull_6box1=QVBoxLayout()
        self.tfull_6d_lb=QLabel(now_full[1][0],self.centralwidget)
        self.tfull_6d_lb.setPixmap(self.get_img(str(now_full[1][0]), now_hour, 50, 35))
        self.tfull_6box1.addWidget(self.tfull_6d_lb)

        self.tfull_6box2=QVBoxLayout()
        self.tfull_6w_tlb=QLabel(now_full[1][1] + "℃",self.centralwidget)
        self.tfull_6w_rlb=QLabel(str(now_full[1][3]) + "mm(" + str(now_full[1][2]) + "%)",self.centralwidget)
        self.tfull_6w_wlb=QLabel(str(now_full[1][4]) + "m/s",self.centralwidget)
        self.tfull_6box2.addWidget(self.tfull_6w_tlb)
        self.tfull_6box2.addWidget(self.tfull_6w_rlb)
        self.tfull_6box2.addWidget(self.tfull_6w_wlb)
        self.tfull_6box.addLayout(self.tfull_6box1)
        self.tfull_6box.addLayout(self.tfull_6box2)

        # 12:00 - 18:00
        self.tfull_12box1=QVBoxLayout()
        self.tfull_12d_lb=QLabel(now_full[2][0],self.centralwidget)
        self.tfull_12d_lb.setPixmap(self.get_img(str(now_full[2][0]), now_hour, 50, 35))
        self.tfull_12box1.addWidget(self.tfull_12d_lb)

        self.tfull_12box2=QVBoxLayout()
        self.tfull_12w_tlb=QLabel(now_full[2][1] + "℃",self.centralwidget)
        self.tfull_12w_rlb=QLabel(str(now_full[2][3]) + "mm(" + str(now_full[2][2]) + "%)",self.centralwidget)
        self.tfull_12w_wlb=QLabel(str(now_full[2][4]) + "m/s",self.centralwidget)
        self.tfull_12box2.addWidget(self.tfull_12w_tlb)
        self.tfull_12box2.addWidget(self.tfull_12w_rlb)
        self.tfull_12box2.addWidget(self.tfull_12w_wlb)

        self.tfull_12box.addLayout(self.tfull_12box1)
        self.tfull_12box.addLayout(self.tfull_12box2)

        # 18:00 - 24:00
        self.tfull_18box1=QVBoxLayout()
        self.tfull_18d_lb=QLabel(now_full[3][0],self.centralwidget)
        self.tfull_18d_lb.setPixmap(self.get_img(str(now_full[3][0]), now_hour, 50, 35))
        self.tfull_18box1.addWidget(self.tfull_18d_lb)

        self.tfull_18box2=QVBoxLayout()
        self.tfull_18w_tlb=QLabel(now_full[3][1] + "℃",self.centralwidget)
        self.tfull_18w_rlb=QLabel(str(now_full[3][3]) + "mm(" + str(now_full[3][2]) + "%)",self.centralwidget)
        self.tfull_18w_wlb=QLabel(str(now_full[3][4]) + "m/s",self.centralwidget)
        self.tfull_18box2.addWidget(self.tfull_18w_tlb)
        self.tfull_18box2.addWidget(self.tfull_18w_rlb)
        self.tfull_18box2.addWidget(self.tfull_18w_wlb)

        self.tfull_18box.addLayout(self.tfull_18box1)
        self.tfull_18box.addLayout(self.tfull_18box2)

        self.tfull_box2.addWidget(self.tfull_0box_frame)
        self.tfull_box2.addWidget(self.tfull_6box_frame)
        self.tfull_box2.addWidget(self.tfull_12box_frame)
        # self.tfull_box2.addWidget(self.tfull_18box_frame)
        self.tfull_box2.addLayout(self.tfull_18box)

        self.full_box.addLayout(self.tfull_box1)
        self.full_box.addLayout(self.tfull_box2)

        self.today_box.addLayout(self.now_box)
        self.today_box.addLayout(self.full_box)

        ######################################################################내일 전체박스
        self.tomorrow_box=QVBoxLayout()

        self.tomorrow_inbox1=QHBoxLayout()
        tom1k=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC_PROB, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[tomorrow,'00:00-06:00',self.chk_loc,1])
        tom1n=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[tomorrow,'00:00-06:00',self.chk_loc,2])

        self.tm1_tlb=QLabel("00:00\n-\n06:00",self.centralwidget)

        self.tm1_wbox1=QVBoxLayout() #내일 00:06 기상청
        self.tm1_klb=QLabel("기상청",self.centralwidget)
        self.tm1_dlb=QLabel(tom1k[0][0],self.centralwidget)
        self.tm1_dlb.setPixmap(self.get_img(str(tom1k[0][0]), now_hour, 30, 20))
        self.tm1_telb=QLabel(tom1k[0][1]+"℃   "+str(tom1k[0][4])+"m/s",self.centralwidget)
        self.tm1_rlb=QLabel(tom1k[0][3]+"mm"+"("+str(tom1k[0][2])+"%"+")",self.centralwidget)
        # self.tm1_wlb=QLabel(str(tom1k[0][4])+"m/s",self.centralwidget)
        self.tm1_wbox1.addWidget(self.tm1_klb)
        self.tm1_wbox1.addWidget(self.tm1_dlb)
        self.tm1_wbox1.addWidget(self.tm1_telb)
        self.tm1_wbox1.addWidget(self.tm1_rlb)
        # self.tm1_wbox1.addWidget(self.tm1_wlb)


        self.tm1_wbox2=QVBoxLayout() #내일 00:06 노르웨이
        self.tm1_nlb=QLabel("노르웨이",self.centralwidget)
        self.tm1_ndlb=QLabel(tom1n[0][0],self.centralwidget)
        self.tm1_ndlb.setPixmap(self.get_img(str(tom1n[0][0]), now_hour, 30, 20))
        self.tm1_ntelb=QLabel(tom1n[0][1]+"℃   "+str(tom1n[0][3])+"m/s",self.centralwidget)
        self.tm1_nrlb=QLabel(tom1n[0][2]+"mm",self.centralwidget)
        # self.tm1_nwlb=QLabel(str(tom1n[0][3])+"m/s",self.centralwidget)
        self.tm1_wbox2.addWidget(self.tm1_nlb)
        self.tm1_wbox2.addWidget(self.tm1_ndlb)
        self.tm1_wbox2.addWidget(self.tm1_ntelb)
        self.tm1_wbox2.addWidget(self.tm1_nrlb)
        # self.tm1_wbox2.addWidget(self.tm1_nwlb)

        self.tomorrow_inbox1.addWidget(self.tm1_tlb)
        self.tomorrow_inbox1.addLayout(self.tm1_wbox1)
        self.tomorrow_inbox1.addLayout(self.tm1_wbox2)

        ##############

        self.tomorrow_inbox2=QHBoxLayout()

        tom2k=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC_PROB, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[tomorrow,'06:00-12:00',self.chk_loc,1])
        tom2n=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[tomorrow,'06:00-12:00',self.chk_loc,2])

        self.tm2_tlb=QLabel("06:00\n-\n12:00",self.centralwidget)

        self.tm2_wbox1=QVBoxLayout()
        self.tm2_dlb=QLabel(tom2k[0][0],self.centralwidget)
        self.tm2_dlb.setPixmap(self.get_img(str(tom2k[0][0]), now_hour, 30, 20))
        self.tm2_telb=QLabel(tom2k[0][1]+"℃   "+str(tom2k[0][4])+"m/s",self.centralwidget)
        self.tm2_rlb=QLabel(tom2k[0][3]+"mm"+"("+str(tom2k[0][2])+"%"+")",self.centralwidget)
        # self.tm2_wlb=QLabel(str(tom2k[0][4])+"m/s",self.centralwidget)
        self.tm2_wbox1.addWidget(self.tm2_dlb)
        self.tm2_wbox1.addWidget(self.tm2_telb)
        self.tm2_wbox1.addWidget(self.tm2_rlb)
        # self.tm2_wbox1.addWidget(self.tm2_wlb)


        self.tm2_wbox2=QVBoxLayout()
        self.tm2_ndlb=QLabel(tom2n[0][0],self.centralwidget)
        self.tm2_ndlb.setPixmap(self.get_img(str(tom2n[0][0]), now_hour, 30, 20))
        self.tm2_ntelb=QLabel(tom2n[0][1]+"℃   "+str(tom2n[0][3])+"m/s",self.centralwidget)
        self.tm2_nrlb=QLabel(tom2n[0][2]+"mm",self.centralwidget)
        # self.tm2_nwlb=QLabel(str(tom2n[0][3])+"m/s",self.centralwidget)
        self.tm2_wbox2.addWidget(self.tm2_ndlb)
        self.tm2_wbox2.addWidget(self.tm2_ntelb)
        self.tm2_wbox2.addWidget(self.tm2_nrlb)
        # self.tm2_wbox2.addWidget(self.tm2_nwlb)

        self.tomorrow_inbox2.addWidget(self.tm2_tlb)
        self.tomorrow_inbox2.addLayout(self.tm2_wbox1)
        self.tomorrow_inbox2.addLayout(self.tm2_wbox2)

        ##############

        self.tomorrow_inbox3=QHBoxLayout()

        tom3k=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC_PROB, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[tomorrow,'12:00-18:00',self.chk_loc,1])
        tom3n=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[tomorrow,'12:00-18:00',self.chk_loc,2])

        self.tm3_tlb=QLabel("12:00\n-\n18:00",self.centralwidget)

        self.tm3_wbox1=QVBoxLayout()
        self.tm3_dlb=QLabel(tom3k[0][0],self.centralwidget)
        self.tm3_dlb.setPixmap(self.get_img(str(tom3k[0][0]), now_hour, 30, 20))
        self.tm3_telb=QLabel(tom3k[0][1]+"℃   "+str(tom3k[0][4])+"m/s",self.centralwidget)
        self.tm3_rlb=QLabel(tom3k[0][3]+"mm"+"("+str(tom3k[0][2])+"%"+")",self.centralwidget)
        # self.tm3_wlb=QLabel(str(tom3k[0][4])+"m/s",self.centralwidget)
        self.tm3_wbox1.addWidget(self.tm3_dlb)
        self.tm3_wbox1.addWidget(self.tm3_telb)
        self.tm3_wbox1.addWidget(self.tm3_rlb)
        # self.tm3_wbox1.addWidget(self.tm3_wlb)


        self.tm3_wbox2=QVBoxLayout()
        self.tm3_ndlb=QLabel(tom3n[0][0],self.centralwidget)
        self.tm3_ndlb.setPixmap(self.get_img(str(tom3n[0][0]), now_hour, 30, 20))
        self.tm3_ntelb=QLabel(tom3n[0][1]+"℃   "+str(tom3n[0][3])+"m/s",self.centralwidget)
        self.tm3_nrlb=QLabel(tom3n[0][2]+"mm",self.centralwidget)
        # self.tm3_nwlb=QLabel(str(tom3n[0][3])+"m/s",self.centralwidget)
        self.tm3_wbox2.addWidget(self.tm3_ndlb)
        self.tm3_wbox2.addWidget(self.tm3_ntelb)
        self.tm3_wbox2.addWidget(self.tm3_nrlb)
        # self.tm3_wbox2.addWidget(self.tm3_nwlb)

        self.tomorrow_inbox3.addWidget(self.tm3_tlb)
        self.tomorrow_inbox3.addLayout(self.tm3_wbox1)
        self.tomorrow_inbox3.addLayout(self.tm3_wbox2)

        ##############

        self.tomorrow_inbox4=QHBoxLayout()

        tom4k=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC_PROB, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[tomorrow,'18:00-24:00',self.chk_loc,1])
        tom4n=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[tomorrow,'18:00-00:00',self.chk_loc,2])

        self.tm4_tlb=QLabel("18:00\n-\n24:00",self.centralwidget)

        self.tm4_wbox1=QVBoxLayout()
        self.tm4_dlb=QLabel(tom4k[0][0],self.centralwidget)
        self.tm4_dlb.setPixmap(self.get_img(str(tom4k[0][0]), now_hour, 30, 20))
        self.tm4_telb=QLabel(tom4k[0][1]+"℃   "+str(tom4k[0][4])+"m/s",self.centralwidget)
        self.tm4_rlb=QLabel(tom4k[0][3]+"mm"+"("+str(tom4k[0][2])+"%"+")",self.centralwidget)
        # self.tm4_wlb=QLabel(str(tom4k[0][4])+"m/s",self.centralwidget)
        self.tm4_wbox1.addWidget(self.tm4_dlb)
        self.tm4_wbox1.addWidget(self.tm4_telb)
        self.tm4_wbox1.addWidget(self.tm4_rlb)
        # self.tm4_wbox1.addWidget(self.tm4_wlb)


        self.tm4_wbox2=QVBoxLayout()
        self.tm4_ndlb=QLabel(tom4n[0][0],self.centralwidget)
        self.tm4_ndlb.setPixmap(self.get_img(str(tom4n[0][0]), now_hour, 30, 20))
        self.tm4_ntelb=QLabel(tom4n[0][1]+"℃   "+str(tom4n[0][3])+"m/s",self.centralwidget)
        self.tm4_nrlb=QLabel(tom4n[0][2]+"mm",self.centralwidget)
        # self.tm4_nwlb=QLabel(str(tom4n[0][3])+"m/s",self.centralwidget)
        self.tm4_wbox2.addWidget(self.tm4_ndlb)
        self.tm4_wbox2.addWidget(self.tm4_ntelb)
        self.tm4_wbox2.addWidget(self.tm4_nrlb)
        # self.tm4_wbox2.addWidget(self.tm4_nwlb)

        self.tomorrow_inbox4.addWidget(self.tm4_tlb)
        self.tomorrow_inbox4.addLayout(self.tm4_wbox1)
        self.tomorrow_inbox4.addLayout(self.tm4_wbox2)

        ######
        self.tomorrow_inbox1_frame=QFrame()
        self.tomorrow_inbox1_frame.setObjectName("tomorrow_inbox1_fr")
        self.tomorrow_inbox1_frame.setLayout(self.tomorrow_inbox1)

        self.tomorrow_inbox2_frame=QFrame()
        self.tomorrow_inbox2_frame.setObjectName("tomorrow_inbox2_fr")
        self.tomorrow_inbox2_frame.setLayout(self.tomorrow_inbox2)

        self.tomorrow_inbox3_frame=QFrame()
        self.tomorrow_inbox3_frame.setObjectName("tomorrow_inbox3_fr")
        self.tomorrow_inbox3_frame.setLayout(self.tomorrow_inbox3)

        self.tomorrow_inbox4_frame=QFrame()
        self.tomorrow_inbox4_frame.setObjectName("tomorrow_inbox4_fr")
        self.tomorrow_inbox4_frame.setLayout(self.tomorrow_inbox4)

        ##############
        
        self.todate_lb=QLabel("내일",self.centralwidget)
        self.tomorrow_box.addWidget(self.todate_lb) 
        self.tomorrow_box.addWidget(self.tomorrow_inbox1_frame)
        self.tomorrow_box.addWidget(self.tomorrow_inbox2_frame)
        self.tomorrow_box.addWidget(self.tomorrow_inbox3_frame)
        self.tomorrow_box.addWidget(self.tomorrow_inbox4_frame)

        ###################################################################### 모레 전체박스
        self.dat_box=QVBoxLayout() 

        self.dat_inbox1=QHBoxLayout()
        dat1k=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC_PROB, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[dat,'00:00-06:00',self.chk_loc,1])
        dat1n=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[dat,'00:00-06:00',self.chk_loc,2])

        self.dat1_tlb=QLabel("00:00\n-\n06:00",self.centralwidget)

        self.dat1_wbox1=QVBoxLayout()
        self.dat1_klb=QLabel("기상청",self.centralwidget)
        self.dat1_dlb=QLabel(dat1k[0][0],self.centralwidget)
        self.dat1_dlb.setPixmap(self.get_img(str(dat1k[0][0]), now_hour, 30, 20))
        self.dat1_telb=QLabel(dat1k[0][1]+"℃   "+str(dat1k[0][4])+"m/s",self.centralwidget)
        self.dat1_rlb=QLabel(dat1k[0][3]+"mm"+"("+str(dat1k[0][2])+"%"+")",self.centralwidget)
        # self.dat1_wlb=QLabel(str(dat1k[0][4])+"m/s",self.centralwidget)
        self.dat1_wbox1.addWidget(self.dat1_klb)
        self.dat1_wbox1.addWidget(self.dat1_dlb)
        self.dat1_wbox1.addWidget(self.dat1_telb)
        self.dat1_wbox1.addWidget(self.dat1_rlb)
        # self.dat1_wbox1.addWidget(self.dat1_wlb)

        self.dat1_wbox2=QVBoxLayout()
        self.dat1_nlb=QLabel("노르웨이",self.centralwidget)
        self.dat1_ndlb=QLabel(dat1n[0][0],self.centralwidget)
        self.dat1_ndlb.setPixmap(self.get_img(str(dat1n[0][0]), now_hour, 30, 20))
        self.dat1_ntelb=QLabel(dat1n[0][1]+"℃   "+str(dat1n[0][3])+"m/s",self.centralwidget)
        self.dat1_nrlb=QLabel(dat1n[0][2]+"mm",self.centralwidget)
        # self.dat1_nwlb=QLabel(str(dat1n[0][3])+"m/s",self.centralwidget)
        self.dat1_wbox2.addWidget(self.dat1_nlb)
        self.dat1_wbox2.addWidget(self.dat1_ndlb)
        self.dat1_wbox2.addWidget(self.dat1_ntelb)
        self.dat1_wbox2.addWidget(self.dat1_nrlb)
        # self.dat1_wbox2.addWidget(self.dat1_nwlb)

        self.dat_inbox1.addWidget(self.dat1_tlb)
        self.dat_inbox1.addLayout(self.dat1_wbox1)
        self.dat_inbox1.addLayout(self.dat1_wbox2)

        ##############

        self.dat_inbox2=QHBoxLayout()
        dat2k=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC_PROB, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[dat,'06:00-12:00',self.chk_loc,1])
        dat2n=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[dat,'06:00-12:00',self.chk_loc,2])

        self.dat2_tlb=QLabel("06:00\n-\n12:00",self.centralwidget)

        self.dat2_wbox1=QVBoxLayout()
        self.dat2_dlb=QLabel(dat2k[0][0],self.centralwidget)
        self.dat2_dlb.setPixmap(self.get_img(str(dat2k[0][0]), now_hour, 30, 20))
        self.dat2_telb=QLabel(dat2k[0][1]+"℃   "+str(dat2k[0][4])+"m/s",self.centralwidget)
        self.dat2_rlb=QLabel(dat2k[0][3]+"mm"+"("+str(dat2k[0][2])+"%"+")",self.centralwidget)
        # self.dat2_wlb=QLabel(str(dat2k[0][4])+"m/s",self.centralwidget)
        self.dat2_wbox1.addWidget(self.dat2_dlb)
        self.dat2_wbox1.addWidget(self.dat2_telb)
        self.dat2_wbox1.addWidget(self.dat2_rlb)
        # self.dat2_wbox1.addWidget(self.dat2_wlb)


        self.dat2_wbox2=QVBoxLayout()
        self.dat2_ndlb=QLabel(dat2n[0][0],self.centralwidget)
        self.dat2_ndlb.setPixmap(self.get_img(str(dat2n[0][0]), now_hour, 30, 20))
        self.dat2_ntelb=QLabel(dat2n[0][1]+"℃   "+str(dat2n[0][3])+"m/s",self.centralwidget)
        self.dat2_nrlb=QLabel(dat2n[0][2]+"mm",self.centralwidget)
        # self.dat2_nwlb=QLabel(str(dat2n[0][3])+"m/s",self.centralwidget)
        self.dat2_wbox2.addWidget(self.dat2_ndlb)
        self.dat2_wbox2.addWidget(self.dat2_ntelb)
        self.dat2_wbox2.addWidget(self.dat2_nrlb)
        # self.dat2_wbox2.addWidget(self.dat2_nwlb)

        self.dat_inbox2.addWidget(self.dat2_tlb)
        self.dat_inbox2.addLayout(self.dat2_wbox1)
        self.dat_inbox2.addLayout(self.dat2_wbox2)

        ##############

        self.dat_inbox3=QHBoxLayout()
        dat3k=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC_PROB, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[dat,'12:00-18:00',self.chk_loc,1])
        dat3n=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[dat,'12:00-18:00',self.chk_loc,2])

        self.dat3_tlb=QLabel("12:00\n-\n18:00",self.centralwidget)

        self.dat3_wbox1=QVBoxLayout()
        self.dat3_dlb=QLabel(dat3k[0][0],self.centralwidget)
        self.dat3_dlb.setPixmap(self.get_img(str(dat3k[0][0]), now_hour, 30, 20))
        self.dat3_telb=QLabel(dat3k[0][1]+"℃   "+str(dat3k[0][4])+"m/s",self.centralwidget)
        self.dat3_rlb=QLabel(dat3k[0][3]+"mm"+"("+str(dat3k[0][2])+"%"+")",self.centralwidget)
        # self.dat3_wlb=QLabel(str(dat3k[0][4])+"m/s",self.centralwidget)
        self.dat3_wbox1.addWidget(self.dat3_dlb)
        self.dat3_wbox1.addWidget(self.dat3_telb)
        self.dat3_wbox1.addWidget(self.dat3_rlb)
        # self.dat3_wbox1.addWidget(self.dat3_wlb)

        self.dat3_wbox2=QVBoxLayout()
        self.dat3_ndlb=QLabel(dat3n[0][0],self.centralwidget)
        self.dat3_ndlb.setPixmap(self.get_img(str(dat3n[0][0]), now_hour, 30, 20))
        self.dat3_ntelb=QLabel(dat3n[0][1]+"℃   "+str(dat3n[0][3])+"m/s",self.centralwidget)
        self.dat3_nrlb=QLabel(dat3n[0][2]+"mm",self.centralwidget)
        # self.dat3_nwlb=QLabel(str(dat3n[0][3])+"m/s",self.centralwidget)
        self.dat3_wbox2.addWidget(self.dat3_ndlb)
        self.dat3_wbox2.addWidget(self.dat3_ntelb)
        self.dat3_wbox2.addWidget(self.dat3_nrlb)
        # self.dat3_wbox2.addWidget(self.dat3_nwlb)

        self.dat_inbox3.addWidget(self.dat3_tlb)
        self.dat_inbox3.addLayout(self.dat3_wbox1)
        self.dat_inbox3.addLayout(self.dat3_wbox2)

        ##############

        self.dat_inbox4=QHBoxLayout()
        dat4k=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC_PROB, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[dat,'18:00-24:00',self.chk_loc,1])
        dat4n=excute('select TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND from sm_tnwh_tb where TNWH_NO = (select max(TNWH_NO) from sm_tnwh_tb where TNWH_DATE=:tom and TNWH_TIME=:time and TNWH_LOC=:loc and TNWH_TYPE=:num)',[dat,'18:00-00:00',self.chk_loc,2])

        self.dat4_tlb=QLabel("18:00\n-\n24:00",self.centralwidget)

        self.dat4_wbox1=QVBoxLayout()
        self.dat4_dlb=QLabel(dat4k[0][0],self.centralwidget)
        self.dat4_dlb.setPixmap(self.get_img(str(dat4k[0][0]), now_hour, 30, 20))
        self.dat4_telb=QLabel(dat4k[0][1]+"℃   "+str(dat4k[0][4])+"m/s",self.centralwidget)
        self.dat4_rlb=QLabel(dat4k[0][3]+"mm"+"("+str(dat4k[0][2])+"%"+")",self.centralwidget)
        # self.dat4_wlb=QLabel(str(dat4k[0][4])+"m/s",self.centralwidget)
        self.dat4_wbox1.addWidget(self.dat4_dlb)
        self.dat4_wbox1.addWidget(self.dat4_telb)
        self.dat4_wbox1.addWidget(self.dat4_rlb)
        # self.dat4_wbox1.addWidget(self.dat4_wlb)

        self.dat4_wbox2=QVBoxLayout()
        self.dat4_ndlb=QLabel(dat4n[0][0],self.centralwidget)
        self.dat4_ndlb.setPixmap(self.get_img(str(dat4n[0][0]), now_hour, 30, 20))
        self.dat4_ntelb=QLabel(dat4n[0][1]+"℃   "+str(dat4n[0][3])+"m/s",self.centralwidget)
        self.dat4_nrlb=QLabel(dat4n[0][2]+"mm",self.centralwidget)
        # self.dat4_nwlb=QLabel(str(dat4n[0][3])+"m/s",self.centralwidget)
        self.dat4_wbox2.addWidget(self.dat4_ndlb)
        self.dat4_wbox2.addWidget(self.dat4_ntelb)
        self.dat4_wbox2.addWidget(self.dat4_nrlb)
        # self.dat4_wbox2.addWidget(self.dat4_nwlb)

        self.dat_inbox4.addWidget(self.dat4_tlb)
        self.dat_inbox4.addLayout(self.dat4_wbox1)
        self.dat_inbox4.addLayout(self.dat4_wbox2)

        ####
        self.dat_inbox1_frame=QFrame()
        self.dat_inbox1_frame.setObjectName("dat_inbox1_fr")
        self.dat_inbox1_frame.setLayout(self.dat_inbox1)

        self.dat_inbox2_frame=QFrame()
        self.dat_inbox2_frame.setObjectName("dat_inbox2_fr")
        self.dat_inbox2_frame.setLayout(self.dat_inbox2)

        self.dat_inbox3_frame=QFrame()
        self.dat_inbox3_frame.setObjectName("dat_inbox3_fr")
        self.dat_inbox3_frame.setLayout(self.dat_inbox3)

        self.dat_inbox4_frame=QFrame()
        self.dat_inbox4_frame.setObjectName("dat_inbox4_fr")
        self.dat_inbox4_frame.setLayout(self.dat_inbox4)

        ##############
        
        self.datdate_lb=QLabel("모레",self.centralwidget)
        self.dat_box.addWidget(self.datdate_lb)
        self.dat_box.addWidget(self.dat_inbox1_frame)
        self.dat_box.addWidget(self.dat_inbox2_frame)
        self.dat_box.addWidget(self.dat_inbox3_frame)
        self.dat_box.addWidget(self.dat_inbox4_frame)
        
        self.tn_box_frame = QFrame()
        self.tn_box_frame.setObjectName("tn_frame")
        self.tn_box_frame.setLayout(self.today_box)

        self.tn_box.addWidget(self.tn_box_frame)
        
        self.to_box_frame = QFrame()
        self.to_box_frame.setObjectName("tn_frame")
        self.to_box_frame.setLayout(self.tomorrow_box)
        
        self.tn_box.addWidget(self.to_box_frame)
        
        self.dat_box_frame = QFrame()
        self.dat_box_frame.setObjectName("tn_frame")
        self.dat_box_frame.setLayout(self.dat_box)
        
        self.tn_box.addWidget(self.dat_box_frame)

        self.wh_in_box.addLayout(self.tn_box)
        
        ###################################################################### 주간 날씨 박스
        self.week_box = QVBoxLayout()
        
        self.korea_box=QHBoxLayout()
        self.korea_lb=QLabel("기\n상\n청")

        kweek1=excute('select WWH_FORECAST, WWH_TEMP, WWH_PREC_PROB from sm_wwh_tb where WWH_NO = (select max(WWH_NO) from sm_wwh_tb where WWH_DATE=:wday and WWH_LOC=:loc and WWH_TYPE=:num)',[d1,self.chk_loc,1])
        self.kday1_box=QVBoxLayout()
        self.kday1_lb=QLabel(dtitle1+"일",self.centralwidget)
        self.kday1_dlb=QLabel(kweek1[0][0],self.centralwidget)
        self.kday1_dlb.setPixmap(self.get_img(str(kweek1[0][0]), now_hour, 50, 35))
        self.kday1_tlb=QLabel(kweek1[0][1]+" ℃",self.centralwidget)
        self.kday1_plb=QLabel("강수확률 "+str(kweek1[0][2])+"%",self.centralwidget)
        self.kday1_box.addWidget(self.kday1_lb)
        self.kday1_box.addWidget(self.kday1_dlb)
        self.kday1_box.addWidget(self.kday1_tlb)
        self.kday1_box.addWidget(self.kday1_plb)

        kweek2=excute('select WWH_FORECAST, WWH_TEMP, WWH_PREC_PROB from sm_wwh_tb where WWH_NO = (select max(WWH_NO) from sm_wwh_tb where WWH_DATE=:wday and WWH_LOC=:loc and WWH_TYPE=:num)',[d2,self.chk_loc,1])
        self.kday2_box=QVBoxLayout()
        self.kday2_lb=QLabel(dtitle2+"일",self.centralwidget)
        self.kday2_dlb=QLabel(kweek2[0][0],self.centralwidget)
        self.kday2_dlb.setPixmap(self.get_img(str(kweek2[0][0]), now_hour, 50, 35))
        self.kday2_tlb=QLabel(kweek2[0][1]+" ℃",self.centralwidget)
        self.kday2_plb=QLabel("강수확률 "+str(kweek2[0][2])+"%",self.centralwidget)
        self.kday2_box.addWidget(self.kday2_lb)
        self.kday2_box.addWidget(self.kday2_dlb)
        self.kday2_box.addWidget(self.kday2_tlb)
        self.kday2_box.addWidget(self.kday2_plb)

        kweek3=excute('select WWH_FORECAST, WWH_TEMP, WWH_PREC_PROB from sm_wwh_tb where WWH_NO = (select max(WWH_NO) from sm_wwh_tb where WWH_DATE=:wday and WWH_LOC=:loc and WWH_TYPE=:num)',[d3,self.chk_loc,1])
        self.kday3_box=QVBoxLayout()
        self.kday3_lb=QLabel(dtitle3+"일",self.centralwidget)
        self.kday3_dlb=QLabel(kweek3[0][0],self.centralwidget)
        self.kday3_dlb.setPixmap(self.get_img(str(kweek3[0][0]), now_hour, 50, 35))
        self.kday3_tlb=QLabel(kweek3[0][1]+" ℃",self.centralwidget)
        self.kday3_plb=QLabel("강수확률 "+str(kweek3[0][2])+"%",self.centralwidget)
        self.kday3_box.addWidget(self.kday3_lb)
        self.kday3_box.addWidget(self.kday3_dlb)
        self.kday3_box.addWidget(self.kday3_tlb)
        self.kday3_box.addWidget(self.kday3_plb)

        kweek4=excute('select WWH_FORECAST, WWH_TEMP, WWH_PREC_PROB from sm_wwh_tb where WWH_NO = (select max(WWH_NO) from sm_wwh_tb where WWH_DATE=:wday and WWH_LOC=:loc and WWH_TYPE=:num)',[d4,self.chk_loc,1])
        self.kday4_box=QVBoxLayout()
        self.kday4_lb=QLabel(dtitle4+"일",self.centralwidget)
        self.kday4_dlb=QLabel(kweek4[0][0],self.centralwidget)
        self.kday4_dlb.setPixmap(self.get_img(str(kweek4[0][0]), now_hour, 50, 35))
        self.kday4_tlb=QLabel(kweek4[0][1]+" ℃",self.centralwidget)
        self.kday4_plb=QLabel("강수확률 "+str(kweek4[0][2])+"%",self.centralwidget)
        self.kday4_box.addWidget(self.kday4_lb)
        self.kday4_box.addWidget(self.kday4_dlb)
        self.kday4_box.addWidget(self.kday4_tlb)
        self.kday4_box.addWidget(self.kday4_plb)

        kweek5=excute('select WWH_FORECAST, WWH_TEMP, WWH_PREC_PROB from sm_wwh_tb where WWH_NO = (select max(WWH_NO) from sm_wwh_tb where WWH_DATE=:wday and WWH_LOC=:loc and WWH_TYPE=:num)',[d5,self.chk_loc,1])
        self.kday5_box=QVBoxLayout()
        self.kday5_lb=QLabel(dtitle5+"일",self.centralwidget)
        self.kday5_dlb=QLabel(kweek5[0][0],self.centralwidget)
        self.kday5_dlb.setPixmap(self.get_img(str(kweek5[0][0]), now_hour, 50, 35))
        self.kday5_tlb=QLabel(kweek5[0][1]+" ℃",self.centralwidget)
        self.kday5_plb=QLabel("강수확률 "+str(kweek5[0][2])+"%",self.centralwidget)
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

        # 노르웨이 주간 날씨
        self.norway_box=QHBoxLayout()
        self.norway_lb=QLabel("노\n르\n웨\n이")

        nweek1=excute('select WWH_FORECAST, WWH_TEMP, WWH_PREC, WWH_WIND from sm_wwh_tb where WWH_NO = (select max(WWH_NO) from sm_wwh_tb where WWH_DATE=:wday and WWH_LOC=:loc and WWH_TYPE=:num)',[d1,self.chk_loc,2])
        self.nday1_box=QVBoxLayout()
        self.nday1_dlb=QLabel(nweek1[0][0],self.centralwidget)
        self.nday1_dlb.setPixmap(self.get_img(str(nweek1[0][0]), now_hour, 50, 35))
        self.nday1_tlb=QLabel(nweek1[0][1]+"℃",self.centralwidget)
        self.nday1_rlb=QLabel(nweek1[0][2]+"mm",self.centralwidget)
        self.nday1_wlb=QLabel(str(nweek1[0][3])+"m/s",self.centralwidget)
        self.nday1_box.addWidget(self.nday1_dlb)
        self.nday1_box.addWidget(self.nday1_tlb)
        self.nday1_box.addWidget(self.nday1_rlb)
        self.nday1_box.addWidget(self.nday1_wlb)

        nweek2=excute('select WWH_FORECAST, WWH_TEMP, WWH_PREC, WWH_WIND from sm_wwh_tb where WWH_NO = (select max(WWH_NO) from sm_wwh_tb where WWH_DATE=:wday and WWH_LOC=:loc and WWH_TYPE=:num)',[d2,self.chk_loc,2])

        self.nday2_box=QVBoxLayout()
        self.nday2_dlb=QLabel(nweek2[0][0],self.centralwidget)
        self.nday2_dlb.setPixmap(self.get_img(str(nweek2[0][0]), now_hour, 50, 35))
        self.nday2_tlb=QLabel(nweek2[0][1]+"℃",self.centralwidget)
        self.nday2_rlb=QLabel(nweek2[0][2]+"mm",self.centralwidget)
        self.nday2_wlb=QLabel(str(nweek2[0][3])+"m/s",self.centralwidget)
        self.nday2_box.addWidget(self.nday2_dlb)
        self.nday2_box.addWidget(self.nday2_tlb)
        self.nday2_box.addWidget(self.nday2_rlb)
        self.nday2_box.addWidget(self.nday2_wlb)

        nweek3=excute('select WWH_FORECAST, WWH_TEMP, WWH_PREC, WWH_WIND from sm_wwh_tb where WWH_NO = (select max(WWH_NO) from sm_wwh_tb where WWH_DATE=:wday and WWH_LOC=:loc and WWH_TYPE=:num)',[d3,self.chk_loc,2])
        self.nday3_box=QVBoxLayout()
        self.nday3_dlb=QLabel(nweek3[0][0],self.centralwidget)
        self.nday3_dlb.setPixmap(self.get_img(str(nweek3[0][0]), now_hour, 50, 35))
        self.nday3_tlb=QLabel(nweek3[0][1]+"℃",self.centralwidget)
        self.nday3_rlb=QLabel(nweek3[0][2]+"mm",self.centralwidget)
        self.nday3_wlb=QLabel(str(nweek3[0][3])+"m/s",self.centralwidget)
        self.nday3_box.addWidget(self.nday3_dlb)
        self.nday3_box.addWidget(self.nday3_tlb)
        self.nday3_box.addWidget(self.nday3_rlb)
        self.nday3_box.addWidget(self.nday3_wlb)

        nweek4=excute('select WWH_FORECAST, WWH_TEMP, WWH_PREC, WWH_WIND from sm_wwh_tb where WWH_NO = (select max(WWH_NO) from sm_wwh_tb where WWH_DATE=:wday and WWH_LOC=:loc and WWH_TYPE=:num)',[d4,self.chk_loc,2])
        self.nday4_box=QVBoxLayout()
        self.nday4_dlb=QLabel(nweek4[0][0],self.centralwidget)
        self.nday4_dlb.setPixmap(self.get_img(str(nweek4[0][0]), now_hour, 50, 35))
        self.nday4_tlb=QLabel(nweek4[0][1]+"℃",self.centralwidget)
        self.nday4_rlb=QLabel(nweek4[0][2]+"mm",self.centralwidget)
        self.nday4_wlb=QLabel(str(nweek4[0][3])+"m/s",self.centralwidget)
        self.nday4_box.addWidget(self.nday4_dlb)
        self.nday4_box.addWidget(self.nday4_tlb)
        self.nday4_box.addWidget(self.nday4_rlb)
        self.nday4_box.addWidget(self.nday4_wlb)

        nweek5=excute('select WWH_FORECAST, WWH_TEMP, WWH_PREC, WWH_WIND from sm_wwh_tb where WWH_NO = (select max(WWH_NO) from sm_wwh_tb where WWH_DATE=:wday and WWH_LOC=:loc and WWH_TYPE=:num)',[d5,self.chk_loc,2])
        self.nday5_box=QVBoxLayout()
        self.nday5_dlb=QLabel(nweek5[0][0],self.centralwidget)
        self.nday5_dlb.setPixmap(self.get_img(str(nweek5[0][0]), now_hour, 50, 35))
        self.nday5_tlb=QLabel(nweek5[0][1]+"℃",self.centralwidget)
        self.nday5_rlb=QLabel(nweek5[0][2]+"mm",self.centralwidget)
        self.nday5_wlb=QLabel(str(nweek5[0][3])+"m/s",self.centralwidget)
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

        self.korea_box_frame = QFrame()
        self.korea_box_frame.setObjectName("krb_frame")
        self.korea_box_frame.setLayout(self.korea_box)

        self.norway_box_frame = QFrame()
        self.norway_box_frame.setObjectName("nob_frame")
        self.norway_box_frame.setLayout(self.norway_box)

        self.week_box.addWidget(self.korea_box_frame)
        self.week_box.addWidget(self.norway_box_frame)
        
        #####
        self.wh_in_box.addLayout(self.week_box)
        
        self.wh_scrollArea.setLayout(self.wh_in_box)
        # wh_box.addStretch(1)
        self.wh_box.addWidget(self.wh_scrollArea)

        self.vbox.addLayout(self.wh_box)
        
    def rw_btn_setting(self, HomeWindow):
        res = excute("SELECT * FROM SM_RPU_TB WHERE RPU_TNWH_NO = :temp_tnwh_no AND RPU_USER_NO = :user_no", [self.now_tnwh_no, HomeWindow.user_info["user_no"]])
        if len(res) > 0: self.hide_rw()
    
    def rgt_click(self, type, HomeWindow):
        rpu_res = 1
        if type == "W": rpu_res = 2
        
        res = excute("SELECT * FROM SM_RPU_TB WHERE RPU_TNWH_NO = :temp_tnwh_no AND RPU_USER_NO = :user_no", [self.now_tnwh_no, HomeWindow.user_info["user_no"]])
        if len(res) < 1:
            res = excute("INSERT INTO SM_RPU_TB(RPU_NO, RPU_TNWH_NO, RPU_USER_NO, RPU_RES) VALUES(SM_RPU_SEQ.NEXTVAL, :temp_tnwh_no, :user_no, :rpu_res)",
                   [self.now_tnwh_no, HomeWindow.user_info["user_no"], rpu_res])
            if res: 
                QMessageBox.question(self.centralwidget, "현재 날씨", "소중한 의견 갑사합니다. 선택한 의견은 기상청 신뢰도에 반영됩니다.", QMessageBox.Yes, QMessageBox.Yes)
                self.hide_rw()
    
    def hide_rw(self):
        self.rw_lb.hide()
        self.rgt_btn.hide()
        self.wrg_btn.hide()

        res_tot = excute("select trunc(part/tot*100) from (select count(*) as tot from SM_RPU_TB), (select count(*) as part from SM_RPU_TB where rpu_res = :txt_res)", [1])
        res_loc = excute("select trunc(part/tot*100) from (select count(*) as tot from SM_RPU_TB where rpu_tnwh_no in (select tnwh_no from sm_tnwh_tb where tnwh_loc = :txt_loc1)), (select count(*) as part from SM_RPU_TB where rpu_tnwh_no in (select tnwh_no from sm_tnwh_tb where tnwh_loc = :txt_loc2) and rpu_res = :txt_res)", [self.chk_loc, self.chk_loc, 1])

        txt_loc = "서울"
        if self.chk_loc == 2: txt_loc = "강릉"
        elif self.chk_loc == 3: txt_loc = "대전"
        elif self.chk_loc == 4: txt_loc = "광주"
        elif self.chk_loc == 5: txt_loc = "울산"

        self.rlb_lb.setText("  | 전체 지역 기상청 신뢰도: " + str(res_tot[0][0]) + "%   |   " + txt_loc + " 기상청 신뢰도: " + str(res_loc[0][0]) + "% |")
        
    def rcdUI(self):
        self.rcd_title = QLabel("이거\n어때요?", self.centralwidget)
        self.rcd_title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.music = QPushButton("노래", self.centralwidget)
        self.music.clicked.connect(self.music_play)
        self.food = QPushButton("음식", self.centralwidget)
        self.food.clicked.connect(self.food_play)
        self.activity = QPushButton("활동", self.centralwidget)
        self.activity.clicked.connect(self.activity_play)
        
        click_pixmap = QPixmap("./project/img/btn_click.png")
        click_pixmap = click_pixmap.scaled(30, 30)
        
        self.music_click_img = QLabel("MUSIC_CLICK", self.centralwidget)
        self.music_click_img.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.music_click_img.setPixmap(click_pixmap)
        
        self.food_click_img = QLabel("FOOD_CLICK", self.centralwidget)
        self.food_click_img.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.food_click_img.setPixmap(click_pixmap)
        
        self.activity_click_img = QLabel("ACTIVITY_CLICK", self.centralwidget)
        self.activity_click_img.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
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
        
    def set_rcd_url(self):
        # self.res1 = excute("select rcd_url from sm_rcd_tb where rcd_tnwh_no = (select tnwh_no from sm_tnwh_tb where tnwh_type = :txt_tnwh_type and tnwh_date = :txt_today and tnwh_loc = :txt_loc and tnwh_time = :txt_time) and rcd_type = :txt_rcd_type and ROWNUM <= 5 order by rcd_no asc",[3, today, self.chk_loc, now_hour, 1])
        # self.res2 = excute("select rcd_url from sm_rcd_tb where rcd_tnwh_no = (select tnwh_no from sm_tnwh_tb where tnwh_type = :txt_tnwh_type and tnwh_date = :txt_today and tnwh_loc = :txt_loc and tnwh_time = :txt_time) and rcd_type = :txt_rcd_type and ROWNUM <= 5 order by rcd_no asc",[3, today, self.chk_loc, now_hour, 3])
        # self.res3 = excute("select rcd_url from sm_rcd_tb where rcd_tnwh_no = (select tnwh_no from sm_tnwh_tb where tnwh_type = :txt_tnwh_type and tnwh_date = :txt_today and tnwh_loc = :txt_loc and tnwh_time = :txt_time) and rcd_type = :txt_rcd_type and ROWNUM <= 1 order by rcd_no asc",[3, today, self.chk_loc, now_hour, 2])
        self.res1 = excute("select rcd_url from sm_rcd_tb where rcd_tnwh_no = :txt_now_tnwh_no and rcd_type = :txt_rcd_type and ROWNUM <= 5 order by rcd_no asc",[self.now_tnwh_no, 1])
        self.res2 = excute("select rcd_url from sm_rcd_tb where rcd_tnwh_no = :txt_now_tnwh_no and rcd_type = :txt_rcd_type and ROWNUM <= 5 order by rcd_no asc",[self.now_tnwh_no, 3])
        self.res3 = excute("select rcd_url from sm_rcd_tb where rcd_tnwh_no = :txt_now_tnwh_no and rcd_type = :txt_rcd_type and ROWNUM <= 1 order by rcd_no asc",[self.now_tnwh_no, 2])
    
    def music_play(self):
        self.toggle("Y")
        self.music_click_img.show()
        self.food_click_img.hide()
        self.activity_click_img.hide()
        self.music.setStyleSheet("width: 80px; height: 30px; color: #FFFFFF; border: 5px red solid; border-radius: 3px; background-color: #FF8C0A; font-size: 12pt;")
        self.webview1.setUrl(QUrl(self.res1[0][0])) 
        self.webview2.setUrl(QUrl(self.res1[1][0])) 
        self.webview3.setUrl(QUrl(self.res1[2][0])) 
        self.webview4.setUrl(QUrl(self.res1[3][0])) 
        self.webview5.setUrl(QUrl(self.res1[4][0])) 
      
    def food_play(self):
        self.toggle("Y")
        self.music_click_img.hide()
        self.food_click_img.show()
        self.activity_click_img.hide()
        self.webview1.setUrl(QUrl(self.res2[0][0]))
        self.webview2.setUrl(QUrl(self.res2[1][0]))
        self.webview3.setUrl(QUrl(self.res2[2][0]))
        self.webview4.setUrl(QUrl(self.res2[3][0]))
        self.webview5.setUrl(QUrl(self.res2[4][0]))
    
    def activity_play(self):
        self.music_click_img.hide()
        self.food_click_img.hide()
        self.activity_click_img.show()
        self.webview1.setUrl(QUrl(self.res3[0][0]))
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
            
    def set_base_style(self):
        logout_style = "width: 80px; height: 30px; color: #1E90FF; border: 2px #1E90FF solid; border-radius: 3px; background-color: #FFFFFF; font-size: 12pt;"
        loc_radio_style = "font-size: 12pt;"
        rw_lb_style = "font-size: 10pt; color: #4C4C4C; font-weight: bold;"
        rgt_style = "width: 80px; height: 30px; color: #FFFFFF; border: 2px #006400 solid; border-radius: 3px; background-color: #64CD32; font-size: 12pt;"
        wrg_style = "width: 80px; height: 30px; color: #FFFFFF; border: 2px #006400 solid; border-radius: 3px; background-color: #FF1900; font-size: 12pt;"
        rlb_style = "font-size: 10pt;"
        rcd_title_style = "font-size: 14pt; color: #B9062F; font-weight: bold; " #rcd_title_style = "font-size: 14pt; color: #B9062F; font-weight: bold;border-style: solid; border-width: 2px; border-color: #B9062F; border-radius: 10px"
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
        
        self.rlb_lb.setStyleSheet(rlb_style)
        
        self.rcd_title.setStyleSheet(rcd_title_style)
        self.music.setStyleSheet(music_style)
        self.food.setStyleSheet(food_style)
        self.activity.setStyleSheet(activity_style)

    def set_tnw_style(self):
        t_title_lb_style = "font-family: '1훈정글북 Regular'; font-size: 12pt; color: #FFFFFF; font-weight: bold; background-color: #FF3232; border-radius: 3px;"
        to_title_lb_style = "font-family: '1훈정글북 Regular'; font-size: 12pt; color: #FFFFFF; font-weight: bold; background-color: #FFB400; border-radius: 3px; padding:0px;"
        dat_title_lb_style = "font-family: '1훈정글북 Regular'; font-size: 12pt; color: #FFFFFF; font-weight: bold; background-color: #FFD228; border-radius: 3px; padding:0px;"
        tn_lb_style = "font-family: '나눔고딕'; font-size: 10pt; font-weight: bold; color: #4C4C4C;"
        tn_s_lb_style = "font-family: '나눔고딕'; font-size: 9pt; color: #505050;"
        kw_style = "font-family: '1훈정글북 Regular'; font-size: 12pt; color: #FFFFFF; font-weight: bold; background-color: #5AD18F; border-radius: 3px; padding:0px;"
        nw_style = "font-family: '1훈정글북 Regular'; font-size: 12pt; color: #FFFFFF; font-weight: bold; background-color: #78A9ED; border-radius: 3px; padding:0px;"

        self.line1.setStyleSheet("color: red; font-size: 2pt; padding: 0; margin: 0;")
        self.line2.setStyleSheet("color: red; font-size: 2pt; padding: 0; margin: 0;")
        self.line3.setStyleSheet("color: red; font-size: 2pt; padding: 0; margin: 0;")
        self.line4.setStyleSheet("color: red; font-size: 2pt; padding: 0; margin: 0;")
        
        # 오늘 현재 label style
        self.tdate_lb.setStyleSheet(t_title_lb_style)
        self.tdate_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.tdraw_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.ttemp_lb.setStyleSheet(tn_lb_style)
        self.ttemp_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.train_lb.setStyleSheet(tn_lb_style)
        self.train_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.twind_lb.setStyleSheet(tn_lb_style)
        self.twind_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # 오늘 시간별 label style
        self.tfull1_lb.setStyleSheet(tn_lb_style)
        self.tfull1_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.tfull2_lb.setStyleSheet(tn_lb_style)
        self.tfull2_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.tfull3_lb.setStyleSheet(tn_lb_style)
        self.tfull3_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.tfull4_lb.setStyleSheet(tn_lb_style)
        self.tfull4_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # 오늘 00:00 - 06:00 label style
        self.tfull_0d_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tfull_0w_tlb.setStyleSheet(tn_s_lb_style)
        self.tfull_0w_rlb.setStyleSheet(tn_s_lb_style)
        self.tfull_0w_wlb.setStyleSheet(tn_s_lb_style)
        
        # 오늘 06:00 - 12:00 albel style
        self.tfull_6d_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tfull_6w_tlb.setStyleSheet(tn_s_lb_style)
        self.tfull_6w_rlb.setStyleSheet(tn_s_lb_style)
        self.tfull_6w_wlb.setStyleSheet(tn_s_lb_style)
        
        # 오늘 12:00 - 18:00 albel style
        self.tfull_12d_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tfull_12w_tlb.setStyleSheet(tn_s_lb_style)
        self.tfull_12w_rlb.setStyleSheet(tn_s_lb_style)
        self.tfull_12w_wlb.setStyleSheet(tn_s_lb_style)
        
        # 오늘 18:00 - 24:00 albel style
        self.tfull_18d_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tfull_18w_tlb.setStyleSheet(tn_s_lb_style)
        self.tfull_18w_rlb.setStyleSheet(tn_s_lb_style)
        self.tfull_18w_wlb.setStyleSheet(tn_s_lb_style)
        
        # 내일 날씨
        self.todate_lb.setFixedSize(238, 19)
        self.todate_lb.setStyleSheet(to_title_lb_style)
        self.todate_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.tm1_tlb.setStyleSheet(tn_lb_style)
        self.tm1_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm2_tlb.setStyleSheet(tn_lb_style)
        self.tm2_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm3_tlb.setStyleSheet(tn_lb_style)
        self.tm3_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm4_tlb.setStyleSheet(tn_lb_style)
        self.tm4_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # 기상청
        self.tm1_klb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.tm1_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm1_telb.setStyleSheet(tn_s_lb_style)
        self.tm1_rlb.setStyleSheet(tn_s_lb_style)
        # self.tm1_wlb.setStyleSheet(tn_s_lb_style)

        self.tm2_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm2_telb.setStyleSheet(tn_s_lb_style)
        self.tm2_rlb.setStyleSheet(tn_s_lb_style)
        # self.tm2_wlb.setStyleSheet(tn_s_lb_style)

        self.tm3_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm3_telb.setStyleSheet(tn_s_lb_style)
        self.tm3_rlb.setStyleSheet(tn_s_lb_style)
        # self.tm3_wlb.setStyleSheet(tn_s_lb_style)

        self.tm4_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm4_telb.setStyleSheet(tn_s_lb_style)
        self.tm4_rlb.setStyleSheet(tn_s_lb_style)
        # self.tm4_wlb.setStyleSheet(tn_s_lb_style)

        # 노르웨이
        self.tm1_nlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.tm1_ndlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm1_ntelb.setStyleSheet(tn_s_lb_style)
        self.tm1_nrlb.setStyleSheet(tn_s_lb_style)
        # self.tm1_nwlb.setStyleSheet(tn_s_lb_style)

        self.tm2_ndlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm2_ntelb.setStyleSheet(tn_s_lb_style)
        self.tm2_nrlb.setStyleSheet(tn_s_lb_style)
        # self.tm2_nwlb.setStyleSheet(tn_s_lb_style)

        self.tm3_ndlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm3_ntelb.setStyleSheet(tn_s_lb_style)
        self.tm3_nrlb.setStyleSheet(tn_s_lb_style)
        # self.tm3_nwlb.setStyleSheet(tn_s_lb_style)

        self.tm4_ndlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tm4_ntelb.setStyleSheet(tn_s_lb_style)
        self.tm4_nrlb.setStyleSheet(tn_s_lb_style)
        # self.tm4_nwlb.setStyleSheet(tn_s_lb_style)

        # 모래 날씨
        self.datdate_lb.setFixedSize(238, 19)
        self.datdate_lb.setStyleSheet(dat_title_lb_style)
        self.datdate_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.dat1_tlb.setStyleSheet(tn_lb_style)
        self.dat1_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat2_tlb.setStyleSheet(tn_lb_style)
        self.dat2_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat3_tlb.setStyleSheet(tn_lb_style)
        self.dat3_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat4_tlb.setStyleSheet(tn_lb_style)
        self.dat4_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # 기상청
        self.dat1_klb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.dat1_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat1_telb.setStyleSheet(tn_s_lb_style)
        self.dat1_rlb.setStyleSheet(tn_s_lb_style)
        # self.dat1_wlb.setStyleSheet(tn_s_lb_style)

        self.dat2_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat2_telb.setStyleSheet(tn_s_lb_style)
        self.dat2_rlb.setStyleSheet(tn_s_lb_style)
        # self.dat2_wlb.setStyleSheet(tn_s_lb_style)

        self.dat3_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat3_telb.setStyleSheet(tn_s_lb_style)
        self.dat3_rlb.setStyleSheet(tn_s_lb_style)
        # self.dat3_wlb.setStyleSheet(tn_s_lb_style)

        self.dat4_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat4_telb.setStyleSheet(tn_s_lb_style)
        self.dat4_rlb.setStyleSheet(tn_s_lb_style)
        # self.dat4_wlb.setStyleSheet(tn_s_lb_style)

        # 노르웨이
        self.dat1_nlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.dat1_ndlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat1_ntelb.setStyleSheet(tn_s_lb_style)
        self.dat1_nrlb.setStyleSheet(tn_s_lb_style)
        # self.dat1_nwlb.setStyleSheet(tn_s_lb_style)

        self.dat2_ndlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat2_ntelb.setStyleSheet(tn_s_lb_style)
        self.dat2_nrlb.setStyleSheet(tn_s_lb_style)
        # self.dat2_nwlb.setStyleSheet(tn_s_lb_style)

        self.dat3_ndlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat3_ntelb.setStyleSheet(tn_s_lb_style)
        self.dat3_nrlb.setStyleSheet(tn_s_lb_style)
        # self.dat3_nwlb.setStyleSheet(tn_s_lb_style)

        self.dat4_ndlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dat4_ntelb.setStyleSheet(tn_s_lb_style)
        self.dat4_nrlb.setStyleSheet(tn_s_lb_style)
        # self.dat4_nwlb.setStyleSheet(tn_s_lb_style)

        # 기상청 주간 날씨
        # 제목, 날짜
        self.korea_lb.setStyleSheet(kw_style)
        self.korea_lb.setFixedSize(19, 175)
        self.korea_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.kday1_lb.setStyleSheet(kw_style)
        self.kday1_lb.setFixedSize(140, 19)
        self.kday1_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.kday2_lb.setStyleSheet(kw_style)
        self.kday2_lb.setFixedSize(140, 19)
        self.kday2_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.kday3_lb.setStyleSheet(kw_style)
        self.kday3_lb.setFixedSize(140, 19)
        self.kday3_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.kday4_lb.setStyleSheet(kw_style)
        self.kday4_lb.setFixedSize(140, 19)
        self.kday4_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.kday5_lb.setStyleSheet(kw_style)
        self.kday5_lb.setFixedSize(140, 19)
        self.kday5_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # 내용
        self.kday1_dlb.setStyleSheet(tn_s_lb_style)
        self.kday1_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.kday1_tlb.setStyleSheet(tn_s_lb_style)
        self.kday1_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.kday1_plb.setStyleSheet(tn_s_lb_style)
        self.kday1_plb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.kday2_dlb.setStyleSheet(tn_s_lb_style)
        self.kday2_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.kday2_tlb.setStyleSheet(tn_s_lb_style)
        self.kday2_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.kday2_plb.setStyleSheet(tn_s_lb_style)
        self.kday2_plb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.kday3_dlb.setStyleSheet(tn_s_lb_style)
        self.kday3_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.kday3_tlb.setStyleSheet(tn_s_lb_style)
        self.kday3_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.kday3_plb.setStyleSheet(tn_s_lb_style)
        self.kday3_plb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.kday4_dlb.setStyleSheet(tn_s_lb_style)
        self.kday4_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.kday4_tlb.setStyleSheet(tn_s_lb_style)
        self.kday4_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.kday4_plb.setStyleSheet(tn_s_lb_style)
        self.kday4_plb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.kday5_dlb.setStyleSheet(tn_s_lb_style)
        self.kday5_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.kday5_tlb.setStyleSheet(tn_s_lb_style)
        self.kday5_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.kday5_plb.setStyleSheet(tn_s_lb_style)
        self.kday5_plb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # 노르웨이 주간 날씨
        self.norway_lb.setStyleSheet(nw_style)
        self.norway_lb.setFixedSize(19,  175)
        self.norway_lb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # 내용
        self.nday1_dlb.setStyleSheet(tn_s_lb_style) 
        self.nday1_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday1_tlb.setStyleSheet(tn_s_lb_style)
        self.nday1_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday1_rlb.setStyleSheet(tn_s_lb_style)
        self.nday1_rlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday1_wlb.setStyleSheet(tn_s_lb_style)
        self.nday1_wlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.nday2_dlb.setStyleSheet(tn_s_lb_style) 
        self.nday2_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday2_tlb.setStyleSheet(tn_s_lb_style)
        self.nday2_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday2_rlb.setStyleSheet(tn_s_lb_style)
        self.nday2_rlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday2_wlb.setStyleSheet(tn_s_lb_style)
        self.nday2_wlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.nday3_dlb.setStyleSheet(tn_s_lb_style) 
        self.nday3_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday3_tlb.setStyleSheet(tn_s_lb_style)
        self.nday3_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday3_rlb.setStyleSheet(tn_s_lb_style)
        self.nday3_rlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday3_wlb.setStyleSheet(tn_s_lb_style)
        self.nday3_wlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.nday4_dlb.setStyleSheet(tn_s_lb_style) 
        self.nday4_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday4_tlb.setStyleSheet(tn_s_lb_style)
        self.nday4_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday4_rlb.setStyleSheet(tn_s_lb_style)
        self.nday4_rlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday4_wlb.setStyleSheet(tn_s_lb_style)
        self.nday4_wlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.nday5_dlb.setStyleSheet(tn_s_lb_style) 
        self.nday5_dlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday5_tlb.setStyleSheet(tn_s_lb_style)
        self.nday5_tlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday5_rlb.setStyleSheet(tn_s_lb_style)
        self.nday5_rlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nday5_wlb.setStyleSheet(tn_s_lb_style)
        self.nday5_wlb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # 날씨 frame
        self.tn_box_frame.setStyleSheet("#tn_frame{border:1px solid #FF3232; background-color: #FFDCDC; border-radius: 5px;}")
        self.to_box_frame.setStyleSheet("#tn_frame{border:1px solid #FFB400; background-color: #FDE6BE; border-radius: 5px;}")
        self.dat_box_frame.setStyleSheet("#tn_frame{border:1px solid #FFD228; background-color: #FAFAD2; border-radius: 5px;}")
        
        self.korea_box_frame.setStyleSheet("#krb_frame{border:1px solid #5AD18F; background-color: #E6FFE6; border-radius: 5px;}")
        self.norway_box_frame.setStyleSheet("#nob_frame{border:1px solid #78A9ED; background-color: #D7F1FA; border-radius: 5px;}")

        self.tfull_0box_frame.setStyleSheet("#tfull_0box_frame{border-bottom:1px solid #FF3232; background-color: #FFDCDC;}")
        self.tfull_6box_frame.setStyleSheet("#tfull_6box_frame{border-bottom:1px solid #FF3232; background-color: #FFDCDC;}")
        self.tfull_12box_frame.setStyleSheet("#tfull_12box_frame{border-bottom:1px solid #FF3232; background-color: #FFDCDC;}")

        self.tomorrow_inbox1_frame.setStyleSheet("#tomorrow_inbox1_fr{border-bottom:1px solid #FFB400; background-color: #FDE6BE;}")
        self.tomorrow_inbox2_frame.setStyleSheet("#tomorrow_inbox2_fr{border-bottom:1px solid #FFB400; background-color: #FDE6BE;}")
        self.tomorrow_inbox3_frame.setStyleSheet("#tomorrow_inbox3_fr{border-bottom:1px solid #FFB400; background-color: #FDE6BE;}")

        self.dat_inbox1_frame.setStyleSheet("#dat_inbox1_fr{border-bottom:1px solid #FFD228; background-color: #FAFAD2;}")
        self.dat_inbox2_frame.setStyleSheet("#dat_inbox2_fr{border-bottom:1px solid #FFD228; background-color: #FAFAD2;}")
        self.dat_inbox3_frame.setStyleSheet("#dat_inbox3_fr{border-bottom:1px solid #FFD228; background-color: #FAFAD2;}")