#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
if (!url) {
  console.error('Please provide a episode number as a command-line argument.');
  process.exit(1);
}

request(url, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
    return;
  }

  const moveId = body.split('people/18/').length - 1;
  console.log(moveId);
});
