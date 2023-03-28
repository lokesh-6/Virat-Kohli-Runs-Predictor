function onClickedEstimateRuns() {


  console.log("Estimate runs button clicked");
  var BF = document.getElementById("uiBF");
  var F = document.getElementById("uiF");
  var S = document.getElementById("uiS");
  var teams = document.getElementById("uiteams");
  var estPrice = document.getElementById("uiEstimatedRuns");

   var url = "http://127.0.0.1:5000/predict_runs"; 

  $.post(url, {
      balls_faced: parseFloat(BF.value),
      fours: parseInt(F.value),
      sixes: parseInt(S.value),
      teams: teams.value
  },function(data, status) {
      console.log(data.estimated_runs);
      estPrice.innerHTML = "<h2>" + data.estimated_runs.toString() + " Runs</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
   var url = "http://127.0.0.1:5000/get_team_names"; 
  $.get(url,function(data, status) {
      console.log("got response for get_team_names request");
      if(data) {
          var teams = data.teams;
          var uiteams = document.getElementById("uiteams");
          $('#uiteams').empty();
          for(var i in teams) {
              var opt = new Option(teams[i]);
              $('#uiteams').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
