#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');

if (process.argv.length < 3) {
  console.error('Incorrect number of arguments');
} else {
  const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(` An error occurred while requesting the url: ${error}`);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
}
