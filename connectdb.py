import mysql.connector
from flask import g


#   链接数据库
def connect_db():
    g.db = mysql.connector.connect(user='root', password='mysqlove', database='edu')


#   断开数据库链接
def disconnect_db():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()
