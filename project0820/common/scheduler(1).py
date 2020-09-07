# PS E:\dev\python_workspace> pip install apscheduler
from apscheduler.schedulers.background import BackgroundScheduler 
from apscheduler.jobstores.base import JobLookupError 
from youtube_search import YoutubeSearch
from bs4 import BeautifulSoup as bs
from datetime import date,datetime,timedelta
from pprint import pprint
import time 
import cx_Oracle
import requests
import urllib.parse

def wther(): 
    print("wther", "| [time] " , str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
    print("------------------------------------날씨 크롤링------------------------------------")
    today=date.today().isoformat()
    kw_ntime=time.localtime().tm_hour

    def kw_now(url,loc):
        kw_url=url

        kw_res=requests.get(kw_url)
        kw_res.raise_for_status()

        kw_soup=bs(kw_res.text,'lxml')

        kw_div=kw_soup.find("div",attrs={"class","now_weather1"})
        kw_dds=kw_div.find_all('dd',attrs={'class','now_weather1_center'})

        kw_ntemp=kw_dds[0].get_text()[:-1]

        kw_nwin=kw_dds[1].get_text().split(" ")[1]
        if kw_nwin.find('km/h')!=-1:
            kw_nwind=round(float(kw_nwin[:-4])*0.277778,2)
        else:
            kw_nwind=float(kw_nwin[:-3])

        kw_nrainfall=kw_dds[3].get_text()
        if kw_nrainfall=="-":
            kw_nrainfall=0
        else:
            #강수량 있을 때 다시!!!
            pass

        kw_div2=kw_soup.find('div',attrs={'class','time_weather1'})
        kw_dd=kw_div2.find('dd',attrs={'class','time_weather1_left icon'})
        kw_ndraw=kw_dd.find('img')['alt']
        
        # connection=cx_Oracle.connect('scott','tigertiger','orcl.cyemppkgt3jv.ap-northeast-2.rds.amazonaws.com:1521/orcl')
        connection=cx_Oracle.connect('scott','tiger','192.168.0.69:1521/orcl')
        cur=connection.cursor()
        sql="insert into SM_TNWH_TB(TNWH_NO, TNWH_LOC, TNWH_TIME, TNWH_DATE, TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND, TNWH_TYPE) values(SM_TNWH_SEQ.NEXTVAL, :TNWH_LOC, :TNWH_TIME, :TNWH_DATE, :TNWH_FORECAST, :TNWH_TEMP, :TNWH_PREC, :TNWH_WIND, :TNWH_TYPE)"
        
        cur.execute(sql,[loc, kw_ntime, today, kw_ndraw, kw_ntemp, kw_nrainfall, kw_nwind, 3])
        
        connection.commit()
        connection.close()

    kw_now("https://www.weather.go.kr/weather/forecast/timeseries.jsp",1)
    kw_now("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=90&y=136&unit=K",2)
    kw_now("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=66&y=102&unit=K",3)
    kw_now("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=60&y=75&unit=K",4)
    kw_now("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=100&y=84&unit=K",5)
    print("----------------------------------------------")
    
def rcd(): 
    print("rcd", "| [time] " , str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
    print("------------------------------------추천 크롤링------------------------------------")
    #----------------------db에서 현재 날씨 번호, 현재 날씨 가져오기 -----------------------------------------
    connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
    cur = connection.cursor()
    sql = """
    SELECT
    TNWH_NO,TNWH_FORECAST,TNWH_TIME,TNWH_DATE
    FROM
    SM_TNWH_TB
    WHERE
    TNWH_TIME = :txt1
    AND
    SUBSTR(TNWH_DATE,9,2) = :txt3
    """
    
    # str(time.localtime().tm_hour) 
    # between
    # SUBSTR(TNWH_TIME,1,2) =< :txt 
    # and 
    # SUBSTR(TNWH_TIME,7,2) >  :txt2

    # and
    cur.execute(sql,[str(time.localtime().tm_hour), str(datetime.today().day)])  #txt = 시간 앞 , txt2 = 시간 뒤 , txt3 = 날짜 //// txt=18, txt2=24 ,

    forecast = []
    weathrtNo = []
    
    for TNWH_NO,TNWH_FORECAST in cur:
        # print("{}\t {} \t {}\t {}  ".format(TNWH_NO,TNWH_FORECAST,TNWH_TIME,TNWH_DATE))
        forecast.append(TNWH_FORECAST)
        weathrtNo.append(TNWH_NO)

    connection.close()
    


    #----------------------------------현재 날씨번호와 현재날씨를 기준으로 크롤링 하여 db에 저장------------------------
    #----------------------------------블로그 크롤링 , 음악 , 영상 3개를 따로 크롤링해야함????

    #TNWH_FORECAST를 기준으로 검색 시작 
    weatherList = ['구름많음','흐리고 비','맑음','흐림','비','구름조금']
    #검색값을 설정해야함.
    #날씨 값을 변경하여 검색자료가 정확하게 나오게 해야함 

    #예)'흐리고 비' 날 추천요리 (x) 흐리고 비 --> '비오는' 으로 변경 
    # 비오는 날 추천 요리로 검색 가능하게 해야함 
    r =''
    for i in range(len(forecast)):
        w = forecast[i]
        if w == '흐리고 비' or w =='비' or w =='소나기':
            r = '비오는' 
        elif w== '구름많음' or w =='흐림' or w =='구름조금':
            r = '흐린'
        elif w== '맑음':
            r = '날씨 좋은'
    for k in range(len(weathrtNo)):  
        # 추천요리
        r_results = YoutubeSearch(r+"날 추천 요리", max_results=10).to_dict() #
        for i in r_results:
            r_url = i['url_suffix'] 
            r_title = i['title']    
            r_thumbnails = i['thumbnails'] 
            r_href = 'https://www.youtube.com/'+r_url  
            r_video = "https://www.youtube.com/embed/"+r_url.split("v=")[-1]+"?autoplay=0"
            r_music = "https://music.youtube.com/"+r_url
        
            connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
            cur = connection.cursor()
            sql = """
                INSERT INTO SM_RCD_TB (SM_RCD_TB.RCD_NO, SM_RCD_TB.RCD_TITLE,SM_RCD_TB.RCD_URL,RCD_TNWH_NO,RCD_TYPE) VALUES (SM_RCD_SEQ.NEXTVAL, :title,:href,:wNo,3)
            """

            cur.execute(sql,[r_title, r_video, weathrtNo[k]])
            connection.commit()
            connection.close()

        # 추천노래 
        r_results = YoutubeSearch(r+"날 추천 노래", max_results=10).to_dict() #
        for i in r_results:
            r_url = i['url_suffix'] 
            r_title = i['title']    
            r_thumbnails = i['thumbnails'] 
            r_href = 'https://www.youtube.com/'+r_url  
            r_video = "https://www.youtube.com/embed/"+r_url.split("v=")[-1]+"?autoplay=0"
            r_music = "https://music.youtube.com/"+r_url
        
            connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
            cur = connection.cursor()
            sql = """
                INSERT INTO SM_RCD_TB (SM_RCD_TB.RCD_NO, SM_RCD_TB.RCD_TITLE,SM_RCD_TB.RCD_URL,RCD_TNWH_NO,RCD_TYPE) VALUES (SM_RCD_SEQ.NEXTVAL, :title,:href,:wNo,1)
            """

            cur.execute(sql,[r_title, r_music,weathrtNo[k]])
            connection.commit()
            connection.close()


        # 추천여행지
        r_plusurl = urllib.parse.quote_plus(r+"날 추천여행지")
        r_url = f"https://search.naver.com/search.naver?where=post&sm=tab_jum&query={r_plusurl}" 
        r_res = requests.get(r_url)
        r_res.raise_for_status()
        r_soup = bs(r_res.text,"lxml")
        r_As = r_soup.find_all("a",attrs={"class","sh_blog_title _sp_each_url _sp_each_title"})      

        for a in r_As:
            r_href = a['href']       
            r_title = a['title']           
            connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
            cur = connection.cursor()
            sql = """
            INSERT INTO SM_RCD_TB (SM_RCD_TB.RCD_NO, SM_RCD_TB.RCD_TITLE,SM_RCD_TB.RCD_URL,RCD_TNWH_NO,RCD_TYPE) VALUES (SM_RCD_SEQ.NEXTVAL, :title,:href,:wNo,2)
            """

            cur.execute(sql,[r_title,r_href,weathrtNo[k]])


            connection.commit()
            connection.close()


    print("----------------------------------------------")

def line():
    print("----------------------------------------------")

rcd()
    
# sched = BackgroundScheduler() 
# sched.start() 

# interval - 매 3조마다 실행 
# sched.add_job(job, 'interval', seconds=3, id="test_2") 
# interval - 매 시간 10분 마다 실행 
# sched.add_job(wther, 'cron', minute="35", second='0', id="wther") 
# sched.add_job(rcd, 'cron', minute="37", second='0', id="rcd")
# sched.add_job(line, 'interval', seconds=600, id="line")

# while True:
#     pass
    
    
    