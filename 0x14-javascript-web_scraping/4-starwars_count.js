#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  const moveId = body.split('people/18/').length - 1;
  console.log(moveId);
});
