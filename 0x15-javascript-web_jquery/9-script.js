$("document").ready(function () {
  $.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    method: "GET",
    dataType: "json",
    success: function(response) {
      $("#hello").append(response.hello)
    }
  });
});
