var fs = require('fs'),
  path = './file.txt';

console.log('before');

fs.readFile(path, function(err, file) {
  console.log('during');
  console.log('' + file);
});

console.log('after');
