#!/usr/bin/nodejs
exports.esrever = function (list) {
  const newArr = [];
  for (let idx = list.length; idx--;) {
    newArr.push(list[idx]);
  }
  return newArr;
};
