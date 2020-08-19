from youtube_search import YoutubeSearch
import cx_Oracle
#pip install youtube-search


#데이터 인풋할때 주의*****
#오늘 날씨를 찾아와서 
#날씨 값 입력 
weatherList = ['구름많음','흐리고 비','맑음','흐림']

# select 
#     tnwh_no,tnwh_forecast,tnwh_time
# from
#     sm_tnwh_Tb
# where
#     SUBSTR('tnwh_time',1,2) = 18;

for w in weatherList:
    if w == "구름많음":
        w = "흐림"
    print(w)

w = "비오는날"


# r_songname = input("노래제목을 입력하세요 : ")  #유튜브 검색 입력 // 나중에 현재날씨 를 불러와서 검색 // 조건을 아직 안붙임(날씨별로 변경)
r_results = YoutubeSearch(w+"날 추천 요리", max_results=10).to_dict() #유튜브 검색을 딕셔너리로 뽑음 
# print(r_results)

for i in r_results:
    r_url = i['url_suffix'] #url 주소를 뽑음 
    r_title = i['title']    #title을 뽑음 
    r_thumbnails = i['thumbnails'] #thumbnails 뽑음
    r_href = 'https://www.youtube.com/'+r_url  #유튜브 url 그대로 가져옴 , 댓글이랑 다른게 다뜸
    print(r_title)
    # print(r_href)
    print(r_thumbnails[-1])
    print("https://www.youtube.com/embed/"+r_url.split("v=")[-1]+"?autoplay=0")  #embed 해서 가져오려하니 음악영상은 재생이 안됨 
    # print("https://music.youtube.com/"+r_url)  #유튜브 뮤직을 통해서 주소를 가져옴 / 음악영상이 아니면 재생이 안됨 
    
    connection = cx_Oracle.connect("scott","tiger","192.168.0.69:1521/orcl")
    print(connection) 
    cur = connection.cursor()
    sql = """
        INSERT INTO SM_RCD_TB (SM_RCD_TB.RCD_NO, SM_RCD_TB.RCD_TITLE,SM_RCD_TB.RCD_URL) VALUES (SM_RCD_SEQ.NEXTVAL, :title,:href)
    """

    cur.execute(sql,[r_title,r_href])


    connection.commit()
    connection.close()
    
    

#   해야할것 08/14
#   날씨 데이터를 받음 , 데이터를 4등분함 맑음 / 흐림 / 비 / 눈 
#   위에 테마에 맞는 검색을 실행 
#   ui에 나타냄
