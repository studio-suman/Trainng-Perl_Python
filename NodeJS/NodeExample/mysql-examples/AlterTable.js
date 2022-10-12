var mysql = require('mysql');  
var con = mysql.createConnection({  
host: "localhost",  
user: "root",  
password: "root123",  
database: "nodejsexamples1"  
});  
con.connect(function(err) {  
if (err) throw err;  
console.log("Connected!");  
var sql = "drop table employees";  
con.query(sql, function (err, result) {  
if (err) throw err;  
console.log(result);  
});  
});  