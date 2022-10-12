var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017";

MongoClient.connect(url, { useNewUrlParser: true }, function(err, db) {
  if (err) throw err;
  var activeDbf = db.db('test');
  activeDbf.collection("NodeJSTrng").find({}).toArray(function(err,sRecords){
	   if (err) throw err;
	   console.log(sRecords);
	   db.close();
  });

  console.log("Database created!");
  
});