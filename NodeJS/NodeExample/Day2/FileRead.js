var fsRead =require("fs");

/* readFile() is an CallBack Method */
fsRead.readFile('URLDemo.js',function(iError,sData){
     if (iError){
	    console.log("File Not Found");
	 }
	 console.log(sData.toString());
});
console.log(' Feeling relaxed after the Break ');