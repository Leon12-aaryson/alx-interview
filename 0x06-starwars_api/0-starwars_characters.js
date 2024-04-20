#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie
 * Usage: ./script_name.js <filmId>
 * Example: ./script_name.js 1
 */

// Import the 'request' module
const request = require('request');

// Retrieve the film ID from the command-line arguments
const filmId = process.argv[2];

// Check if the film ID is provided and is a valid number
if (!filmId || isNaN(filmId)) {
  console.error('Invalid film ID. Please provide a valid film ID as a command-line argument.');
  process.exit(1);
}

// Construct the URL for the Star Wars API based on the provided film ID
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

// Make a GET request to the Star Wars API to fetch information about the movie
request(url, (error, res, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  // Parse the JSON response
  const starWarsMovie = JSON.parse(body);

  // Extract the list of characters from the movie data
  const characters = starWarsMovie.characters;

  // Array to store promises for fetching character names
  const characterPromises = [];

  // Iterate over each character URL and create a promise for fetching its name
  characters.forEach(characterUrl => {
    // Create a promise for fetching the character's name
    const promise = new Promise((resolve, reject) => {
      // Make a GET request to fetch the character data
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        // Parse the JSON response
        const characterData = JSON.parse(body);

        // Resolve the promise with the character's name
        resolve(characterData.name);
      });
    });

    // Add the promise to the array
    characterPromises.push(promise);
  });

  // Wait for all promises to resolve
  Promise.all(characterPromises)
    .then(characterNames => {
      // Print the names of all characters
      console.log('Characters in the movie:');
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error fetching character data:', error);
    });
});
