#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, { json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.log('Bad Request');
    console.log('Status code', response.statusCode);
  }

  const completeTasks = {};

  body.forEach(task => {
    if (task.completed) {
      if (!completeTasks[task.userId]) {
        completeTasks[task.userId] = 0;
      }
      completeTasks[task.userId] += 1;
    }
  });
  console.log(completeTasks);
});
