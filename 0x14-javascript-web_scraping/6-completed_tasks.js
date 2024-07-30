#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.log('Bad Request');
    console.log('Status code', response.statusCode);
  }

  const data = JSON.parse(body);
  const completeTasks = {};

  data.forEach(task => {
    if (!(task.userId in completeTasks)) {
      completeTasks[task.userId] = 0;
    }
    if (task.completed) {
      completeTasks[task.userId] += 1;
    }
  });
  console.log(completeTasks);
});
