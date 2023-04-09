#!/usr/bin/node
// prints a square
const myArgs = require('process');
if (isNaN(myArgs.argv[2])) {
  console.log('Missing size');
} else {
  for (let x = 0; x < myArgs.argv[2]; x++) {
    console.log('X'.repeat(myArgs.argv[2]));
  }
}
