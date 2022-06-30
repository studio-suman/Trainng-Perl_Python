var fs= require("fs");
var zlib = require("zlib");
fs.createReadStream('URLDemo.gz').pipe(zlib.createGunzip()).pipe(fs.createWriteStream('Dmo.txt'));
console.log(" File Decompressed ");