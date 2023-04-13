#!/usr/bin/node
// script that display the status code of a GET request
const request = require('request');

if (process.argv.length < 3) {
  console.error('Incorrect number of arguments');
} else {
  const url = process.argv[2];
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(` An error occurred while requesting the url: ${error}`);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}
