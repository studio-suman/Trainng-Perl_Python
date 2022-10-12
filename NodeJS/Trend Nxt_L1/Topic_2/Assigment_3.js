/*
Assignment 3: 
a) Create a folder called views (there's nothing special about this folder name, it's just a common name for one part of a standard MVC pattern). In this folder make a file called index.html. Add some content to it. 
b) Use fs.readFile to get hold of the about.html file. you can use __dirname to get the current directory. In the fs call back use response.write() to write the file contents to the response. Finally call response.end to send the index.html file content to the user. 
(Note: call-backs are asynchronous, you don't know how long it will take to start reading the file, 
and Node will not wait. This means you will need to call response.end in the fs call back 
or the response will be returned before the file has been read.)

*/
const fs = require("fs");
const http = require("http");

const views = "./views";
if (!fs.existsSync(views)) {
  console.log("Making directory");
  fs.mkdirSync(views);
  console.log("Directory made");
} else {
  console.log("directory mentioned already exists");
}
const htmlContent = "<h1>Writing content in a index.html file<h1>";
console.log("Writing contents in html file");
fs.writeFileSync("./views/index.html", htmlContent);
console.log("Content written in html file successfully");

const server = http.createServer(function (request, response) {
  let path = __dirname + "/views/index.html";
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
