const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const { urlencoded } = require('body-parser')
var userDb = require('./user')
const connection = require('./dbConfig')
const dbOperations = require('./routes/dbOperations')
const { request, response } = require('express')
var router = express.Router()

const app = express()

app.use(cors())
app.use(bodyParser.json())
app.use(urlencoded({ extended: true }))
process.chdir('../')
app.use(express.static(process.cwd()+"/Frontend/dist/A2-WMG/"))

app.use('/api', router)


router.use((request,response,next) => {
  console.log('middleware')
  next()
})

router.route("/users").get((req,res) => {
  dbOperations.getData().then((result => {
    console.log('this value ' +result)
    res.json(result)
  }))
})

router.route("/users/:id").get((req,res) => {
  dbOperations.getData_withQuery(req.params.id).then((result => {
    console.log('this value ' +result)
    res.json(result[0])
  }))
})



process.chdir('../')
app.get('/',(req,res) => {
  res.sendFile(process.cwd()+"/Frontend/dist/A2-WMG/index.html")
})

app.listen(3080,()=>{
    console.log('server & api running...')
})