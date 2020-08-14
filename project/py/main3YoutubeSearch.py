from youtube_search import YoutubeSearch
import cx_Oracle
#pip install youtube-search


r_songname = input("노래제목을 입력하세요 : ")  #유튜브 검색 입력 // 나중에 현재날씨 를 불러와서 검색 // 조건을 아직 안붙임(날씨별로 변경)
r_results = YoutubeSearch(r_songname, max_results=10).to_dict() #유튜브 검색을 딕셔너리로 뽑음 
for i in r_results:
    r_url = i['url_suffix'] #url 주소를 뽑음 
    r_title = i['title']    #title을 뽑음 
    r_href = 'https://www.youtube.com/'+r_url
    print(r_title)
    print(r_href)
    
    connection = cx_Oracle.connect("scott","tigertiger","orcl.c6qnbgjpp2wo.ap-northeast-2.rds.amazonaws.com:1521/orcl")
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