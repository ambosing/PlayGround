import pymysql

conn = pymysql.connect(host="localhost", user="root", password="root", db="pythonDB", charset="utf8")
cur = conn.cursor()

sql = "CREATE Table userTable (id char(4), userName char(10))"
cur.execute(sql)

conn.commit()
conn.close()
