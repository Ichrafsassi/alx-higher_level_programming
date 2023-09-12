#!/usr/bin/node
const scndBig = process.argv
  .slice(2)
  .map(Number)
  .sort((a, b) => b - a)[1];
console.log(scndBig === undefined ? 0 : scndBig);
