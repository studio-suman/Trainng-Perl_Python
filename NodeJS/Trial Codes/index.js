// include node fs module
var fs = require("fs");
var data = fs.readFileSync('input.txt')
 
fs.readFile('input.txt', function(err, data) {
    if(err) return console.error(err);
    console.log(data.toString());
});
console.log("Program Ended");


var http = require('http');
var dt = require('./firstModule');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write("The date and time are currently: " + dt.myDateTime());
  res.end();
}).listen(8087);