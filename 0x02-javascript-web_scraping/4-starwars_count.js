#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');

if (process.argv.length < 3) {
  console.error('Incorrect number of arguments');
} else {
  const url = process.argv[2];
  const characterID = 18;

  request.get(url, (error, response, body) => {
    if (error) {
      console.error(` An error occurred while requesting the url: ${error}`);
    }

    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      let count = 0;

      films.forEach((film) => {
        if (film.characters.some((characterUrl) => characterUrl.includes(`/people/${characterID}/`))) {
          count += 1;
        }
      });

      console.log(count);
    } else {
      console.log('An error occurred while requesting the url');
    }
  });
}
