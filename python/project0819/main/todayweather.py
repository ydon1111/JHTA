import cx_Oracle
from youtube_search import YoutubeSearch
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import urllib.parse



#----------------------db에서 현재 날씨 번호, 현재 날씨 가져오기 -----------------------------------------
connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
print(connection) 
cur = connection.cursor()
sql = """

SELECT
TNWH_NO,TNWH_FORECAST,TNWH_TIME,TNWH_DATE
FROM
SM_TNWH_TB
WHERE
str(time.localtime().tm_hour) 
between
SUBSTR(TNWH_TIME,1,2) =< :txt 
and 
SUBSTR(TNWH_TIME,7,2) >  :txt2

and
SUBSTR(TNWH_DATE,9,2) = :txt3

"""

cur.execute(sql,txt=18, txt2=24 ,txt3=str(time.localtime().tm_day))  #txt = 시간 앞 , txt2 = 시간 뒤 , txt3 = 날짜
print(cur)

for TNWH_NO,TNWH_FORECAST,TNWH_TIME,TNWH_DATE in cur:
    # print("{}\t {} \t {}\t {}  ".format(TNWH_NO,TNWH_FORECAST,TNWH_TIME,TNWH_DATE))
    forecast = TNWH_FORECAST
    weathrtNo = TNWH_NO

connection.commit()
connection.close()


#----------------------------------현재 날씨번호와 현재날씨를 기준으로 크롤링 하여 db에 저장------------------------
#----------------------------------블로그 크롤링 , 음악 , 영상 3개를 따로 크롤링해야함????

#TNWH_FORECAST를 기준으로 검색 시작 
weatherList = ['구름많음','흐리고 비','맑음','흐림','비','구름조금']
#검색값을 설정해야함.
#날씨 값을 변경하여 검색자료가 정확하게 나오게 해야함 

#예)'흐리고 비' 날 추천요리 (x) 흐리고 비 --> '비오는' 으로 변경 
# 비오는 날 추천 요리로 검색 가능하게 해야함 

w = forecast
if w == '흐리고 비' or '비' or '소나기':
    r = '비오는' 
elif w== '구름많음' or '흐림' or'구름조금':
    r = '흐린'
elif w== '맑음':
    r = '날씨 좋은'

# 추천요리
r_results = YoutubeSearch(r+"날 추천 요리", max_results=10).to_dict() #
for i in r_results:
    r_url = i['url_suffix'] 
    r_title = i['title']    
    r_thumbnails = i['thumbnails'] 
    r_href = 'https://www.youtube.com/'+r_url  
    r_video = "https://www.youtube.com/embed/"+r_url.split("v=")[-1]+"?autoplay=0"
    r_music = "https://music.youtube.com/"+r_url
 
    connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
    print(connection) 
    cur = connection.cursor()
    sql = """
        INSERT INTO SM_RCD_TB (SM_RCD_TB.RCD_NO, SM_RCD_TB.RCD_TITLE,SM_RCD_TB.RCD_URL,RCD_TNWH_NO,RCD_TYPE) VALUES (SM_RCD_SEQ.NEXTVAL, :title,:href,:wNo,3)
    """

    cur.execute(sql,[r_title, r_video, weathrtNo])
    connection.commit()

# 추천노래 
r_results = YoutubeSearch(r+"날 추천 노래", max_results=10).to_dict() #
for i in r_results:
    r_url = i['url_suffix'] 
    r_title = i['title']    
    r_thumbnails = i['thumbnails'] 
    r_href = 'https://www.youtube.com/'+r_url  
    r_video = "https://www.youtube.com/embed/"+r_url.split("v=")[-1]+"?autoplay=0"
    r_music = "https://music.youtube.com/"+r_url
 
    connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
    print(connection) 
    cur = connection.cursor()
    sql = """
        INSERT INTO SM_RCD_TB (SM_RCD_TB.RCD_NO, SM_RCD_TB.RCD_TITLE,SM_RCD_TB.RCD_URL,RCD_TNWH_NO,RCD_TYPE) VALUES (SM_RCD_SEQ.NEXTVAL, :title,:href,:wNo,1)
    """

    cur.execute(sql,[r_title, r_music, weathrtNo])
    connection.commit()


# 추천여행지
r_plusurl = urllib.parse.quote_plus(r+"날 추천여행지")
r_url = f"https://search.naver.com/search.naver?where=post&sm=tab_jum&query={r_plusurl}" 
r_res = requests.get(r_url)
r_res.raise_for_status()
r_soup = bs(r_res.text,"lxml")
r_As = r_soup.find_all("a",attrs={"class","sh_blog_title _sp_each_url _sp_each_title"})      

for a in r_As:
    r_href = a['href']       
    r_title = a['title']           
    print(r_title)
    print(r_href) 
    connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
    print(connection) 
    cur = connection.cursor()
    sql = """
       
       INSERT INTO SM_RCD_TB (SM_RCD_TB.RCD_NO, SM_RCD_TB.RCD_TITLE,SM_RCD_TB.RCD_URL,RCD_TNWH_NO,RCD_TYPE) VALUES (SM_RCD_SEQ.NEXTVAL, :title,:href,:wNo,2)
    """

    cur.execute(sql,[r_title,r_href,weathrtNo])


    connection.commit()
    connection.close()





connection.close()



#1. DB에서 스케쥴러 기준 시간과 날짜를 쿼리문에 대입하여 
#   날씨 고유번호, 현재날씨 를 가져온다 . 
'''
스캐줄러에서 시간을 불러올 수 있는지 확인
시간, 날짜 
스캐줄러와 연결 시켜야함
'''

#2. 날씨 고유번호와 함께 
#   현재날씨를 통해 유튜브자료크롤링하여 DB에 입력
'''
가져온 자료를 뽑아내서 입력하고 ,다시 넣는 작업을 해야함 
(날씨를 가져와서 유튜브에서 크롤링하여 다시 날씨고유번호와 함께 url
넣어야함)
'''

#3. 입력한 자료를 불러와서 화면에 출력 
 


#아니면 

'''
db에 유튜브 자료를 미리 넣어둠 , 넣을 때 날씨를 기준으로 정리해서 넣어둠 
넣어둔 자료를 실시간자료와 조인해서 자료를 가져옴 
'''