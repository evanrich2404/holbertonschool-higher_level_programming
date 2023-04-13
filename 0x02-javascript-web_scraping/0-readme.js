#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');

if (process.argv.length === 3) {
  fs.readFile(process.argv[2], 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
} else {
  console.log('Usage: ./0-readme.js filename');
};
