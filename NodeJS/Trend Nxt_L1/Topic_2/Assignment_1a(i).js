var net = require('net');
var colors = require('colors');

var client = net.connect({port: 3000},
    function() { //'connect' listener
  console.log('connected to server!'.green);
  client.write('Hello Server!!\r\n'.green);
  });
  client.on('data', function(data) {
  console.log(data.toString());
  client.end();
  });
  client.on('end', function() {
  console.log('disconnected from server'.rainbow);

  client.on('error', (err) => {
  console.log(`Error occurred in : ${err.message}`); 
        }); 
  });