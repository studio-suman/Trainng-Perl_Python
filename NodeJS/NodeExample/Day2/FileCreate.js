var fsCreate = require("fs");
var sStr = ' Learning NodeJS from TT - Day 2';
/* writeFile() - Takes 4 arguments 
	      	1st	: Filename
		    2nd	: Content to be written
		    3rd	: Optional ,which mode the file as to be written , default mode is utf8
		    4th	: AnonymousFunction */		  
fsCreate.writeFile("Demo.txt",sStr,function(refError){
    if (refError)
      console.log(refError);
    console.log(" File created successfully ");
});