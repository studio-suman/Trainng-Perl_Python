var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017";

MongoClient.connect(url,{ useNewUrlParser: true }, function(err, db) {
  if (err) throw err;
  var activeDbf = db.db('test');
  var sRecord = {iTrngNo:1254,sTrngName:"NodeJS",iDuration:3,sMode:"WebEx"};
  activeDbf.collection("NodeJSTrng").insertOne(sRecord,function(err,iInsert){
	  if (err) throw err;
	  console.log(' Record Inserted ');
	  db.close();
  });
  console.log("Database created!");
  
});