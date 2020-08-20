from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import urllib.parse
import cx_Oracle


r_plusurl = urllib.parse.quote_plus(input("검색어를 입력하세요 : "))  #날씨 값 받아서 블로그에 검색 할 예정 // 조건을 아직 안붙임(날씨별로 변경)

r_url = f"https://search.naver.com/search.naver?where=post&sm=tab_jum&query={r_plusurl}" #네이버 포스터 url
r_res = requests.get(r_url)
r_res.raise_for_status()
# print(res.text)
r_soup = bs(r_res.text,"lxml")
# pprint(r_soup)
r_As = r_soup.find_all("a",attrs={"class","sh_blog_title _sp_each_url _sp_each_title"})       #a태그에서 블로그 url 및 title 찾음 
# pprint(r_As)

for a in r_As:
    r_href = a['href']       #검색 포스터 url
    r_title = a['title']     #검색 포스터 타이틀        
    print(r_title)
    print(r_href) 
    connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
    print(connection) 
    cur = connection.cursor()
    sql = """
       
       INSERT INTO SM_RCD_TB (SM_RCD_TB.RCD_NO, SM_RCD_TB.RCD_TITLE,SM_RCD_TB.RCD_URL) VALUES (SM_RCD_SEQ.NEXTVAL, :title,:href)
    """

    cur.execute(sql,[r_title,r_href])


    connection.commit()
    connection.close()