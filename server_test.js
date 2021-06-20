const http = require('http');
const url = require('url');
const querystring = require('querystring'); 
const mysql = require('mysql');

const server = http.createServer(function(request,response){
    console.log('--- log start ---');
    const parsedUrl   = url.parse(request.url);
    const parsedQuery = querystring.parse(parsedUrl.query,'&','=');
    const word        = parsedQuery.word;
    const connection = mysql.createConnection({
        host: '127.0.0.1',
        port: 3306,
        user: "root",
        password: "adsf25did",
        connectionLimit: 5,
        database: "airport"
        });
    connection.connect();
    sql=`SELECT * FROM countries \ 
        JOIN airports ON countries.korean_name=airports.country_korean \
        JOIN regions ON regions.name=countries.region \
        WHERE countries.english_name LIKE '%${word}%' \
        or regions.name LIKE '%${word}%' or countries.korean_name LIKE '%${word}%' or airports.english_name LIKE '%${word}%' \
        or airports.korean_name LIKE '%${word}%' or airports.iata_code LIKE '%${word}%' or airports.icao_code LIKE '%${word}%' \
        or airports.city_english LIKE '%${word}%' `
    connection.query(sql, function(err, rows, fields){
        if(!err){    
            const data = new Array();
            for (let i = 0; i < rows.length; i++) {
                data[i]= {
                    korean_name:rows[i].korean_name,
                    english_name:rows[i].english_name,
                    continent:rows[i].region,
                    IATA_CODE:rows[i].iata_code,
                    ICAO_CODE:rows[i].icao_code,
                    country:rows[i].country_korean,
                    city:rows[i].city_english
                }                
            }
            console.log(data)
            response.writeHead(200, {'Content-Type':'text/html'});
            response.write(JSON.stringify(data));
            response.end();
        }else{
            console.log("query error: " + err);
            response.send(err);
        }
        });
    connection.end();
    console.log('--- log end ---');
});

server.listen(8088, function(){
    console.log('Server is running...');
});