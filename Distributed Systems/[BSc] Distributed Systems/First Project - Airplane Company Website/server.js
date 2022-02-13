var express = require( 'express' )
var cors = require( 'cors' )
var app = express()
var body_parser = require( 'body-parser' )
var fs = require( 'fs' )

app.use( body_parser.urlencoded( { extended : false } ) )
app.use( body_parser.json() )

app.use(cors({
    'allowedHeaders': ['sessionId', 'Content-Type'],
    'exposedHeaders': ['sessionId'],
    'origin': '*',
    'methods': 'GET,HEAD,PUT,PATCH,POST,DELETE',
    'preflightContinue': false
  }));

var path_booked = __dirname + "/source/booked.json"


app.get( '', function( req, res ) {

    console.log( "User connected" )
    res.end( "caralho" )

})

app.post( '/count_booked', function( req, res ) {

    fs.readFile( path_booked, 'utf8', function( err, data ) {
        
        var leng = Object.keys( JSON.parse( data ) ).length
        
        console.log( "Exists " + leng + " booked flights" )
        res.end( JSON.stringify( { 'count' : leng.toString() } ) )
    
    })

})

app.post( '/flight_list', function( req, res ) {

    fs.readFile( path_booked, 'utf8', function( err, data ) {

        console.log( data )
        res.end( data )

    })
    
})


var server = app.listen( 8081, function() {

    var host = server.address().address
    var port = server.address().port
    console.log( "Server is listening at http://%s:%s\n", host, port )

})
