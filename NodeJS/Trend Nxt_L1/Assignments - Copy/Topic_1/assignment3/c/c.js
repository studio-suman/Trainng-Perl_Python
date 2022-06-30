const fs = require("fs");
let y = 1; //no. of years
let c = 1; //no. of centuries
//console.log("number of seconds in a year");
let x = y * 60 * 60 * 24 * 365;
const secondsInYear = "number of seconds in " + y + " year : " + x + "\n";
fs.writeFile("print.txt", secondsInYear.toString(), (err) => {
  if (err) throw err;
});
console.log("written successfully for years");
let secondsInCentury = c * 60 * 60 * 24 * 365 * 100;
secondsInCentury =
  "number of seconds in " + c + " century : " + secondsInCentury;
fs.appendFile("print.txt", secondsInCentury.toString(), (err) => {
  if (err) throw err;
});
console.log("written successfully for century");
