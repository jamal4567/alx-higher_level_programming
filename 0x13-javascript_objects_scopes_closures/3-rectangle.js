#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method
  print () {
    for (let i = 0; i < this.height; i++) {
      let character = '';
      for (let j = 0; j < this.width; j++) {
        character += 'X';
      }
      console.log(character);
    }
  }
}
module.exports = Rectangle;
