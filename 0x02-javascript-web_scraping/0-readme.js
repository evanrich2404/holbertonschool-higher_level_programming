#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Cannot find file');
} else {
  const file = process.argv[2];

  fs.readFile(file, 'utf8', (error, data) => {
    if (error) {
      console.error(` An error occurred while reading the file: ${error}`);
      return;
    }
    console.log(data);
  });
}
