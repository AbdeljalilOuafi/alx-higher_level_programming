#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');
const pattern = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(result => {
      count += result.characters.filter(url => url === pattern).length;
    });
    console.log(count);
  }
});
