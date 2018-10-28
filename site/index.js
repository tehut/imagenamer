var AWS = require('aws-sdk');
AWS.config.loadFromPath('./config.js');

$( document ).ready(function() {
  $( ".buttonchan" ).on("click", function () {
    console.log( "ready!" );
  });
});
