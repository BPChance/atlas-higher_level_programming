#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const data = JSON.parse(body);
  const completedTasksByUser = {};

  for (const todo of data) {
    const userId = todo.userId;

    if (todo.completed) {
      if (!completedTasksByUser[userId]) {
        completedTasksByUser[userId] = 0;
      }
      completedTasksByUser[userId]++;
    }
  }

  const filteredCompletedTasksByUser = {};
  for (const userId in completedTasksByUser) {
    if (userId === '1' || userId === '2') {
      filteredCompletedTasksByUser[userId] = completedTasksByUser[userId];
    }
  }

  console.log(JSON.stringify(filteredCompletedTasksByUser));
});
