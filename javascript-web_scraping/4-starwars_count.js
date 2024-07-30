#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.hbtn.io/api/films/';
const characterID = 18;

let totalCount = 0;

function countWedgeAppearances(url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const data = JSON.parse(body);
    const nextUrl = data.next;

    for (const film of data.results) {
      for (const characterUrl of film.characters) {
        if (characterUrl.endsWith(`/${characterID}/`)) {
          totalCount++;
          break;
        }
      }
    }

    if (nextUrl) {
      countWedgeAppearances(nextUrl);
    } else {
      console.log(totalCount);
    }
  });
}

countWedgeAppearances(baseUrl);
