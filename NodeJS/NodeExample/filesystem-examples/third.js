var fs=require('fs');
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
