#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body);
  
  if (body.title) {
    console.log(`Film Title: ${body.title}`);
  } else {
    console.error('Film title not found in the API response.');
  }
});

