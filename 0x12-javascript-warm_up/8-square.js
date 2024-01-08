#!/usr/bin/node

const arg = process.argv[2];

if (parseInt(arg)) {
  for (let x = 0; x < arg; x++) {
    let text = '';
    for (let i = 0; i < arg; i++) {
      text = text + 'X';
    }
    console.log(text);
  }
} else {
  console.log('Missing size');
}
