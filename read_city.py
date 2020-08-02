import pymysql

#获取城市code
def read_database():
    city_code_arr = []
    db = pymysql.connect("localhost", "root", "123456", "movie")
    cursor = db.cursor()
    sql = "SELECT * FROM city"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        city_code = row[0]
        city_code_arr.append(city_code)
    db.close()
    return city_code_arr

# 获取城市
def get_city(city_code):
    db = pymysql.connect("localhost", "root", "123456", "movie")
    cursor = db.cursor()
    sql = "SELECT city FROM city  WHERE city_code = '%s'" %(city_code)
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    city =''
    for row in results:
       city = row[0]
    db.close()
    return city

# 删除表中数据
def delete_table():
    db = pymysql.connect("localhost", "root", "123456", "movie")
    cursor = db.cursor()
    sql ="truncate table weather"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()

