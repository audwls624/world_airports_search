import csv
# import os
# import sys
# import django
import pymysql

# os.chdir(".")
# print("Current dir=", end=""), print(os.getcwd())

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print("BASE_DIR=", end=""), print(BASE_DIR)

# sys.path.append(BASE_DIR)

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airport.settings")
# django.setup()

REGION_CSV_PATH='./regions.csv'
COUNTRY_CSV_PATH='./countries.csv'
AIRPORT_CSV_PATH='./airports.csv'


# conn = pymysql.connect(host='localhost',
#         user='root',
#         password='adsf25did',
#         db='airport',
#         charset='utf8mb4')

def region_uploader():
    with open(REGION_CSV_PATH, newline='', encoding='utf8') as csvfile:	
        data_reader = csv.DictReader(csvfile)
        conn = pymysql.connect(host='localhost',
        user='root',
        password='adsf25did',
        db='airports',
        charset='utf8mb4')
        for row in data_reader:
            with conn.cursor() as cursor:
                name = row['name']
                sql  = '''INSERT INTO continents (name) VALUES (%s)'''
                cursor.execute(sql,name)
        conn.commit()
        conn.close()
def country_uploader():
    with open(COUNTRY_CSV_PATH, newline='', encoding='utf8') as csvfile:	
        data_reader = csv.DictReader(csvfile)
        conn = pymysql.connect(host='localhost',
        user='root',
        password='adsf25did',
        db='airports',
        charset='utf8mb4')
        for row in data_reader:
            with conn.cursor() as cursor:
                region       = row['region']
                english_name = row['english_name']
                korean_name  = row['korean_name']
                sql  = '''INSERT INTO countries (region,english_name,korean_name) VALUES (%s,%s,%s)'''
                cursor.execute(sql,(region,english_name,korean_name))
        conn.commit()
        conn.close()
# def airport_uploader():
#     with open(AIRPORT_CSV_PATH, newline='', encoding='utf8') as csvfile:	
#         data_reader = csv.DictReader(csvfile)
#         conn = pymysql.connect(host='localhost',
#         user='root',
#         password='adsf25did',
#         db='airports',
#         charset='utf8mb4')
#         for row in data_reader:
#             with conn.cursor() as cursor:
#                 english_name   = row['english_name']
#                 korean_name    = row['korean_name']
#                 country_korean = row['country_korean']
#                 iata_code      = row['iata_code']
#                 icao_code      = row['icao_code']
#                 city_english   = row['city_english']
#                 sql  = '''INSERT INTO airports (english_name,korean_name,country_korean,iata_code,icao_code,city_english) VALUES (%s,%s,%s,%s,%s,%s)'''
#                 cursor.execute(sql,(english_name,korean_name,country_korean,iata_code,icao_code,city_english))
#         conn.commit()
#         conn.close()

region_uploader()
# country_uploader()
# airport_uploader()