#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log(
      ('X'.repeat(this.width) + '\n').repeat(this.height).slice(0, -1)
    );
  }
}

module.exports = Rectangle;
