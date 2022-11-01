const { src, dest, series, parallel } = require('gulp')
const path = require("path")
const gulp = require("gulp")
//const del =  require('del')
const { existsSync, mkdirSync } =  require('fs')
const zip = require('gulp-zip')
const log =require('fancy-log')
const webpack_stream = require('webpack-stream')
const webpack = require('webpack')
const { webpack_config } = require('./Backend/webpack.config.js')

const { exec } = require('child_process')

const paths = {
    prod_build: 'prod-build',
    server_file_name: 'Backend/server.bundle.js',
    angular_src: 'Frontend/dist/**/*',
    angular_dist: 'prod-build/',
    zipped_file_name: 'angular-nodejs.zip'
}

function clean() {
    log('removing the old files in the directory')
    return del('prod-build/**',{force:true})
}

function createProdBuildFolder() {
    const dir = paths.prod_build
    log(`Creating the folder if not exist ${dir}`)
    if(!existsSync(dir)) {
        mkdirSync(dir)
        log(' folder created:', dir)
    }
    return Promise.resolve('the value is ignored')
}

function buildAngularCodeTask(cb) {
    log('building Angular code into the directory')
    return exec('cd Frontend && npm run build', function(err, stdout, stderr) {
        log(stdout)
        log(stderr)
        cb(err)
    })
}

function copyAngularCodeTask() {
    log('copying Angular code into the directory')
    return src(`${paths.angular_src}`)
           .pipe(dest(`${paths.angular_dist}`))
}



function copyNodeJSCodeTask() {
    log('building and copying server code into the directory')
    return gulp
        .src(['Backend/chunk.js'])
        .pipe(webpack_stream({
            entry: './Backend/server.js',
            mode: 'production',
            target: 'node',
            output: {
                path: path.resolve(__dirname,'js'),
                filename: 'server.bundle.js'
            },
        }))
        .pipe(dest(`${paths.prod_build}`))
}

function zippingTask() {
    log('zipping the code ')
    return src(`${paths.prod_build}/**`)
        .pipe(zip(`${paths.zipped_file_name}`))
        .pipe(dest(`${paths.prod_build}`))
}

exports.default = series(
    //clean,
    createProdBuildFolder,
    buildAngularCodeTask,
    parallel(copyNodeJSCodeTask,copyAngularCodeTask),
    zippingTask
)

