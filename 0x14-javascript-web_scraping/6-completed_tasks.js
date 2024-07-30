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

  try {
    data = JSON.parse(body);
  } catch (e) {
    console.log('Error parsing JSON:', e);
    process.exit(1);
  }

  if (!Array.isArray(data)) {
    console.log('Expected an array but received:', typeof data);
    process.exit(1);
  }

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
