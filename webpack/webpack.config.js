var webpack = require('webpack');
var path = require('path');
var autoprefixer = require('autoprefixer');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: {
    'app': './js/main.js',
    'styles': './scss/main.scss'
  },
  output: {
    path: path.dirname(__dirname) + '/assets/static/gen',
    publicPath: '/static',
    filename: '[name].js'
  },
  devtool: '#cheap-module-source-map',
  resolve: {
    modules: [
      path.join(__dirname, "src"),
      'node_modules',
    ],
    extensions: ['.js']
  },
  module: {
   rules: [
    {
      test: /\.(woff(2)?|ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,    //to support @font-face rule 
      loader: "url-loader",
      query:{
        limit:'10000',
        name:'[name].[ext]',
        outputPath:'fonts/'
        //the fonts will be emmited to public/assets/fonts/ folder 
        //the fonts will be put in the DOM <style> tag as eg. @font-face{ src:url(assets/fonts/font.ttf); } 
      }
    },
    {
      test: /\.css$/,
      loaders: ["style-loader","css-loader"]
    },

      {
       test: /\.scss$/,
       use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: "css-loader!sass-loader"
        })
      },
      {
        test: /\.jsx$/,
        loader: "babel-loader", // Do not use "use" here
      }
    ]
  },
  plugins: [
    new ExtractTextPlugin('styles.css', {
      allChunks: true
    }),
    new webpack.ProvidePlugin({
        $: "jquery",
        jQuery: "jquery"
    }),
    new webpack.optimize.UglifyJsPlugin()
  ],
};