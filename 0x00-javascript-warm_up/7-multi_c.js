#!/usr/bin/node
// prints x times “C is fun”
const myArgs = require('process');
if (isNaN(myArgs.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < myArgs.argv[2]; x++) {
    console.log('C is fun');
  }
}
