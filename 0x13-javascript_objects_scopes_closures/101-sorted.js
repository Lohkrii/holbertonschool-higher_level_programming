#!/usr/bin/nodejs
const dict = require('./101-data').dict;
const myDict = {};
for (let key in dict) {
  if (dict[key] in myDict) {
    myDict[dict[key]].push(key);
  } else {
    myDict[dict[key]] = [key];
  }
}
console.log(myDict);
