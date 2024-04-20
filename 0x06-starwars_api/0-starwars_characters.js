#!/usr/bin/node
const request = require('request');

function getCharacters(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

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
    printCharactersInOrder(characters);
  });
}

function printCharactersInOrder(characters) {
  characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (characterError, characterResponse, characterBody) => {
      if (characterError || characterResponse.statusCode !== 200) {
        console.error(`Error fetching character data from ${characterUrl}:`, characterError || 'Invalid response');
      } else {
        console.log(characterBody.name);
      }
    });
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as a command line argument.');
  process.exit(1);
}

getCharacters(movieId);
