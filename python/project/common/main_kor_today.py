#기상청 오늘

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import cx_Oracle
from datetime import date,datetime,timedelta 
import time
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

    kw_nprob=int(kw_dds[2].get_text()[:-1])

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
    sql="insert into SM_TNWH_TB(TNWH_NO, TNWH_LOC, TNWH_TIME, TNWH_DATE, TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND, TNWH_PREC_PROB, TNWH_TYPE) values(SM_TNWH_SEQ.NEXTVAL, :TNWH_LOC, :TNWH_TIME, :TNWH_DATE, :TNWH_FORECAST, :TNWH_TEMP, :TNWH_PREC, :TNWH_WIND, :TNWH_PREC_PROB, :TNWH_TYPE)"
    
    cur.execute(sql,[loc, kw_ntime, today, kw_ndraw, kw_ntemp, kw_nrainfall, kw_nwind, kw_nprob, 3])
    
    connection.commit()
    connection.close()

kw_now("https://www.weather.go.kr/weather/forecast/timeseries.jsp",1)
kw_now("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=90&y=136&unit=K",2)
kw_now("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=66&y=102&unit=K",3)
kw_now("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=60&y=75&unit=K",4)
kw_now("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=100&y=84&unit=K",5)