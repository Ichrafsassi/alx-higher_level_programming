#!/usr/bin/node

const dict = require('./101-data.js').dict;
const new_sortdic = {};

for (const key in dict) {
  if (new_sortdic[dict[key]] === undefined) {
    new_sortdic[dict[key]] = [key];
  } else {
    new_sortdic[dict[key]].push(key);
  }
}
console.log(new_sortdic);
