import cx_Oracle
from youtube_search import YoutubeSearch


#----------------------db에서 현재 날씨 번호, 현재 날씨 가져오기 -----------------------------------------
connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
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

for TNWH_NO,TNWH_FORECAST,TNWH_TIME,TNWH_DATE in cur:
    forecast = TNWH_FORECAST
    weathrtNo = TNWH_NO

connection.commit()
connection.close()

#TNWH_FORECAST를 기준으로 검색 시작 
weatherList = ['구름많음','흐리고 비','맑음','흐림','비','구름조금']

w = forecast
if w == '흐리고 비' or '비' or '소나기':
    r = '비오는' 
elif w== '구름많음' or '흐림' or'구름조금':
    r = '흐린'
elif w== '맑음':
    r = '날씨 좋은'

    
r_results = YoutubeSearch(r+"날 추천 요리", max_results=10).to_dict() #

for i in r_results:
    r_url = i['url_suffix'] 
    r_title = i['title']    
    r_thumbnails = i['thumbnails'] 
    r_href = 'https://www.youtube.com/'+r_url  
    r_video = "https://www.youtube.com/embed/"+r_url.split("v=")[-1]+"?autoplay=0"
    r_music = "https://music.youtube.com/"+r_url
 
    connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
    cur = connection.cursor()
    sql = """
        INSERT INTO SM_RCD_TB (SM_RCD_TB.RCD_NO, SM_RCD_TB.RCD_TITLE,SM_RCD_TB.RCD_URL,RCD_TNWH_NO) VALUES (SM_RCD_SEQ.NEXTVAL, :title,:href,:wNo)
    """

    cur.execute(sql,[r_title, r_video, weathrtNo])
    connection.commit()

connection.close()