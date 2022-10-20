const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const { urlencoded } = require('body-parser');
const connection = require('./connection')
const userRoute = require('./routes/user')

const app = express()

app.use(cors())
app.use(bodyParser.json())
app.use(urlencoded({ extended: true }))
process.chdir('../')
app.use(express.static(process.cwd()+"/Frontend/dist/A2-WMG/"))

app.use('/user',userRoute)


  
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

  app.get('/user1',(req,res)=>{

    req.sql("select * from [dbo].[scott.emp]").into(res)
    
  })
process.chdir('../')
app.get('/',(req,res) => {
  res.sendFile(process.cwd()+"/Frontend/dist/A2-WMG/index.html")
})

app.listen(3080,()=>{
    console.log('server running...')
})