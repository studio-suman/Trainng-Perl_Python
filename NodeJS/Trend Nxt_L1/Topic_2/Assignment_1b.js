/* Assignment 1: a) Create Server socket that listens at a port number 3000 and creates sockets for every client request and sends “Hello Client” message (Hint: Use net module) 
b) Send a request to server from browser(http://localhost:3000) & get the response 
c) Create a client socket that sends request to the server along with a message “Hello Server” 
d) Test it through ‘telnet’, to see the message echo.

*/
var net = require('net');
var http = require('http');
var colors = require('colors');

var server = net.createServer(function(c) {//'connection' listener
  console.log('Client connected' .green);
    c.on('end', function() {
    console.log('Client disconnected'.yellow);
     });
    c.write('Hello Client\r\n' .red);
    //c.pipe(c);

    c.on('error', (err) => { 
    console.log(`Error occurred in : ${err.message}`); 
        }); 
});
server.listen(3000, function() { //'listening' listener
  console.log('server bound');
});