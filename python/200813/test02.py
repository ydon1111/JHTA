import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

# pip install bs4
url ="https://comic.naver.com/webtoon/list.nhn?titleId=20853"

res = requests.get(url)

res.raise_for_status()
res.close()
# pprint(res.text) #소스코드를 다가져옴 \b\t 등많음

soup = bs(res.text,'lxml')  #lxml을 통해 간결하게 가져옴 
# print(soup)
# print('type :' ,type(soup))

# pip install lxml

print(soup.title)     #타이틀을 가져옴
print(soup.title.get_text())  #타이틀안의 내용을 가져옴 

print("------------------------")
print(soup.find("a")) #soup 객체에서 처음 발견되는 a element출력
print("------------------------")
print(soup.a.attrs)  # a tag 의 속성들 출력
print("------------------------")
print(soup.a.attrs['href'])

print("------------------------")
#함수를 이용한 접근 방법
print(soup.find("td",attrs={"class","title"}))
title1 = soup.find("td",attrs={"class","title"})
print("------------------------")
a = title1.find("a")
print(a.get_text())