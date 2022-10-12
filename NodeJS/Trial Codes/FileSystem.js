var fs = require("fs");  
// Asynchronous read  
fs.readFile('input.txt', function (err, data) {  
   if (err) {  
       return console.error(err);  
   }  
   console.log("Asynchronous read: " +data.toString());  
});  
// Synchronous read  
var data = fs.readFileSync('input.txt');  
console.log("Synchronous read: " +data.toString());  
console.log("Program Ended");  

fs.writeFile('somedata.txt','Happy New Year', function (err, data) {  
    if (err) { 
        return console.error(err);  
    }  
    console.log("Asynchronous read: " +data.toString());  
 });  

var dt="\n Learning Node.JS";
fs.appendFile("./input.txt",dt,"utf8",function(err){
        if(err)
            throw err;
        console.log("Data is appended to the file");
        });

console.log("Opening the File");
fs.open('input.txt','r+',function(err,fd){
        if(err)
        {
            return console.error(err);
        }
    console.log("File open successfully");
    });

var path='input.txt';
fs.stat(path, function(err, stats) {
    console.log(path);
    console.log();
    console.log(stats);
    console.log();
 
    if (stats.isFile()) {
        console.log('    file');
    }
    if (stats.isDirectory()) {
        console.log('    directory');
    }
 
    console.log('    size: ' + stats["size"]);
});
