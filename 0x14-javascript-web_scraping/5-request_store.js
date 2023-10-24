#!/usr/bin/node
// write data in a file from web
const fs = require('fs');
const request = require('request');

if (process.argv.length > 3) {
  request.get(process.argv[2], (error, resopnse, body) => {
    if (error) console.log(error);
    else {
      fs.writeFile(process.argv[3], body, 'utf8', (error) => {
        if (error) console.log(error);
      });
    }
  });
}
