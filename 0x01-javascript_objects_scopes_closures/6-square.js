#!/usr/bin/node
// creating class Square that defines a square and inherits from Square of 5-square.js
const SquareBase = require('./5-square');
module.exports = class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
