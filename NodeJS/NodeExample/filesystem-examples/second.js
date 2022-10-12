var fs = require("fs");
console.log("Trying Writing");
fs.writeFile('somedata.txt', 'Happy Learning',  function(err) {
   if (err) {
       return console.error(err);
   }
   console.log("Writing Done !");
});
