// * We can hit the file system with the fs module
// * Requiring modules
// * readFile
// * Filing (like all IO) is done using a callback. This is because Node is single threaded, so blocking on IO is a bad thing.
// * Callback function(error,data){}
// * Order of execution (before, during after)
// * a special variable __dirname gives us access to the app directory.


var fs = require('fs'),
  path = './file.txt';

console.log('before');

fs.readFile(path, function(err, file) {
  console.log('during');
  console.log('' + file);
});

console.log('after');









// Final code
// var fs = require('fs'),
//   path = './file.txt';

// console.log('Before');
// fs.readFile(path, function (error,data) {
//   console.log('In the callback');
// });
// console.log('After');
