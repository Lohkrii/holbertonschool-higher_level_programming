#!/usr/bin/nodejs
const args = process.argv.slice(2);
let x = 0;
if (!(args.length <= 1)) {
  args.sort();
  x = args[args.length - 2];
}
console.log(x);
