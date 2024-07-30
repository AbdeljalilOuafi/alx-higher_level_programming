#!/usr/bin/node

const url = process.argv[2];
const filename = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, function (error, repsonse, body) {
  if (error) {
    console.log(error);
  }
  const data = body;
  fs.writeFile(filename, data, { encoding: 'utf-8' }, function (err) {
    if (err) {
      console.log(err);
      process.exit(1);
    }
  });
});
