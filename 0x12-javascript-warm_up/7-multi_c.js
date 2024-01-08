#!/usr/bin/node

const arg = process.argv[2];

if (arg) {
  for (let x = 0; x < arg; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
