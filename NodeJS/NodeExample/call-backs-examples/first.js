var fs = require("fs");  
var data = fs.readFileSync('input.txt');  //Synchronous
console.log(data.toString());  
console.log("Program Ended"); 