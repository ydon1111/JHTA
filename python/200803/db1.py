
import cx_Oracle   #오라클 접속 

# orcl.c6qnbgjpp2wo.ap-northeast-2.rds.amazonaws.com
# print(cx_Oracle.init_oracle_client())


# connection = cx_Oracle.connet("id","pw","서버id:1521(port번호)/db명")
#오라클 설치 안되어있으면 클라이언트 파일 설치 해야함, 밑에 오류주소로 들어가서 다운로드 
#https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
#Oracle Instant Client Zip Files


connection = cx_Oracle.connect("scott","tigertiger","orcl.c6qnbgjpp2wo.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection) #로그인

cur = connection.cursor()  #커리문 사용할꺼다 저장메모리만듬

query = "select * from dept" #조건문은 이거다 

cur.execute(query) #조건문을 커리함 저장메모리에 담음

for x in cur:         #커리한거 출력
    print(x)

connection.close()       #접속을 끊지 않으면 계속 실행되고 있어서 자원을 소비함 




