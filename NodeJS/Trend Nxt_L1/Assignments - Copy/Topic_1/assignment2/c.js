//reading file synchronously
const fs = require("fs");
let content = fs.readFileSync("hello.txt");
console.log("Synchronous read: " + content.toString());
//reading asynchronously
fs.readFile("hello.txt", function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log("Asynchronous read: " + data.toString());
});
