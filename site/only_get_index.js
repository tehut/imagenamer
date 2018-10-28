


$( document ).ready(function() {

  $( ".buttonchan" ).on("click", function () {
    $.ajax({
      type: "POST",
      url: "https://wa797zuhxf.execute-api.us-east-1.amazonaws.com/prod/helloworld",
      data:  {
        "input": "{\"comments\": \"test\"}",
        "stateMachineArn": "arn:aws:states:us-east-1:459472629219:stateMachine:StepTest-the-second"
      }
    });
  });
});

// apigateway.createApi(params, function (err, data) {
//   if (err) console.log(err)
//   console.log(data)
// })


