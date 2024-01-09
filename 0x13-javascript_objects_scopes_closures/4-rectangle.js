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

  rotate () {
    let tem = 0;
    tem = this.width;
    this.width = this.height;
    this.height = tem;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
