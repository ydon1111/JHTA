#기상청 주간

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

kw_w_url="http://www.weather.go.kr/weather/forecast/mid-term_01.jsp"

kw_w_res=requests.get(kw_w_url)
kw_w_res.raise_for_status()

kw_w_soup=bs(kw_w_res.text,'lxml')

def draw_prob():
    kw_w_drawlist=[]
    kw_w_problist=[]
    for t in kw_w_tr:
        ul=t.find('ul')
        if ul != None and ul != -1:
            # print(ul)
            # print(ul.contents[1],ul.contents[5])
            kw_w_draw=ul.contents[1]['title']
            kw_w_drawlist.append(kw_w_draw)

            kw_w_prbo=ul.contents[5].get_text()[:-1]
            kw_w_problist.append(kw_w_prbo)

    kw_w_drawlist=kw_w_drawlist[:-3]
    kw_w_drawlist=kw_w_drawlist[1::2]

    kw_w_problist=kw_w_problist[:-3]
    kw_w_problist=kw_w_problist[1::2]

    return kw_w_drawlist, kw_w_problist

def temp():
    kw_w_tlist=[]
    for t in kw_w_tr:
        ul=t.find('ul')
        if ul != None and ul != -1:
            # print(ul)
            li=ul.contents[1]
            low=li.contents[0].get_text()
            high=li.contents[2].get_text()
            kw_w_temp=low+" / "+high
            kw_w_tlist.append(kw_w_temp)
    kw_w_tlist=kw_w_tlist[:-3]
    return kw_w_tlist

def weeklyDB(loc,dlist,tlist,plist,date,i): #d1-0,d2-1,d3-2,d4-3,d5-4
    # connection=cx_Oracle.connect('scott','tigertiger','orcl.cyemppkgt3jv.ap-northeast-2.rds.amazonaws.com:1521/orcl')
    connection=cx_Oracle.connect('scott','tiger','192.168.0.69:1521/orcl')
    cur=connection.cursor()

    sql="insert into SM_WWH_TB(WWH_NO, WWH_LOC, WWH_DATE, WWH_FORECAST, WWH_TEMP, WWH_PREC_PROB, WWH_TYPE) values(SM_WWH_SEQ.NEXTVAL, :WWH_LOC, :WWH_DATE, :WWH_FORECAST, :WWH_TEMP, :WWH_PREC_PROB, :WWH_TYPE)"
    cur.execute(sql,[loc,date,dlist[i],tlist[i],plist[i],1])

    connection.commit()
    connection.close()

kw_w_tables=kw_w_soup.find_all("table",attrs={"class","table_midterm"})

dlist1,dlist2,dlist3,dlist4,dlist5,plist1,plist2,plist3,plist4,plist5,tlist1,tlist2,tlist3,tlist4,tlist5=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
cnt=1
for table in kw_w_tables:
    if cnt==1:
        kw_w_tr=table.tbody.tr
        dlist1,plist1=draw_prob() #1.서울

        kw_w_tr=kw_w_tr.next_sibling.next_sibling
        kw_w_tr=kw_w_tr.next_sibling.next_sibling
        dlist2,plist2=draw_prob() #2.강릉

        kw_w_tr=kw_w_tr.next_sibling.next_sibling
        dlist3,plist3=draw_prob() #3.대전

        kw_w_tr=kw_w_tr.next_sibling.next_sibling
        kw_w_tr=kw_w_tr.next_sibling.next_sibling
        dlist4,plist4=draw_prob() #4.광주

        kw_w_tr=kw_w_tr.next_sibling.next_sibling
        kw_w_tr=kw_w_tr.next_sibling.next_sibling
        dlist5,plist5=draw_prob() #5.울산

    elif cnt==2:
        kw_w_tr=table.tbody.tr
        tlist1=temp() #1.서울
        
        for i in range(8):
            kw_w_tr=kw_w_tr.next_sibling.next_sibling
        tlist2=temp() #2.강릉

        kw_w_tr=kw_w_tr.next_sibling.next_sibling
        tlist3=temp() #3.대전

        for i in range(6):
            kw_w_tr=kw_w_tr.next_sibling.next_sibling
        tlist4=temp() #4.광주

        for i in range(13):
            kw_w_tr=kw_w_tr.next_sibling.next_sibling
        tlist5=temp() #5.울산
    cnt+=1
    
weeklyDB(1,dlist1,tlist1,plist1,d1,0)
weeklyDB(1,dlist1,tlist1,plist1,d2,1)
weeklyDB(1,dlist1,tlist1,plist1,d3,2)
weeklyDB(1,dlist1,tlist1,plist1,d4,3)
weeklyDB(1,dlist1,tlist1,plist1,d5,4)
    
weeklyDB(2,dlist2,tlist2,plist2,d1,0)
weeklyDB(2,dlist2,tlist2,plist2,d2,1)
weeklyDB(2,dlist2,tlist2,plist2,d3,2)
weeklyDB(2,dlist2,tlist2,plist2,d4,3)
weeklyDB(2,dlist2,tlist2,plist2,d5,4)
    
weeklyDB(3,dlist3,tlist3,plist3,d1,0)
weeklyDB(3,dlist3,tlist3,plist3,d2,1)
weeklyDB(3,dlist3,tlist3,plist3,d3,2)
weeklyDB(3,dlist3,tlist3,plist3,d4,3)
weeklyDB(3,dlist3,tlist3,plist3,d5,4)
    
weeklyDB(4,dlist4,tlist4,plist4,d1,0)
weeklyDB(4,dlist4,tlist4,plist4,d2,1)
weeklyDB(4,dlist4,tlist4,plist4,d3,2)
weeklyDB(4,dlist4,tlist4,plist4,d4,3)
weeklyDB(4,dlist4,tlist4,plist4,d5,4)
    
weeklyDB(5,dlist5,tlist5,plist5,d1,0)
weeklyDB(5,dlist5,tlist5,plist5,d2,1)
weeklyDB(5,dlist5,tlist5,plist5,d3,2)
weeklyDB(5,dlist5,tlist5,plist5,d4,3)
weeklyDB(5,dlist5,tlist5,plist5,d5,4)




