import numpy as np
import pandas as pd
import cx_Oracle as co 


#DAO(Data Access Object) : DeptDAO
class DeptDAO(object):
    def __init__(self):
        self.dsnString = co.makedsn("192.168.0.68","1521",service_name="orcl")
        self.user = 'scott'
        self.password = 'tiger'
    #조회하는 기능
    def query_all(self):
        sql = 'select * from dept'
        conn = co.connect(user=self.user , password =self.password, dsn = self.dsnString)
        print(conn)
        query_result = pd.read_sql(sql,conn)
        conn.close()
        return query_result 
    def insertOne(self,data):
        sql = 'insert into dept values (:1,:2,:3)'
        conn = co.connect(user=self.user , password =self.password, dsn = self.dsnString)
        cursor = conn.cursor()
        cursor.execute(sql,data)
        conn.commit()
        conn.close()
    
    def updateDept(self ,data):
        sql = 'update dept set dname = :1 , loc= :2 where deptno =:3'
        conn = co.connect(user=self.user , password =self.password, dsn = self.dsnString)
        cursor = conn.cursor()
        cursor.execute(sql,data)
        conn.commit()
        conn.close()
        
    def deleteDept(self,data):
        sql = 'delete dept where deptno = :1 '
        conn = co.connect(user=self.user , password =self.password, dsn = self.dsnString)
        cursor = conn.cursor()
        cursor.execute(sql,data)
        conn.commit()
        conn.close()
        