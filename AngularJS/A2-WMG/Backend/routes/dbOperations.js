const { query } = require("express")
const express = require("express")
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
    } catch (err) {
        console.log("sql connectivity error" + err)
    }
}

async function getData_withQuery() {
    try {
        let pool = await sql.connect(config)
        console.log("sql server connected..")
        let res = await pool.request().query("select * from users")
        return res.recordsets
    } catch (err) {
        console.log("sql connectivity error" + err)
    }
}



module.exports = {
    getData: getData,
    getData_withQuery: getData_withQuery,

}