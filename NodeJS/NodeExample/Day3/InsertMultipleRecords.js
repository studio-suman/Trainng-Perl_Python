var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017";

MongoClient.connect(url, { useNewUrlParser: true },function(err, db) {
  if (err) throw err;
  var activeDbf = db.db('test');
  var aRecords = [{iTrngNo:1254,sTrngName:"NodeJS",iDuration:3,sMode:"WebEx"},{iTrngNo:1263,sTrngName:"Java8",iDuration:4,sMode:"WebEx"},{iTrngNo:1281,sTrngName:"Angualr JS",iDuration:3,sMode:"WebEx"}];
  
  activeDbf.collection("NodeJSTrng").insertMany(aRecords,function(err,iStatus){
	   if (err) throw err;
	   console.log(' Multiple Records inserted ');
	   db.close();
  });

  console.log("Database created!");
  
});