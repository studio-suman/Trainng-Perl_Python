var refFile = require('fs');
var acBuffer = new Buffer(2560);

refFile.open('URLDemo.js','r',function(refError,filePtr){
     if (refError)
	    console.log(' File Not opened ');
	 refFile.read(filePtr,acBuffer,0,acBuffer.length,0,function(refErr,iBytes){
	    if (refErr)
		  console.log(' Challenges in reading the content of the file ');
		console.log(acBuffer.slice(0,iBytes).toString());
	    
	 });
	 refFile.close(filePtr,function(rfErr){
	    if (rfErr)
		   console.log(' Still open ');
		console.log(' File Opened , Read the contents and closed it ');
	 });
});