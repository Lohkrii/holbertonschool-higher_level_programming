#!/usr/bin/nodejs
const ifNum = parseInt(process.argv[2], 10);
if (isNaN(ifNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${ifNum}`);
}
