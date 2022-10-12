var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017";

MongoClient.connect(url, { useNewUrlParser: true }, function(err, dbfPtr) {
  if (err) throw err;
  var activeDbf = dbfPtr.db('test');
  activeDbf.createCollection("NodeJSTrng",function(err,colStatus){
	  if (err) throw err;
	  console.log(' Collection Created ');
	  dbfPtr.close();
  });
  console.log("Database created!");
  
});