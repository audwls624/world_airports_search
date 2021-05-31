import pymysql

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    word = request.args.get('word')
    conn = pymysql.connect(host='localhost',user='root',password='adsf25did',db='airports',charset='utf8mb4')
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM continents \
                JOIN countries on continents.ID=countries.continent_id \
                JOIN cities on countries.ID=cities.country_id \
                JOIN airports on cities.ID=airports.city_id \
                where continents.korean_name LIKE '%{word}%' or countries.korean_name LIKE '%{word}%' \
                or continents.english_name LIKE '%{word}%' or countries.english_name LIKE '%{word}%' \
                or cities.english_name LIKE '%{word}%' or cities.korean_name LIKE '%{word}%' \
                or airports.english_name LIKE '%{word}%' or airports.korean_name LIKE '%{word}%' \
                or airports.iata_code LIKE '%{word}%' or airports.icao_code LIKE '%{word}%'"
        cursor.execute(sql)
        data=[{'continents(kor)':airport[1],'continents(eng)':airport[2],'country(kor)':airport[4],'country(eng)':airport[5],'city(eng)':airport[9],
                'name(kor)':airport[12],'name(eng)':airport[13],'iata_code':airport[14],'icao_code':airport[15]} for airport in cursor.fetchall()]
        print(data)
    conn.commit()
    conn.close()
    return jsonify({'data':data})

if __name__ == '__main__': app.run(debug=True)