#!/usr/bin/node
const request = require('request');

function getCharacters(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  // Make a GET request to the Star Wars API films endpoint
  request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching data from Star Wars API:', error.message);
      return;
    }

    if (response.statusCode !== 200 || !body.characters || body.characters.length === 0) {
      console.error('Invalid Movie ID or no characters found for the provided Movie ID.');
      return;
    }

    const characters = body.characters;
    printCharactersInOrder(characters, 0);
  });
}

function printCharactersInOrder(characters, index) {
  if (index >= characters.length) {
    return;
  }

  const characterUrl = characters[index];

  // Make a request for the character
  request(characterUrl, { json: true }, (characterError, characterResponse, characterBody) => {
    if (characterError || characterResponse.statusCode !== 200) {
      console.error(`Error fetching character data from ${characterUrl}:`, characterError || 'Invalid response');
    } else {
      console.log(characterBody.name);
    }

    printCharactersInOrder(characters, index + 1);
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as a command line argument.');
  process.exit(1);
}

getCharacters(movieId);
