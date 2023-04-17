"""
author: 王璐斯
file: pysql.py
time: 2022/10/10 9:22
"""
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='123456', database='jiajun', port=3306)
# 获取游标
cursor = conn.cursor()
# 执行sql语句
# sql = 'select user from stu'
# sql = 'insert into stu(user) value ("小马")'
sql = 'update stu set user = "郑雪利" where id = 7'
s = 'select * from stu'
# 插入语句
cursor.execute(sql)
cursor.execute(s)

# print(cursor.fetchone())
# conn.close()
# 数据查询
# sql = """select * from ss;"""

# cursor.fetchmany(1)
print(cursor.fetchall())


