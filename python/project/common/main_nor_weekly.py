#노르웨이 주간

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import cx_Oracle

from datetime import date,datetime,timedelta 
d1=(date.today()+timedelta(days=+3)).isoformat()
d2=(date.today()+timedelta(days=+4)).isoformat()
d3=(date.today()+timedelta(days=+5)).isoformat()
d4=(date.today()+timedelta(days=+6)).isoformat()
d5=(date.today()+timedelta(days=+7)).isoformat()

def nw_weekly(url,num):
    nw_w_url=url

    nw_w_res=requests.get(nw_w_url)
    nw_w_res.raise_for_status()

    nw_w_soup=bs(nw_w_res.text,'lxml')

    nw_w_tab=nw_w_soup.find("table",attrs={"class","yr-table yr-table-longterm yr-popup-area"})
    nw_w_tds=nw_w_tab.find_all("td")

    nw_w_tlist, nw_w_rlist, nw_w_wlist, nw_w_dlist=[],[],[],[]
    for td in nw_w_tds:
        if td["title"].find("Temperature")!=-1:
            nw_w_temp=td.get_text()[:-1]
            nw_w_tlist.append(nw_w_temp)
        elif td["title"].find("Precipitation")!=-1:
            a=td["title"].split(":")[1]
            nw_w_rainfall=a.split("mm")[0][1:-1]
            nw_w_rlist.append(nw_w_rainfall)
        elif td["title"].find("m/s")!=-1:
            a=td["title"].split("m/s")[0]
            nw_w_wind=a.split(",")[1][1:-1]
            nw_w_wlist.append(nw_w_wind)
        else:
            nw_w_draw=td["title"][:-2]
            nw_w_dlist.append(nw_w_draw)
        
    nw_w_tlist=nw_w_tlist[2:7]
    nw_w_rlist=nw_w_rlist[2:7]
    nw_w_wlist=nw_w_wlist[2:7]
    nw_w_dlist=nw_w_dlist[2:7]

    def n_weeklyDB(loc,date,i): #d1-0,d2-1,d3-2,d4-3,d5-4
        # connection=cx_Oracle.connect('scott','tigertiger','orcl.cyemppkgt3jv.ap-northeast-2.rds.amazonaws.com:1521/orcl')
        connection=cx_Oracle.connect('scott','tiger','192.168.0.69:1521/orcl')
        cur=connection.cursor()

        sql="insert into SM_WWH_TB(WWH_NO, WWH_LOC, WWH_DATE, WWH_FORECAST, WWH_TEMP, WWH_PREC, WWH_WIND, WWH_TYPE) values(SM_WWH_SEQ.NEXTVAL, :WWH_LOC, :WWH_DATE, :WWH_FORECAST, :WWH_TEMP, :WWH_PREC, :WWH_WIND, :WWH_TYPE)"
        cur.execute(sql,[loc,date,nw_w_dlist[i],nw_w_tlist[i],nw_w_rlist[i],nw_w_wlist[i],2])

        connection.commit()
        connection.close()

    n_weeklyDB(num,d1,0)
    n_weeklyDB(num,d2,1)
    n_weeklyDB(num,d3,2)
    n_weeklyDB(num,d4,3)
    n_weeklyDB(num,d5,4)

nw_weekly("https://www.yr.no/place/South_Korea/Seoul/Seoul/long.html?spr=eng",1) #서울
nw_weekly("https://www.yr.no/place/South_Korea/Gangwon/Gangneung-si/long.html?spr=eng",2) #강릉
nw_weekly("https://www.yr.no/place/South_Korea/Daejeon/Daejeon/long.html?spr=eng",3) #대전
nw_weekly("https://www.yr.no/place/South_Korea/Gwangju/Gwangju/long.html?spr=eng",4) #광주
nw_weekly("https://www.yr.no/place/South_Korea/Ulsan/Ulsan/long.html?spr=eng",5) #울산



