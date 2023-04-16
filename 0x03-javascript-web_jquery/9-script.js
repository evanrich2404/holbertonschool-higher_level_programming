// fetches from https://stefanbohacek.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML’s tag DIV#hello
$(document).ready(function() {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', function(data) {
    const helloTranslation = $(data).find('#hello').text();
    $('#hello').text(helloTranslation);
  });
});
