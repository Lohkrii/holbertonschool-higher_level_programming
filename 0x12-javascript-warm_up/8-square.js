#!/usr/bin/nodejs
const isInt = parseInt(process.argv[2]);
if (isNaN(isInt)) {
  console.log('Missing size');
} else {
  for (let idx = 1; idx <= isInt; idx++) {
    for (let cidx = 1; cidx <= isInt; cidx++) {
      process.stdout.write('x');
    }
    process.stdout.write('\n');
  }
}
