const http = require("http");
const server = http.createServer(function (request, response) {
  response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  response.end("<h1>Welcome To Your First Server !</h1>");
});

server.listen(8080, function () {
  console.log(`Listening on port http://localhost:8080/`);
});
