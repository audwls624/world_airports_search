import pymysql

conn = pymysql.connect(host='10.211.55.4',
        user='root',
        password='adsf25did',
        db='airport',
        charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql1 = '''CREATE TABLE regions (name varchar(50) NOT NULL PRIMARY KEY)'''
        sql2 = '''CREATE TABLE countries (korean_name varchar(200) NOT NULL PRIMARY KEY, english_name varchar(200) NOT NULL, region varchar(50) REFERENCES regions (name))'''
        sql3 = '''CREATE TABLE airports (korean_name varchar(200) NOT NULL, english_name varchar(200) NOT NULL, 
        iata_code varchar(10) NOT NULL PRIMARY KEY, icao_code varchar(10) NOT NULL, country_korean varchar(200) NOT NULL REFERENCES countries (korean_name) , city_english varchar(200) NOT NULL)'''
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
    conn.commit()
finally:
    conn.close()