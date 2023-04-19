// fetches from https://stefanbohacek.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML’s tag DIV#hello
$(document).ready(function() {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    $('#hello').text(data.hello);
  });
});
