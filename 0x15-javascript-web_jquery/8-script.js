$(document).ready(function () {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    dataType: "json",
    success: function(response) {
      if (response.results && Array.isArray(response.results)) {
        response.results.forEach(function (movie) {
          $("#list_movies").append("<li>" + movie.title + "</li>");
        });
      } else {
        console.log("Unexpected response structure:", response);
      }
    },
    error: function(error) {
      console.log("Error fetching data:", error);
    }
  });
});
