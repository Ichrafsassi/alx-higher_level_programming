#!/usr/bin/node
// get request
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (!error) console.log('code:', response.statusCode);
});
