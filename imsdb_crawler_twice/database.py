import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    port=3306,
    db='imsdb',
)

cursor = db.cursor()
create_table = 'CREATE TABLE IF NOT EXISTS stu(id INTEGER PRIMARY KEY ,name TEXT,age INTEGER )'
# cursor.execute(create_table)
insert_sql = "INSERT INTO stu(id,name,age)VALUE (3,'zhangsan',22)"
cursor.execute(insert_sql)
update_sql = "UPDATE stu SET age=50 WHERE id = 2"
cursor.execute(update_sql)
select_sql = "SELECT * FROM stu"
res = cursor.execute(select_sql)
# fetchall() 查询所有数据
res = cursor.fetchall()
print(res)
db.commit()
cursor.close()
db.close()