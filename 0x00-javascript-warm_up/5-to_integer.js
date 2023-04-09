#!/usr/bin/node
// prints “My number: ” if the first argument can be converted to an integer
const myArgs = require('process');
if (isNaN(myArgs.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArgs.argv[2]);
}
