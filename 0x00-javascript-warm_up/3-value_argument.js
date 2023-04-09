#!/usr/bin/node
// prints the first argument passed to it
const myArgs = require('process');

if (myArgs.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(myArgs.argv[2]);
}
