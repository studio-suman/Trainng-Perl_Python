const { query } = require("express");
const express = require("express");
const connection = require("../connection");
const router = express.Router();


router.post('/signup',(req, res) => {
    let user = req.body;
    query = "select email,password,role,status from users where email=?"
    connection.execSql(query)
    if(!err) {}
    else {
        return res.status(500).json(err);
    }
})


module.exports = router