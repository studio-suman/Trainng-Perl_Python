const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const { Connection, Request } = require("tedious");
const { urlencoded } = require('body-parser');

const app = express()

app.use(cors())
app.use(bodyParser.json())
app.use(urlencoded({ extended: true }))
process.chdir('../')
app.use(express.static(process.cwd()+"/Frontend/dist/A2-WMG/"))

//database connection

// Create connection to database
const config = {
    authentication: {
      options: {
        userName: "db", // update me
        password: "welcome@123" // update me
      },
      type: "default"
    },
    server: "mis-db.database.windows.net", // update me
    options: {
      database: "MIS_DB", //update me
      encrypt: true
    }
  };

  
  const connection = new Connection(config);
  
  // Attempt to connect and execute queries if connection goes through
  connection.on("connect", err => {
    if (err) {
      console.error(err.message);
    } else {
        console.log('Connected to MIS_DB...');
    }
    //connection.close();
  });
  
  connection.connect();
  
  function queryDatabase() {
    console.log("Reading rows from the Table...");
  
    // Read all rows from table
    const request = new Request(
      `select * from [dbo].[scott.emp]`,
      (err, rowCount) => {
        if (err) {
          console.error(err.message);
        } else {
          console.log(`${rowCount} row(s) returned`);
        }
      }
    );
  
    request.on("row", columns => {
      columns.forEach(column => {
        console.log("%s\t%s", column.metadata.colName, column.value);
      });
    });
  
    connection.execSql(request);
  }

  app.get('/user',(req,res)=>{

    req.sql("select * from [dbo].[scott.emp]").into(res)
    
  })
process.chdir('../')
app.get('/',(req,res) => {
  res.sendFile(process.cwd()+"/Frontend/dist/A2-WMG/index.html")
})

app.listen(3080,()=>{
    console.log('server running...')
})