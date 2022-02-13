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

    console.log( req )
    res.end( "caralho" )

})


app.get( '/insert_planes1', function( req, res ) {
    
    fs.readFile(path_booked, (err, data) => {  
        if (err) throw err;
        let words = JSON.parse(data);
        var leng = Object.keys( words.planes ).length
        
        id=leng+1
        //delete words.planes["plane_"+ id];
        

        words.planes["plane_"+id]={
            partida_dia: '11',
            chegada_dia: '12',
            partida_segundos: '1000',
            chegada_segundos: '1000',
            status: 'awaiting',
            price: '100',
            destino: 'portugal',
            partida: 'italia'
        }

        let data_planes = JSON.stringify(words);
        fs.writeFileSync(path_booked, data_planes);  
    });

    res.end( "oi "  )

})


app.post( '/delete_planes', function( req, res ) {

    fs.readFile(path_booked, (err, data) => {  
        if (err) throw err;
        let words = JSON.parse(data);
        var leng = Object.keys( words.planes ).length
        
        id=leng
        
        //delete words.planes["plane_"+req.body.id];
 
        delete words.planes["plane_"+id];

        /*var i;
        for(i=req.body.id;i<=id;i++){
            words.planes["plane_"+i]=words.planes["plane_"+i+1]

        }*/
        //delete words.planes["plane_"+id];

        let data_planes = JSON.stringify(words);
        fs.writeFileSync(path_booked, data_planes); 
        res.end( data_planes )
        
    });


})

app.post( '/insert_planes', function( req, res ) {

    fs.readFile(path_booked, (err, data) => {  
        if (err) throw err;
        let words = JSON.parse(data);
        var leng = Object.keys( words.planes ).length
        
        id=leng+1
        
        words.planes["plane_"+id]=req.body
        var leng = Object.keys( words.planes ).length
        let data_planes = JSON.stringify(words);
        fs.writeFileSync(path_booked, data_planes);
        res.end( JSON.stringify( { 'count' : leng.toString() } ) )
    
    });


})


app.post( '/count_booked', function( req, res ) {

    fs.readFile( path_booked, 'utf8', function( err, data ) {
        
        var leng = Object.keys( JSON.parse( data ).planes ).length
        
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
