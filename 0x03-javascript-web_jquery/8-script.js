// fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $.each(data.results, function (index, value) {
      $('UL#list_movies').append('<li>' + value.title + '</li>');
    });
  });
});
