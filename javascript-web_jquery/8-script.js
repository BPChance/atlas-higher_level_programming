$(document).ready(function() {
  $.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
    const moviesList = $('#list_movies');
    $.each(data.results, function(index, movie) {
      const listItem = $('<li></li>');
      listItem.text(movie.title);
      moviesList.append(listItem);
    });
  });
});
