#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let r = 0;
  list.map((i) => (searchElement === i ? r++ : r));
  return r;
};
