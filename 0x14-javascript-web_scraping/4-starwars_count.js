#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let characterCount = 0;

request(starWarsUri, function (error, response, body) {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  try {
    const data = JSON.parse(body);

    // Ensure the response structure matches expectations
    if (!Array.isArray(data.results)) {
      console.error('Unexpected response structure');
      return;
    }

    // Loop through films
    data.results.forEach((film) => {
      if (Array.isArray(film.characters)) {
        // Check for character ID '18' (Assuming '18' represents the character you want)
        const characterIds = film.characters.map((characterUrl) => characterUrl.split('/').pop());
        if (characterIds.includes('18')) {
          characterCount += 1;
        }
      }
    });

    console.log(`Character ID '18' appears in ${characterCount} films.`);
  } catch (e) {
    console.error('Error parsing JSON response:', e.message);
  }
});

