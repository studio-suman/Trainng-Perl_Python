const { query } = require("express")
const express = require("express")
const { info } = require("fancy-log")
const sql = require("mssql")
var config = require("../dbConfig") 
const router = express.Router()


/* router.post('/signup',(req, res) => {
    let user = req.body;
    query = "select email,password,role,status from users where email=?"
    connection.execSql(query)
    if(!err) {}
    else {
        return res.status(500).json(err);
    }
}) */

async function getData() {
    try {
        let pool = await sql.connect(config)
        console.log("sql server connected..")
        debugger
        let res = await pool.request().query(`Select * from users`)
        return res.recordsets
    } catch (info) {
        console.log("sql connectivity error " + info)
    }
}

async function getData_withQuery(userId) {
    try {
        let pool = await sql.connect(config)
        console.log("sql server connected..")
        let res = await pool.request()
                .input('input_param',sql.Int, userId)
                .query(`Select * from sys.sysdatabases where dbId = @input_param`)
        return res.recordsets
    } catch (info) {
        console.log("sql connectivity error " + info)
    }
}



module.exports = {
    getData: getData,
    getData_withQuery: getData_withQuery,

}