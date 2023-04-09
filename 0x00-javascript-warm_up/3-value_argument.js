#!/usr/bin/node
// prints the first argument passed to it
const myArgs = process.argv.slice(2);
let firstArgFound = false;

for (const arg of myArgs) {
  if (!firstArgFound) {
    console.log(arg);
    firstArgFound = true;
  }
  break;
}

if (!firstArgFound) {
  console.log('No argument');
}
