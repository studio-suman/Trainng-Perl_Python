var reqValid = require('http');

var custServer = reqValid.createServer(function(refRequest,refResponse){
   if (refRequest.url == '/') {
	   refResponse.writeHead(200,{'Content-Type':'text/html'});
	   refResponse.write(' Doing Multitasking during Training ');
	   refResponse.end();
   }
   else if (refRequest.url == '/NodeJS') {
	   refResponse.writeHead(200,{'Content-Type':'text/html'});
	   refResponse.write('<html><body><h1> WebEx Training - Feeling Sleepy </h1></body></html>');
	   refResponse.end();
   }
   else{
	   refResponse.writeHead(200,{'Content-Type':'text/html'});
	   refResponse.write('Check the URL ');
	   refResponse.end(); 
   }
});

custServer.listen(4620);
console.log(' Server is Up and Running ');