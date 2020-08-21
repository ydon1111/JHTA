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
        
        kday_style = "font-size:10pt; color:black; border-radius: 10px; background-color: #E68282; "

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

        #주간
        #기상청
        self.korea_lb.setFont(font)
        self.kday1_lb.setFont(font)
        self.kday1_dlb.setFont(font)
        self.kday1_tlb.setFont(font)
        self.kday1_plb.setFont(font)
        self.kday2_lb.setFont(font)
        self.kday2_dlb.setFont(font)
        self.kday2_tlb.setFont(font)
        self.kday2_plb.setFont(font)
        self.kday3_lb.setFont(font)
        self.kday3_dlb.setFont(font)
        self.kday3_tlb.setFont(font)
        self.kday3_plb.setFont(font)
        self.kday4_lb.setFont(font)
        self.kday4_dlb.setFont(font)
        self.kday4_tlb.setFont(font)
        self.kday4_plb.setFont(font)
        self.kday5_lb.setFont(font)
        self.kday5_dlb.setFont(font)
        self.kday5_tlb.setFont(font)
        self.kday5_plb.setFont(font)

        self.kday1_lb.setStyleSheet(kday_style)
        self.kday2_lb.setStyleSheet(kday_style)
        self.kday3_lb.setStyleSheet(kday_style)
        self.kday4_lb.setStyleSheet(kday_style)
        self.kday5_lb.setStyleSheet(kday_style)
         
        #노르웨이
        self.norway_lb.setFont(font)
    
        self.nday1_dlb.setFont(font)
        self.nday1_tlb.setFont(font)
        self.nday1_rlb.setFont(font)
        self.nday1_wlb.setFont(font)
     
        self.nday2_dlb.setFont(font)
        self.nday2_tlb.setFont(font)
        self.nday2_rlb.setFont(font)
        self.nday2_wlb.setFont(font)
    
        self.nday3_dlb.setFont(font)
        self.nday3_tlb.setFont(font)
        self.nday3_rlb.setFont(font)
        self.nday3_wlb.setFont(font)
     
        self.nday4_dlb.setFont(font)
        self.nday4_tlb.setFont(font)
        self.nday4_rlb.setFont(font)
        self.nday4_wlb.setFont(font)
    
        self.nday5_dlb.setFont(font)
        self.nday5_tlb.setFont(font)
        self.nday5_rlb.setFont(font)
        self.nday5_wlb.setFont(font)

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
        
    def whUI(self):
        p_img1 = QPixmap("./project/img/sun.png")
        p_img2 = QPixmap("./project/img/rain.png")
        
        #수평상자 레이아웃 객체         
        self.wh_box = QHBoxLayout() # 최상위 box
        self.wh_scrollArea = QScrollArea() # 스크롤
        self.wh_in_box = QHBoxLayout() # 스크롤 안 박스
        ######
        self.tn_box = QHBoxLayout() # 오늘, 내일, 모레 날씨 박스
        self.today_box=QVBoxLayout() #오늘 전체박스
        self.now_box=QVBoxLayout() #오늘=>현재시간대 날씨박스
        # 주간 날씨 박스
        NorwayList = ['Cludy', 'Fair', 'Heavy rain', 'Heavy rain showers' ,'Light rain' , 'Light rain showers', 'Partly cloudy' ,'Rain' ,'Rain showers','Clear sky','Fog']   
        #NowayList는 DB에서불러오는 값으로 변경 
        
        korTran = ''
        if NorwayList[] == 'Cludy' and NorwayList[] == 'Fog':
            korTran = "흐림"
        elif NorwayList[] == 'Heavy rain showers' or NowayList[] == 'Light rain showers' or NowayList[] ==  'Rain showers':
            korTran =  "소나기"
        elif NorwayList[] == 'fair':
            korTran = "구름조금"
        elif NorwayList[] == 'Light rain':
            korTran = "흐리고 비"
        elif NorwayList[] == 'Heavy rain' or NorwayList[] == 'Rain' or NorwayList[] == 'Rain':
            korTran = "비"
        elif NorwayList[] == 'Partly cloudy':
            korTran = "구름많음"
        elif NorwayList[] == 'Clear sky':
            korTran = "맑음"

        koreaDic= {'맑음':"w1",'구름조금':"w3",'구름많음':"w5",'흐림':"w7",'소나기':"w8",'비':"w9",'흐리고 비':"w10",'구름많고 비':"w10",'천둥번개':"w17"}
        
        self.week_box = QVBoxLayout()
        
        self.korea_box=QHBoxLayout()
        self.korea_lb=QLabel("기\n상\n청")

        self.kday1_box=QVBoxLayout()
        self.kday1_lb=QLabel("day1",self.centralwidget)
        self.kday1_dlb=QLabel("day1 날씨그림",self.centralwidget)
        self.kday1_tlb=QLabel("day1 온도",self.centralwidget)
        self.kday1_plb=QLabel("day1 강수확률",self.centralwidget)
        w1 = QPixmap("./project0820/img/"+"w1")
        w1 = w1.scaled(50,50)
        self.kday1_dlb.setPixmap(w1)
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

        self.nday1_box=QVBoxLayout()
        
        self.nday1_dlb=QLabel("day1 날씨그림",self.centralwidget)
        self.nday1_tlb=QLabel("day1 온도",self.centralwidget)
        self.nday1_rlb=QLabel("day1 강수량",self.centralwidget)
        self.nday1_wlb=QLabel("day1 풍속",self.centralwidget)
    
        self.nday1_box.addWidget(self.nday1_dlb)
        self.nday1_box.addWidget(self.nday1_tlb)
        self.nday1_box.addWidget(self.nday1_rlb)
        self.nday1_box.addWidget(self.nday1_wlb)

        self.nday2_box=QVBoxLayout()
      
        self.nday2_dlb=QLabel("day2 날씨그림",self.centralwidget)
        self.nday2_tlb=QLabel("day2 온도",self.centralwidget)
        self.nday2_rlb=QLabel("day2 강수량",self.centralwidget)
        self.nday2_wlb=QLabel("day2 풍속",self.centralwidget)
     
        self.nday2_box.addWidget(self.nday2_dlb)
        self.nday2_box.addWidget(self.nday2_tlb)
        self.nday2_box.addWidget(self.nday2_rlb)
        self.nday2_box.addWidget(self.nday2_wlb)

        self.nday3_box=QVBoxLayout()
        
        self.nday3_dlb=QLabel("day3 날씨그림",self.centralwidget)
        self.nday3_tlb=QLabel("day3 온도",self.centralwidget)
        self.nday3_rlb=QLabel("day3 강수량",self.centralwidget)
        self.nday3_wlb=QLabel("day3 풍속",self.centralwidget)
     
        self.nday3_box.addWidget(self.nday3_dlb)
        self.nday3_box.addWidget(self.nday3_tlb)
        self.nday3_box.addWidget(self.nday3_rlb)
        self.nday3_box.addWidget(self.nday3_wlb)

        self.nday4_box=QVBoxLayout()
        
        self.nday4_dlb=QLabel("day4 날씨그림",self.centralwidget)
        self.nday4_tlb=QLabel("day4 온도",self.centralwidget)
        self.nday4_rlb=QLabel("day4 강수량",self.centralwidget)
        self.nday4_wlb=QLabel("day4 풍속",self.centralwidget)
        
        self.nday4_box.addWidget(self.nday4_dlb)
        self.nday4_box.addWidget(self.nday4_tlb)
        self.nday4_box.addWidget(self.nday4_rlb)
        self.nday4_box.addWidget(self.nday4_wlb)

        self.nday5_box=QVBoxLayout()
     
        self.nday5_dlb=QLabel("day5 날씨그림",self.centralwidget)
        self.nday5_tlb=QLabel("day5 온도",self.centralwidget)
        self.nday5_rlb=QLabel("day5 강수량",self.centralwidget)
        self.nday5_wlb=QLabel("day5 풍속",self.centralwidget)
       
        self.nday5_box.addWidget(self.nday5_dlb)
        self.nday5_box.addWidget(self.nday5_tlb)
        self.nday5_box.addWidget(self.nday5_rlb)
        self.nday5_box.addWidget(self.nday5_wlb)


   
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
        res = excute("SELECT * FROM SM_RPU_TB WHERE RPU_TNWH_NO = :temp_tnwh_no ", [self.temp_tnwh_no])
        if len(res) > 0: self.hide_rw()
    
    def rgt_click(self, type, HomeWindow):
        self.temp_tnwh_no = 471
        rpu_res = 1
        if type == "W": rpu_res = 2
        
        res = excute("SELECT * FROM SM_RPU_TB WHERE RPU_TNWH_NO = :temp_tnwh_no", [self.temp_tnwh_no])
        if len(res) < 1:
            res = excute("INSERT INTO SM_RPU_TB(RPU_NO, RPU_TNWH_NO, RPU_USER_NO, RPU_RES) VALUES(SM_RPU_SEQ.NEXTVAL, :temp_tnwh_no, :rpu_res)",
                   [self.temp_tnwh_no,  rpu_res])
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
            
            
        
        