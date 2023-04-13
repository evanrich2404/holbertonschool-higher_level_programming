#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Incorrect number of arguments');
} else {
  const url = process.argv[2];
  const file = process.argv[3];

  request.get(url, (error, response, body) => {
    if (error) {
      console.error(` An error occurred while requesting the url: ${error}`);
    }

    fs.writeFile(file, body, 'utf8', (error) => {
      if (error) {
        console.error(` An error occurred while writing the file: ${error}`);
      }
    });
  });
}
