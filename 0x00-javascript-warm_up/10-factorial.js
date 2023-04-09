#!/usr/bin/node
// prints the factorial of a number
const myArgs = require('process');
if (isNaN(myArgs.argv[2])) {
  console.log(1);
} else {
  console.log(factorial(myArgs.argv[2]));
} function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
