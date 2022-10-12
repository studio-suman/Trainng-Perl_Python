const fs = require("fs");
const testFolder = process.argv[2];
fs.readdir(testFolder, (err, files) => {
  files.forEach((file) => {
    console.log(file);
  });
});
// const fs = require("fs");

// const folderPath = process.argv[2];
// fs.readdirSync(folderPath);
