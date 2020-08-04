import cx_Oracle

#1. connection  객체 생성
#2. cursor 객체
#3. 사용할 sql문 객
#  :  <== 바인드변수  매개변수 입력 
#4. 실행
#5. 로직처리 
#6. 자원반납 

connection = cx_Oracle.connect("scott","tigertiger","orcl.c6qnbgjpp2wo.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)
cur = connection.cursor()

sql="""
    INSERT INTO dept VALUES (:deptno,:dname,:loc)
"""
sql2="""
    INSERT INTO dept (deptno,loc) VALUES (:deptno,:loc)
"""



cur.execute(sql,[1,"SALESMAN","SEOUL"])
cur.execute(sql,[2,None,"BUSAN"])
cur.execute(sql2,[3,"INCHEON"])


connection.commit()
connection.close()