import cx_Oracle
#1. connection  객체 생성
connection = cx_Oracle.connect("scott","tigertiger","orcl.c6qnbgjpp2wo.ap-northeast-2.rds.amazonaws.com:1521/orcl")

print(connection)

#2. cursor 객체

cur = connection.cursor()

#3. 사용할 sql문 객
sql = """
SELECT empno , ename,sal 
FROM emp 
WHERE ename = :txt   
"""

#4. 실행
# #  :  <== 바인드변수  매개변수 입력 
cur.execute(sql,txt="SCOTT")
print(cur)

#5. 로직처리 

for empno,ename, sal  in cur:
    print('{} \t {} \t {}'.format(empno,ename,sal))

#6. 자원반납 
connection.close()



