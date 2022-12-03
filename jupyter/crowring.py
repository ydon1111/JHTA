from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests
from pathlib import Path
import pandas as pd 
import numpy as np 


# headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
addr =[]
name =[]
loc =[]
tel = []
for r in range(1,123):
    url = "http://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page="+str(r)
    res = requests.get(url)        #응답 값 확인
    res.raise_for_status() 
    # print(res.text)


    bs(res.text,'lxml') #값정리 
    soup  = bs(res.text,'lxml')
    date_name = soup.findAll('td',attrs = {"class","td_date"})
    date_addr = soup.findAll('td',attrs = {"class","td_subject"})
    
    for z in date_addr:
        addr.append(z.text)

    for i,v in enumerate(date_name):
        if (i-1)%4 == 0 :
            name.append(v.text)
        elif i%4 ==0:
            loc.append(v.text)
        elif (i-2)%4 ==0:
            tel.append(v.text)
print(addr,name,loc,tel)
  

df = pd.DataFrame([name,addr,loc,tel])

df2 =df.T
print(df2)
df2.to_csv('cheogajip.csv',encoding='euc-kr')

