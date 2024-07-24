#!/usr/bin/node

const Square = require('./5-square');

class SquareExtend extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const char = c || 'X';
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log(char.repeat(this.width));
      }
    }
  }
}

module.exports = SquareExtend;
