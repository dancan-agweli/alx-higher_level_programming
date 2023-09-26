#!/usr/bin/node

const request = require('request');

// Function to fetch data from a URL and return a Promise
function getDataFrom(url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

// Function to print character names
function printCharacterNames(characterUrls) {
  const promises = characterUrls.map((url) => getDataFrom(url));

  Promise.all(promises)
    .then((results) => {
      const characterNames = results.map((data) => JSON.parse(data).name);
      characterNames.forEach((name) => console.log(name));
    })
    .catch((err) => {
      console.error(err);
    });
}

// Main function to fetch movie data and call the printCharacterNames function
function printMovieCharacters(movieId) {
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  getDataFrom(movieUri)
    .then((data) => {
      const characters = JSON.parse(data).characters;
      printCharacterNames(characters);
    })
    .catch((err) => {
      console.error(err);
    });
}

// Call the main function with the movie ID from command-line arguments
const movieId = process.argv[2];
if (movieId) {
  printMovieCharacters(movieId);
} else {
  console.error('Please provide a movie ID as a command-line argument.');
}

