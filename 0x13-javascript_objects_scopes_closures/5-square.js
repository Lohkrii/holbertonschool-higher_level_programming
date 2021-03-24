#!/usr/bin/nodejs
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (area) {
    super (area, area);
  }
}

module.exports = Square;
