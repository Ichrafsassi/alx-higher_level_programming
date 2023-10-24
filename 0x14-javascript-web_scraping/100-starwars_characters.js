#!/usr/bin/node
// get request
const request = require('request');
const movieId = process.argv[2];
if (!movieId) process.exit();

const filmsURL = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(filmsURL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const charactersInMovie = JSON.parse(body).characters;
    for (const char of charactersInMovie) {
      request.get(char, (error, response, body) => {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
