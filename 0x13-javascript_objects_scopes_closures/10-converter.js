#!/usr/bin/nodejs
exports.converter = function (base) {
  return function (idx) {
    return idx.toString(base);
  };
}
