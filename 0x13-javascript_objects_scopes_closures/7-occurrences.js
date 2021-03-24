#!/usr/bin/nodejs
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let idx = 0; idx < list.length; idx++) {
    if (searchElement === list[idx]) {
      count++;
    }
  }
  return count;
}
