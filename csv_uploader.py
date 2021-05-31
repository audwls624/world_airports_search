import csv
import pymysql

REGION_CSV_PATH='./regions.csv'
COUNTRY_CSV_PATH='./distinct_countries.csv'
CITY_CSV_PATH='./regions_final.csv'
AIRPORT_CSV_PATH='./airports.csv'

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
                korean_name = row['korean_name']
                english_name = row['english_name']
                sql  = '''INSERT INTO continents (korean_name,english_name) VALUES (%s,%s)'''
                cursor.execute(sql,(korean_name,english_name))
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
                continent = row['continent']
                korean_name = row['korean_name']
                english_name = row['english_name']
                sql  = '''INSERT INTO countries (english_name,korean_name,continent_id) VALUES (%s,%s,(select ID from continents where korean_name=%s))'''
                cursor.execute(sql,(english_name,korean_name,continent))
        conn.commit()
        conn.close()

def city_uploader():
    with open(CITY_CSV_PATH, newline='', encoding='utf8') as csvfile:	
        data_reader = csv.DictReader(csvfile)
        conn = pymysql.connect(host='localhost',
        user='root',
        password='adsf25did',
        db='airports',
        charset='utf8mb4')
        for row in data_reader:
            with conn.cursor() as cursor:
                english_name = row['city_english']
                country     = row['country_korean']
                sql  = '''INSERT INTO cities (english_name,country_id) VALUES (%s,(select ID from countries where korean_name=%s))'''
                cursor.execute(sql,(english_name,country))
        conn.commit()
        conn.close()

def airport_uploader():
    with open(AIRPORT_CSV_PATH, newline='', encoding='utf8') as csvfile:	
        data_reader = csv.DictReader(csvfile)
        conn = pymysql.connect(host='localhost',
        user='root', 
        password='adsf25did',
        db='airports',
        charset='utf8mb4')
        for row in data_reader:
            with conn.cursor() as cursor:
                english_name   = row['english_name']
                korean_name    = row['korean_name']
                iata_code      = row['iata_code']
                icao_code      = row['icao_code']
                city           = row['city_english']
                sql  = '''INSERT INTO airports (english_name,korean_name,iata_code,icao_code,city_id) VALUES (%s,%s,%s,%s,(select ID from cities where english_name=%s))'''
                cursor.execute(sql,(english_name,korean_name,iata_code,icao_code,city))
        conn.commit()
        conn.close()

region_uploader()
country_uploader()
city_uploader()
airport_uploader()