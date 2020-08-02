import pymysql

db = pymysql.connect("localhost", "root", "123456", "movie")
cursor = db.cursor()
sql = "INSERT INTO city(city_code, city) \
       VALUES ('%s', '%s')" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
#title,director,country, year, type,grade
sql_createTb = """CREATE TABLE weather (
                 date CHAR(255),
                 weather  CHAR(255),
                 temperature_highest CHAR(255),
                 temperature_lowest CHAR(255),
                 city CHAR(255),
                 city_code CHAR(255),
                 week CHAR(255))
                 """

sql_city = """CREATE TABLE city (
                 city_code CHAR(255),
                 city CHAR(255))
                 """
try:
    # 执行sql语句
    cursor.execute(sql_city)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()

