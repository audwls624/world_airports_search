import pymysql

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    word = request.args.get('word')
    conn = pymysql.connect(host='10.211.55.4',user='root',password='adsf25did',db='airport',charset='utf8mb4')
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM countries JOIN airports ON countries.korean_name=airports.country_korean \
            JOIN regions ON regions.name=countries.region \
            WHERE countries.english_name LIKE '%{word}%' \
        or regions.name LIKE '%{word}%' or countries.korean_name LIKE '%{word}%' or airports.english_name LIKE '%{word}%' \
        or airports.korean_name LIKE '%{word}%' or airports.iata_code LIKE '%{word}%' or airports.icao_code LIKE '%{word}%' \
        or airports.city_english LIKE '%{word}%' "
        cursor.execute(sql)
        data=[{'country(korean)':airport[0],
            'country(english)':airport[1],'continent':airport[2],'airport(korean)':airport[3],'airport(english)':airport[4],
            'IATA_code':airport[5],'ICAO_code':airport[6],'city(english)':airport[8]} for airport in cursor.fetchall()]
    conn.commit()
    conn.close()
    return jsonify({'data':data})

if __name__ == '__main__': app.run(debug=True)