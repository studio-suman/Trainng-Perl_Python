var fsTruncate = require("fs");

/* open() takes 3 arguments 
	   1st : Name of the file
	   2nd : Mode [ r, w, r+ ,w+ , a , ... ]
	   3rd : Anonymous function
*/	   
fsTruncate.open("Demo.txt",'r+',function(refError,filePtr){
	if (refError)
		console.log(refError);
	console.log(' File Opened Successfully ');
	/* ftruncate() takes 3 arguments
	   1st : File Pointer
	   2nd : Offset
	   3rd : Anonymous function 
    */	  
    fsTruncate.ftruncate(filePtr,3,function(refError){
       if (refError)
	     console.log(refError);
	   console.log(" File Truncated ");
    });
	
});

