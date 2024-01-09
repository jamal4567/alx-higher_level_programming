#!/usr/bin/node

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let character = '';
      for (let j = 0; j < this.width; j++) {
        character += c;
      }
      console.log(character);
    }
  }
}
module.exports = Square;
