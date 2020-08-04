import cx_Oracle

connection = cx_Oracle.connect("scott","tigertiger","orcl.c6qnbgjpp2wo.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)

cur = connection.cursor()

sql = """
select empno,ename,job,deptno
from emp
where deptno = :txt
"""

cur.execute(sql,txt=10)
print(cur)

for empno,ename,job,deptno in cur:
    print('{} \t {} \t {} \t {}'.format(empno,ename,job,deptno))

