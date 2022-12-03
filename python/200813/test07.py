from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path

url = "https://movie.naver.com/movie/running/current.nhn"

res = requests.get(url)

res.raise_for_status()
# print(res.text)

soup = bs(res.text,"lxml")

# pprint(soup)
divs = soup.find_all("div",attrs={"class","thumb"})
# pprint(divs)

idx=0
for div in divs:
    # pprint(div)
    # print("-------------------------------")
    aTag = div.find("a")
    # pprint(aTag['href'].split("=")[1])
    # print("----------------------")
    movieCode = aTag['href'].split("=")[1]
    url2 ="https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode="+movieCode
    # print(url2)
    res2 = requests.get(url2)
    # pprint(res2)
    soup2 = bs(res2.text,"lxml")
    img = soup2.find("img")
    # print(img['src'])
    imgpath = img['src']
    res3 = requests.get(imgpath)

    Path("./img/movie_poster").mkdir(parents = True , exist_ok = True)
    idx +=1 
    with open("./img/movie_poster/movie{}.jpg".format(idx),'wb') as f:
        f.write(res3.content)