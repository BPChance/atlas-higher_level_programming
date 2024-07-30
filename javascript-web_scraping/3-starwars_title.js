#!/usr/bin/node
const request = require('request');
const episodeNumber = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/${episodeNumber}';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error', error);
    return;
  }
  const data = JSON.parse(body);

  if (!data.title) {
    console.error('Movie not found');
    return;
  }

  console.log(data.title);
});
