const fs = require("fs");
const views = "./views";
if (!fs.existsSync(views)) {
  console.log("Making directory");
  fs.mkdirSync(views);
  console.log("Directory made");
} else {
  console.log("directory mentioned already exists");
}
const htmlContent = "<h1>Some content in a index.html file<h1>";
console.log("Writing contents in html file");
fs.writeFileSync("./views/index.html", htmlContent);
console.log("Content written in html file successfully");
