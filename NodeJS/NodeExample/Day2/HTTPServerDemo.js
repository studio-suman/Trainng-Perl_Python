var httpServer = require('http');

console.log(httpServer);

var custServer = httpServer.createServer(function(refRequest,refResponse){
	refResponse.writeHead(200,{'Content-Type':'text/html'});
	refResponse.write(' Enjoying the Training ');
	refResponse.write('<br>');
	refResponse.write(' NodeJS is interesting ');
	refResponse.end();
});

custServer.listen(3918);
console.log(' Customizing Node as WebServer');