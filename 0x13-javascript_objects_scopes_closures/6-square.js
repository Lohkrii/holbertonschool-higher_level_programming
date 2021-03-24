#!/usr/bin/nodejs
const iSquare = require('./5-square');
class Square extends iSquare {
  constructor (area) {
    super(area, area);
  }

  charPrint(c = 'X') {
    for (let idx = 0; idx < this.height; idx++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
