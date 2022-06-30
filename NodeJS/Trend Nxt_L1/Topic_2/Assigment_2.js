/*
Assignment 2: 
a) Create a simple HTTP server that responds to requests with a simple HTML response. (Hint : using http module)
b) Create a Node JS Script, using ‘http’ module that downloads the content from a web page to a File 
E.g. to download the google home page 
c) Write a Node JS script file to create & emit custom events one, two & three with messages “First Event” ,”Second Event” & “Third Event” by using Event Emitter class of Events module

*/

const http = require("http");
const fs = require("fs");

const server = http.createServer(function (request, response) {
  response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  response.end("<h1>Welcome To Your First Server !</h1>");
});

server.listen(8080, function () {
  console.log(`Listening on port http://localhost:8080/`);
});


const request = http.get("http://www.google.com/", function (response) {
  console.log("Downloading file");
  response.pipe(fs.createWriteStream("google.html")); //we can create a file by changing the extension value to ".txt" that file is also included in the b directory
  console.log("File Downloaded");
});


const events = require("events");
const eventEmitter = new events.EventEmitter();
var one = function FirstEvent() {
  console.log("First Event");
};
eventEmitter.on("one", one);
var two = function SecondEvent() {
  console.log("Second Event");
};
eventEmitter.on("two", two);
var three = function ThirdEvent() {
  console.log("Third Event");
};
eventEmitter.on("three", three);
eventEmitter.emit("one");
eventEmitter.emit("two");
eventEmitter.emit("three");
