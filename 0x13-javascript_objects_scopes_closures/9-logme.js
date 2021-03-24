#!/usr/bin/nodejs
let argCount = 0;
exports.logMe = function (item) {
  console.log('%d: %s', argCount, item);
  argCount++;
}
