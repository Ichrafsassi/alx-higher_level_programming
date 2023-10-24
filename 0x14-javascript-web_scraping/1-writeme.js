#!/usr/bin/node
// write data in a file from arg
const fs = require('fs');

if (process.argv.length > 3) {
  fs.writeFile(process.argv[2], process.argv[3], (error) => {
    if (error) console.log(error);
  });
}
