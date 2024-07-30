#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.log('Please provide the API URL as the first argument.');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;

  films.forEach((film) => {
    if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  });

  console.log(count);
});
