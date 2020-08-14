from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8"

res = requests.get(url)

# print(res)

res.raise_for_status()
# print(res.text,len(res.text))

soup = bs(res.text,"lxml")

# pprint(soup)
dds = soup.find_all("dd",attrs={"class",'lv1'})
# pprint(dds)

for d in dds:
    # print(d)
    num = d.find("span",attrs={"class","num"})
    print(num.get_text())
    print("-----------------------")


temp = soup.find("span",attrs={"class",'todaytemp'}) # span 의 하부 클래스와 클래스명 설정 
# pprint(temp)
print(temp.get_text())
print("-------------------------------")

rainfall = soup.find("span",attrs={'class','rainfall'})
# pprint(rainfall)
num2 = rainfall.find("span",attrs={"class","num"})
# print(num2)
print(num2.get_text())

# 정의 목록 만들기
#<d1>  정의목록(definition List)
# <dt> 용어 제목</dt> (definition term)
#<dd>용어 설명</dd> (definition description)