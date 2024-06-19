#!/usr/bin/node

const oldSquare = require('./5-square');

class Square extends oldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let character = c;
    if (c === undefined) {
      character = 'X';
    }

    let i; let j; let string = '';
    for (j = 0; j < this.width; j++) {
      string += character;
    }
    for (i = 0; i < this.height; i++) {
      console.log(string);
    }
  }
}

module.exports = Square;
