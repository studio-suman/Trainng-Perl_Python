var fsRead =require("fs");

/* readFile() is an CallBack Method */
var sData = fsRead.readFileSync('URLDemo.js');
console.log(sData.toString());

console.log(' Feeling relaxed after the Break ');