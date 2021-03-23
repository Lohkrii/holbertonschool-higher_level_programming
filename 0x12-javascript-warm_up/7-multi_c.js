#!/usr/bin/nodejs
const isInt = parseInt(process.argv[2]);
if (isNaN(isInt)) {
	console.log('Missing number of ocurrances');
} else {
	for (let idx = 1; idx <= isInt; idx++) {
		console.log('C is fun');
	}
}
