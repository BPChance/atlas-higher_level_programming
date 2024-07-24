#!usr/bin/nodferfe
const Square = require('./5-square');

class SquareExtend extends Square {
    constructor(size) {
        super(size);
    }

    charPrint(c) {
        const char = c || 'X';
        if (this.size) {
            for (let i = 0; i < this.size; i++) {
                console.log(char.repeat(this.size));
            }
        }
    }
}

module.exports = SquareExtend;
