const path = require('path')

module.exports = {

    entry: './server.js',
    mode: 'production',
    target: 'node',
    output: {
        path: path.resolve(__dirname,'js'),
        filename: 'server.bundle.js'
    },
    devServer: {
        inline: false,
        contentBase: "./dist",
    },
    resolve: {
        extensions: ['.js', '.jsx']
      },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude:/(node_modules|bower_components)/,
                loader: 'babel-loader'
            }
        ]
    }

}
