var fsInfo = require("fs");

/* stat() is a CallBack Method */
fsInfo.stat("FileCreate.js",function(refError,refFileInfo){
      if (refError)
	     console.log(refError);
      console.log(refFileInfo);
      console.log(refFileInfo.isFile());
});