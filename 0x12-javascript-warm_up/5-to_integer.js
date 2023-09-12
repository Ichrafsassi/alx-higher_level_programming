#!/usr/bin/node
// Mynumber: <first argument converted in integer>

const Mynumber = Number(process.argv[2]);
console.log(isNaN(Mynumber) ? 'Not a number' : 'My number: ' + Mynumber);
