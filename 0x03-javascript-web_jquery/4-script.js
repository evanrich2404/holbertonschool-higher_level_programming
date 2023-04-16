// toggles the class of the header element when the user clicks on the tag DIV#toggle_header
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
