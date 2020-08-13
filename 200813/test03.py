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

# print('type :' ,type(soup))
tdList = soup.find_all("td",attrs={"class","title"})
print(tdList,type(tdList))
# print(tdList[0].find("a").get_text())

for td in tdList:
    print(td.find("a").get_text())

