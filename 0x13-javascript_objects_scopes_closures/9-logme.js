#!/usr/bin/node

let n = -1;
exports.logMe = function (item) {
  n++;
  console.log(n + ': ' + item);
};
