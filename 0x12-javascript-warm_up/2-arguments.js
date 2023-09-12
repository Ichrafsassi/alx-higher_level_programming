#!/usr/bin/node

console.log(
  process.argv[2] === undefined ? 'No argument' : process.argv[3] === undefined ? 'Argument found' : 'Arguments found'
);
