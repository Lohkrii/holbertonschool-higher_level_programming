#!/usr/bin/nodejs
let arg_count = process.argv.length;
if (arg_count <= 2) {
	console.log('No argument');
} else if (arg_count == 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
