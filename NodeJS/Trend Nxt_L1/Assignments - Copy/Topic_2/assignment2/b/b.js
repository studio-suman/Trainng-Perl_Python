const http = require("http"); // or 'https' for https:// URLs
const fs = require("fs");

const request = http.get("http://www.google.com/", function (response) {
  console.log("Downloading file");
  response.pipe(fs.createWriteStream("google.html")); //we can create a file by changing the extension value to ".txt" that file is also included in the b directory
  console.log("File Downloaded");
});
