#!/usr/bin/nodejs
const list = require('./100-data').list;
let idx = 0;
const nList = list.map(x => x * idx++);
console.log(list);
console.log(nList);
