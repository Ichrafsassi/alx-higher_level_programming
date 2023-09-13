#!/usr/bin/node

const dict = require('./101-data.js').dict;
const New_dict = {};

for (const [key, value] of Object.entries(dict)) {
  if (New_dict[value] === undefined) {
    New_dict[value] = [key];
  } else {
    New_dict[value].push(key);
  }
}

console.log(New_dict);
