#!/usr/bin/node
const x = Number(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let square;
  for (let i = 0; i < x; i++) {
    square = '';
    for (let j = 0; j < x; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
