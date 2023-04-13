#!/usr/bin/node
// script that writes a string to a file
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Incorrect number of arguments');
} else {
  const file = process.argv[2];
  const content = process.argv[3];

  fs.writeFile(file, content, 'utf8', (error) => {
    if (error) {
      console.error(` An error occurred while writing the file: ${error}`);
    }
  });
}
