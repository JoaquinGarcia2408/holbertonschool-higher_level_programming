$(document).ready(function () {
    const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";
    $.get(apiUrl, function (data) {
      var characterName = data.name;
      $("#character").text(characterName);
    });
  });