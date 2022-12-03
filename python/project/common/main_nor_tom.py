#노르웨이 내일, 모레

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

# print(today,tomorrow)

def nw_wDB(url,loc):
    w_url=url

    w_res=requests.get(w_url)
    w_res.raise_for_status()

    w_soup=bs(w_res.text,'lxml')

    w_temps=w_soup.find_all("td",attrs={'class','temperature plus'})
    # w_temps=w_temps[:-4]

    w_wlist=[]

    for w_tem in w_temps:
        w_wdic = dict()

        w_presilbing=w_tem.find_previous_sibling()
        w_draw=w_presilbing['title'].split(".")[0] #날씨그림의 텍스트값 저장변수
        w_wdic["날씨"] = w_draw

        w_nextsiblings=w_tem.find_next_siblings()
        for w_sibling in w_nextsiblings:

            w_wcontent=w_sibling.get_text()
            if w_wcontent.find("mm") != -1:
                w_rainfall=w_wcontent[:-3].replace(',','.') #강수량값 저장변수
                w_wdic["강수량"] = w_rainfall

                w_time=w_sibling['title'].split("period:")[1][1:12].replace('–','-') #시간대값 저장변수
                w_wdic["시간"] = w_time

            if w_wcontent.find("m/s") != -1:
                w_wind=float(w_wcontent.lstrip().split(',')[1][1:3]) #풍속값 저장변수
                w_wdic["풍속"] = w_wind
    
        w_temp=int(w_tem.get_text()[:-1]) #온도값 저장변수
        w_wdic["온도"] = w_temp

        w_wlist.append(w_wdic)
        
    # print(w_wlist) 

    # w_todaylist=w_wlist[:-8]
    w_tomorrowlist=w_wlist[-8:-4]
    w_datlist=w_wlist[-4:]

    # connection=cx_Oracle.connect('scott','tigertiger','orcl.cyemppkgt3jv.ap-northeast-2.rds.amazonaws.com:1521/orcl')
    connection=cx_Oracle.connect('scott','tiger','192.168.0.69:1521/orcl')
    # print(connection)

    cur=connection.cursor()

    sql="insert into SM_TNWH_TB(TNWH_NO, TNWH_LOC, TNWH_TIME, TNWH_DATE, TNWH_FORECAST, TNWH_TEMP, TNWH_PREC, TNWH_WIND, TNWH_TYPE) values(SM_TNWH_SEQ.NEXTVAL, :TNWH_LOC, :TNWH_TIME, :TNWH_DATE, :TNWH_FORECAST, :TNWH_TEMP, :TNWH_PREC, :TNWH_WIND, :TNWH_TYPE)"

    # for wlist in w_todaylist:
    #     # print("오늘:",wlist["시간"])
    #     cur.execute(sql,[loc,wlist["시간"],today,wlist["날씨"],wlist["온도"],wlist["강수량"],wlist["풍속"],2])

    for wlist in w_tomorrowlist:
        cur.execute(sql,[loc,wlist["시간"],tomorrow,wlist["날씨"],wlist["온도"],wlist["강수량"],wlist["풍속"],2])

    for wlist in w_datlist:
        cur.execute(sql,[loc,wlist["시간"],dat,wlist["날씨"],wlist["온도"],wlist["강수량"],wlist["풍속"],2])
        
    connection.commit()
    connection.close()

nw_wDB("https://www.yr.no/place/South_Korea/Seoul/Seoul/?spr=eng",1)
nw_wDB("https://www.yr.no/place/South_Korea/Gangwon/Gangneung-si/?spr=eng",2)
nw_wDB("https://www.yr.no/place/South_Korea/Daejeon/Daejeon/?spr=eng",3)
nw_wDB("https://www.yr.no/place/South_Korea/Gwangju/Gwangju/?spr=eng",4)
nw_wDB("https://www.yr.no/place/South_Korea/Ulsan/Ulsan/?spr=eng",5)
