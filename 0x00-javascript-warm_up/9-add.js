#!/usr/bin/node
// prints the addition of 2 integers
const myArgs = require('process');
if (isNaN(myArgs.argv[2]) || isNaN(myArgs.argv[3])) {
  console.log('NaN');
} else {
  console.log(parseInt(myArgs.argv[2]) + parseInt(myArgs.argv[3]));
}
