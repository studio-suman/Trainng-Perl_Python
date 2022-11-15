const { query } = require("express")
const express = require("express")
const { info } = require("fancy-log")
const sql = require("mssql")
var config = require("../dbConfig")
const router = express.Router()


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

async function getData_withQuery(userName) {
    try {
        let pool = await sql.connect(config)
        console.log("sql server connected..")
        let res = await pool.request()
                .input('input_param',sql.Int, userName)
                .query(`Select * from users where name = @input_param`)
        return res.recordsets
    } catch (info) {
        console.log("sql connectivity error " + info)
    }
}

async function addUser(userDb) {
    try {
        let pool = await sql.connect(config)
        console.log("sql server connected..")
        let res = await pool.request()
                //.input('id',sql.Int, userDb.id)
                .input('name',sql.NVarChar, userDb.name)
                .input('contactNumber',sql.NVarChar, userDb.contactNumber)
                .input('email',sql.NVarChar, userDb.email)
                .input('password',sql.NVarChar, userDb.password)
                .input('status',sql.NVarChar, userDb.status)
                .input('role',sql.NVarChar, userDb.role)
                .execute('addUser')
        return res.recordsets
    } catch (info) {
        console.log("sql connectivity error " + info)
    }
}

async function updateUser(userDb) {
    try {
        let pool = await sql.connect(config)
        console.log("sql server connected..")
        let res = await pool.request()
                .input('id',sql.Int, userDb.id)
                .input('name',sql.NVarChar, userDb.name)
                .input('contactNumber',sql.NVarChar, userDb.contactNumber)
                .input('email',sql.NVarChar, userDb.email)
                .input('password',sql.NVarChar, userDb.password)
                .input('status',sql.NVarChar, userDb.status)
                .input('role',sql.NVarChar, userDb.role)
                .execute('updateUser')
        return res.recordsets
    } catch (info) {
        console.log("sql connectivity error " + info)
    }
}

async function deleteUser(userName){
    try {
        let pool = await sql.connect(config)
        console.log("sql server connected..")
        let res = await pool.request()
                .input('input_param',sql.NVarChar, userName)
                .query(`Delete from users where name = @input_param`)
        return res.recordsets
    } catch (info) {
        console.log("sql connectivity error " + info)
    }
}


module.exports = {
    getData: getData,
    getData_withQuery: getData_withQuery,
    addUser: addUser,
    deleteUser: deleteUser,
    updateUser: updateUser,
}