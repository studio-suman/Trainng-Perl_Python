var fileServer = require("fs");
var cmpFile = require("zlib");

fileServer.createReadStream("URLDemo.js").pipe(cmpFile.createGzip()).pipe(fileServer.createWriteStream('URLDemo.gz'));

console.log(" File Compressed ");


