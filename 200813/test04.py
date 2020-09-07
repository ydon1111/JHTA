from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests
from pathlib import Path


headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
url = "https://comic.naver.com/webtoon/detail.nhn?titleId=20853&no=1237&weekday=tue"
res = requests.get(url)        #응답 값 확인
res.raise_for_status()         #응답하면 실행 응답안하면 실행 안함 
# pprint(res.text)

bs(res.text,'lxml') #값정리 
soup  = bs(res.text,'lxml')
# pprint(soup)

data = soup.find('div',attrs = {"class","wt_viewer"}) #값에서 div에서 class, wt_viewr 항목 찾음 라이브러리 로 나옴  
# print(data)

images = data.findAll("img") #라이브러리에서 img 찾음
# pprint(images)

# 찾음 라이브러리를 하나씩 꺼냄 
for img in images:
    pprint(img['src'])   #그중 src 항목만 뽑음 
    path = img['src']
    # print(path[46:50])
    res2 = requests.get(path, headers =headers)  #프로그램에서 직접 접근하면 권한을 안줌, 따라서 크롬으로 우회해서 접근 headers 변경 
    
    # print(res2)
    # 별도디렉토리를 만들고 그 장소에 이미지 파일을 저장 
    Path("./img/"+path[46:50]).mkdir(parents= True , exist_ok =True)
    with open("./img/"+path[46:50]+"/"+path[-12:],"wb") as f:
        f.write(res2.content)
