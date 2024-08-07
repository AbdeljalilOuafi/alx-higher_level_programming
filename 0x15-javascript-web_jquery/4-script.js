$("document").ready(function () {
  $("#toggle_header").click(function () {
    if ($("header").hasClass('green')) {
      $("header").removeClass('green').addClass('red');
    }
    else if ($("header").hasClass('red')) {
      $("header").removeClass('red').addClass('green');
    }
  });
});
