// updates the text color of the header to red (#FF0000) when the user clicks on the tag DIV#red_header
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
