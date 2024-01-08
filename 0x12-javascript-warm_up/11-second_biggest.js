#!/usr/bin/node

const { argv } = require('process');
const args = argv.slice(2);
let bgsecend = 0;
let arr = [];

if (args.length > 1) {
  arr = [...new Set(args.map((e) => parseInt(e)).sort((a, b) => b - a))];
  bgsecend = arr.length > 1 ? arr[1] : arr[0];
}

console.log(bgsecend);
