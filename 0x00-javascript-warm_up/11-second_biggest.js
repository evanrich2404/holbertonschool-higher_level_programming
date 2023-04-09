#!/usr/bin/node
// prints the second biggest integer in the list of arguments
const myArgs = require('process');
if (myArgs.argv.length <= 3) {
  console.log(0);
} else {
  const sortedArgs = myArgs.argv.slice(2).sort((a, b) => a - b);
  console.log(sortedArgs[sortedArgs.length - 2]);
}
