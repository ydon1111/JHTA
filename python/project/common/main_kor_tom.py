#기상청 내일, 모레

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import cx_Oracle
from datetime import date,datetime,timedelta 
t=date.today()
today=t.isoformat()
tom=t+timedelta(days=+1)
tomorrow=tom.isoformat() 
d=tom+timedelta(days=+1)
dat=d.isoformat()

def kw_wDB(url,loc):
    kw_url=url

    kw_res=requests.get(kw_url)
    kw_res.raise_for_status()

    kw_soup=bs(kw_res.text,'lxml')

    kw_table=kw_soup.find("table",attrs={"class","forecastNew3"})

    kw_tr=kw_table.tbody.tr
    kw_tr=kw_tr.next_sibling.next_sibling

    kw_timelist=[] #시간대
    for t in kw_tr.children:
        if t.name=='td':
            for c in t.contents:
                if c.name=='p':
                    kw_time=c.get_text()
                    kw_timelist.append(kw_time)
    # print("시간",kw_timelist)

    kw_tr=kw_tr.next_sibling.next_sibling

    kw_drawlist=[] #날씨그림의 텍스트값
    for t in kw_tr.children:
        if t.name=='td' and len(t.contents)>0:
            kw_draw=t['title']
            kw_drawlist.append(kw_draw)
    # print("그림",kw_drawlist)

    kw_tr=kw_tr.next_sibling.next_sibling

    kw_problist=[] #강수확률
    for t in kw_tr.children:
        if t.name=='td' and len(t.contents)>0:
            kw_prob=int(t.get_text())
            kw_problist.append(kw_prob)
    # print("강수확률",kw_problist)

    kw_tr=kw_tr.next_sibling.next_sibling

    kw_rainlist=[] #강수량
    for t in kw_tr.children:
        if t.name=='td' and len(t.contents)>0:
            kw_rainfall=t.get_text()
            if kw_rainfall.find('-')!=-1:
                kw_rainfall=0
            else:
                kw_rainfall=kw_rainfall.lstrip()
                kw_rainfall=kw_rainfall.rstrip()
                kw_rainfall=kw_rainfall[:-2]
            kw_rainlist.append(kw_rainfall)
    # print("강수량",kw_rainlist)

    kw_tr=kw_tr.next_sibling.next_sibling
    kw_tr=kw_tr.next_sibling.next_sibling

    kw_templist=[] #온도
    for t in kw_tr.children:
        if t.name=='td' and len(t.contents)>0:
            kw_temp=int(t.contents[0].get_text())
            kw_templist.append(kw_temp)
    # print("온도",kw_templist)

    if len(kw_timelist)>len(kw_templist):
        kw_templist.insert(0,kw_templist[0])

    kw_tr=kw_tr.next_sibling.next_sibling

    kw_windlist=[] #풍속
    for t in kw_tr.children:
        if t.name=='td' and len(t.contents)>0:
            con=t.contents[0]
            a=con.find('span',attrs={'class','wind_ws'})
            kw_wind=float(a.get_text())
            kw_windlist.append(kw_wind)
    # print("풍속",kw_windlist)

    if len(kw_timelist)>len(kw_windlist):
        kw_windlist.insert(0,kw_windlist[0])

    kw_tdict={"24":"00:00-06:00","06":"06:00-12:00","12":"12:00-18:00","18":"18:00-24:00"}

    kw_wlist=[]
    kw_wdic=dict()
    for i in range(1,len(kw_timelist)):
        if kw_timelist[i] in ["24","06","12","18"]:
            kw_wdic["시간"]=kw_tdict[kw_timelist[i]]
            kw_wdic["날씨"]=kw_drawlist[i-1]
            kw_wdic["강수확률"]=kw_problist[i-1]
            kw_wdic["강수량"]=kw_rainlist[i//2]

            kw_tsum=0
            kw_cnt=0
            kw_end=i+3
            if i+3>len(kw_timelist):
                kw_end=len(kw_timelist)

            for j in range(i,kw_end):
                kw_tsum+=kw_templist[j] #int(kw_templist[j])
                kw_cnt+=1
            kw_wdic["온도"]=kw_tsum//kw_cnt

            kw_wsum=0
            kw_cnt=0
            for j in range(i,kw_end):
                kw_wsum+=kw_windlist[j]
                kw_cnt+=1
            kw_wdic["풍속"]=kw_wsum//kw_cnt

            kw_wlist.append(kw_wdic)
            kw_wdic=dict() #초기화

    # print(kw_wlist)

    connection=cx_Oracle.connect('scott','tiger','192.168.0.69:1521/orcl')

    cur=connection.cursor()

    sql="insert into SM_TNWH_TB(TNWH_NO, TNWH_LOC, TNWH_TIME, TNWH_DATE, TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND, TNWH_PREC_PROB, TNWH_TYPE) values(SM_TNWH_SEQ.NEXTVAL, :TNWH_LOC, :TNWH_TIME, :TNWH_DATE, :TNWH_FORECAST, :TNWH_TEMP, :TNWH_PREC, :TNWH_WIND, :TNWH_PREC_PROB, :TNWH_TYPE)"

    # kw_todaylist=kw_wlist[:-8]
    kw_tomorrowlist=kw_wlist[-8:-4]
    kw_datlist=kw_wlist[-4:]

    for wlist in kw_tomorrowlist:
        cur.execute(sql,[loc,wlist["시간"],tomorrow,wlist["날씨"],wlist["온도"],wlist["강수량"],wlist["풍속"],wlist["강수확률"],1])

    for wlist in kw_datlist:
        cur.execute(sql,[loc,wlist["시간"],dat,wlist["날씨"],wlist["온도"],wlist["강수량"],wlist["풍속"],wlist["강수확률"],1])

    # if len(kw_todaylist)!=0:
    #     for wlist in kw_todaylist:
    #         cur.execute(sql,[loc,wlist["시간"],today,wlist["날씨"],wlist["온도"],wlist["강수량"],wlist["풍속"],wlist["강수확률"],1])
    connection.commit()
    connection.close()

kw_wDB("https://www.weather.go.kr/weather/forecast/timeseries.jsp",1) #서울
kw_wDB("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=90&y=136&unit=K",2) #강릉
kw_wDB("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=66&y=102&unit=K",3) #대전
kw_wDB("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=60&y=75&unit=K",4) #광주
kw_wDB("http://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=100&y=84&unit=K",5) #울산




