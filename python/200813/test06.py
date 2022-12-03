import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

# input에 한국어로 검색하면 이것을 컴퓨터 언어로 변환해줌
plusurl = urllib.parse.quote_plus(input("검색어를 입력하세요 : "))
 
# 페이지를 넘겨가면서 카운트 하기 위해 최초값을 1로 설정함.
page_num = 1
count = 1

i = input("몇 페이지까지를 크롤링 할까요? : ")

# 크롤링 범위를 제한하기 위해 lastpage를 정해줌.
lastpage = int(i) * 10 - 9

while page_num < lastpage + 1:
    url = f"https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=%{plusurl}&sm=tab_pge&srchby=all&st=sim&where=post&start={page_num}"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # find, select_one은 고른 태그의 최초값을 가져옴.
    # find_all, select는 고른 태그의 모든값을 리스트로 가져옴. 단 한개여도 리스트로.
    # find, find_all은 하위 태그를 지정할 때 ﻿find('div').find('a').find('img') 이렇게 해야하고
    # select_one("div a img")를 하면 됨. 다만 태그값에 " "가 있을 때 select는 하위값으로 인식하기 때문에 사용 못함.
    title = soup.find_all(class_='sh_blog_title')

    print(f"{count}페이지 결과입니다.")
    # attrs는 태그의 title, id 속성값을 찾아줌. 속성값을 가져오는 게 아니라 출력함.
    for i in title:
        print(i.attrs['title'])
        print(i.attrs['href'])
    print()

    page_num += 10
    count += 1
