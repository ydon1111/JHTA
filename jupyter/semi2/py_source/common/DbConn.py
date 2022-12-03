#-*- coding:utf-8 -*-
import cx_Oracle
import os 

os.environ["NLS_LANG"] = ".AL32UTF8"
#""" 
# 민수 DB
# orcl.czq0cxsnbcns.ap-northeast-2.rds.amazonaws.com, orcl, scott, tigertiger, 1521
# """ 

class DbConn:
    def __init__(
        self, 
        host = "localhost", 
        dbname = "orcl", 
        user = "scott", 
        password = "tiger", 
        port = "1521"
        ):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.connection = cx_Oracle.connect(self.user, self.password, self.host+":"+self.port+"/"+self.dbname)

    def execute(self, sql, args=None):
        cur = self.connection.cursor()
        if args == None:
            res = cur.execute(sql)
        else:
            res = cur.execute(sql, args)
            
        if res == None:
            self.connection.commit()  
        else:
            resultList = cur.fetchall()
            return resultList
            
    
    def disconnect(self):
        self.connection.close()