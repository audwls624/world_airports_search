const mysql = require("mysql"); //mariadb가 아니라 mysql이라 적어야 됨!

router.get('/:id', function(req, res) {
    const connection = mysql.createConnection({
    host: '127.0.0.1',
    port: 3306,
    user: "root",
    password: "adsf25did",
    connectionLimit: 5,
    database: "airport"
    });
    connection.connect();
    connection.query("SELECT * FROM airports WHERE id=?", [req.params.id], function(err, rows, fields){
        if(!err){
            console.log(rows);
            console.log(fields);
            let result="rows: " + JSON.stringify(rows) + "<br><br>" + "fields: " + JSON.stringify(fields);
            res.send(result);
    }   else {
            console.log("query error: " + err);
            res.send(err);
    }
    });
    connection.end();
});