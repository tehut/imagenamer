var AWS = require('aws-sdk');
AWS.config.loadFromPath('./config.js');
var apigateway = new AWS.APIGateway();

$( document ).ready(function() {
  $( ".buttonchan" ).on("click", function () {
    console.log( "ready!" );
  });
});

var params = {
  "input": "{\"comments\": \"test\"}",
  "stateMachineArn": "arn:aws:states:us-east-1:459472629219:stateMachine:StepTest-the-second"
}
apigateway.createApi(params, function (err, data) {
  if (err) console.log(err)
  console.log(data)
})
