#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((value, indx) => value * indx);
console.log(list);
console.log(newList);
