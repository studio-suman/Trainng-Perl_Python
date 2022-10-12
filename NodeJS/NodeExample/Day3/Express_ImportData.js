var express = require('express');  // import 
var app = express();

app.get('/txtChk',function(req,res){
     var sStr = req.query.txtName;
	 res.writeHead(200,{'Content-Type':'text/html'});
     res.write(' Thanks for your Co-operation ' + sStr);
	 console.log(' Inside get method ' + sStr);
});

var server = app.listen(3000, function () {   
   console.log("Example app listening at http");
});