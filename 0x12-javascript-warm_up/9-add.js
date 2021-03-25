#!/usr/bin/nodejs
const args = process.argv;
add(parseInt(args[2]), parseInt(args[3]));

function add (a, b) {
  console.log(a + b);
}
