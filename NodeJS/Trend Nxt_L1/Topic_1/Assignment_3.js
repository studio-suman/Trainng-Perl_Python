/* Assignment 3 : 
a) Create a user defined date module that can give you the current date and time. 
b) Write a Node script file to display current Date & Time by using user defined date module. 
c) Write a Node script file to find out how many seconds are there in a year. 
How many seconds are there in a century and writes the result into a file. 
d) Create a daysTill custom module. It should be able to give you the number of days till Christmas and the number of days till mother’s day. 
number of days till your Birthday.(Hint : Subtract both the dates to get difference in no.of milliseconds) */

var dt = require('./DateTimeModule');
var fs = require("fs");

console.log("The date and time are currently: " + dt.myDateTime());

//******************************************************************* */

let y = 1; //no. of years
let c = 1; //no. of centuries
//console.log("number of seconds in a year");
let x = y * 60 * 60 * 24 * 365;
const secondsInYear = "number of seconds in " + y + " year : " + x + "\n";
fs.writeFile("somedata.txt", secondsInYear.toString(), (err) => {
  if (err) throw err;
});
console.log("Written successfully for years");
let secondsInCentury = c * 60 * 60 * 24 * 365 * 100;
secondsInCentury = "number of seconds in " + c + " century : " + secondsInCentury;
fs.appendFile("print.txt", secondsInCentury.toString(), (err) => {
  if (err) throw err;
});
console.log("Written successfully for century");
