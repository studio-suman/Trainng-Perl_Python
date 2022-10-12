const fs = require("fs");
const http = require("http");

const server = http.createServer(function (request, response) {
  let path = __dirname + "/index.html";
  //console.log(path);
  fs.readFile(path, function (__, data) {
    response.writeHead(200);
    response.end(data);
    //getting a look at the contents for reference
    console.log(data.toString());
  });
});
server.listen(8080);
console.log("listening on localhost:8080");
