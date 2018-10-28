var AWS = require('aws-sdk');
AWS.config.loadFromPath('./config.js');

$( document ).ready(function() {
  $( ".buttonchan" ).on("click", function () {
    console.log( "ready!" );
  });
});

$.get( "https://wa797zuhxf.execute-api.us-east-1.amazonaws.com/prod/helloworld", function( data ) {
  console.log(data);
  alert( data );
});
