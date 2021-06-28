import pymysql
from pymysql.cursors import DictCursor
class MysqlHandler:
    def __init__(self,host=None,user=None,password=None,port=3306,charset='utf8',cursorclass=DictCursor):
        self.conn=pymysql.connect(host=host,user=user,password=password,port=port,charset='utf8',cursorclass=DictCursor)
        self.cursor = self.conn.cursor()  # 实例化游标
    def query(self,sql,one=True):
        self.cursor.execute(sql)
        if one:
            return self.cursor.fetchone()
        return self.cursor.fetchall()
    def mysql_close(self):
        self.conn.close()
        self.cursor.close()
