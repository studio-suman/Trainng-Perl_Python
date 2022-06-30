var fsDelete = require("fs");

/* unlink() takes 2 arguments 
	  1st : Name of the file
	  2nd : Anonymous Function
*/	  
fsDelete.unlink("Dmo.txt",function(refError){
    if (refError)
	   console.log(refError);
	console.log(' File Deleted Successfuly ');
});