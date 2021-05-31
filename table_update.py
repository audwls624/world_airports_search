import pymysql

conn = pymysql.connect(host='localhost',
        user='root',
        password='adsf25did',
        db='airports',
        charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql1 = '''CREATE TABLE continents (ID int NOT NULL auto_increment, korean_name varchar(50), english_name varchar(50), PRIMARY KEY (ID))'''
        sql2 = '''CREATE TABLE countries (ID int NOT NULL auto_increment, korean_name varchar(200), english_name varchar(200), continent_id int NOT NULL, PRIMARY KEY (ID), FOREIGN KEY (continent_id) REFERENCES continents (ID))'''
        sql3 = '''CREATE TABLE cities (ID int NOT NULL auto_increment, korean_name varchar(200), english_name varchar(200), country_id int, PRIMARY KEY (ID), FOREIGN KEY (country_id) REFERENCES countries (ID))'''
        sql4 = '''CREATE TABLE airports (ID int NOT NULL auto_increment, korean_name varchar(200), english_name varchar(200), iata_code varchar(10) NOT NULL, icao_code varchar(10) NOT NULL, city_id int NOT NULL, PRIMARY KEY (ID), FOREIGN KEY(city_id) REFERENCES cities(ID))'''
        sql5 = '''CREATE TABLE nicknames (ID int NOT NULL auto_increment, name varchar(100), airport_id int NOT NULL, PRIMARY KEY (ID), FOREIGN KEY(airport_id) REFERENCES airports(ID))'''
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        cursor.execute(sql5)
    conn.commit()
finally:
    conn.close()