from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests
from pathlib import Path
import pandas as pd 
import numpy as np 


# headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

name2 = []
addr = []
for r in range(1,113):
    url = "https://pelicana.co.kr/store/stroe_search.html?page=" +str(r)
    res = requests.get(url)        #응답 값 확인
    res.raise_for_status() 
    res.encoding = 'utf-8'
    # print(res.text)
    bs(res.text,'lxml') #값정리 
    soup  = bs(res.text,'html.parser')
    name = soup.findAll('a',attrs = {"class","btn_gray"})

    for i in range(10):
        aa = name[i].attrs['onclick'].split("'")
        # print(aa[5])
        name2.append(aa[5])
        addr.append(aa[9])

df = pd.DataFrame([name2,addr])
df2 =df.T
print(df2)
df2.to_csv('pr.csv',encoding='euc-kr')

