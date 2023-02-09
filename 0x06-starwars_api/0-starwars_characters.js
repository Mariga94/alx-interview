#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const starWarsAPI = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
if (movieId) {
  request(`${starWarsAPI}`, function (error, res, body) {
    if (error) {
      console.log('Error');
    } else {
      const bodyObj = JSON.parse(body);
      const charactersURL = bodyObj.characters;
      charactersURL.forEach(characterURL => {
        request(`${characterURL}`, function (body, res) {
          console.log(JSON.parse(res.body).name);
        });
      });
    }
  });
} else {
  console.log('Enter the correct index value');
}
