#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

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

  for (const userId in completedTasksByUser) {
    if (completedTasksByUser[userId] > 0) {
      console.log(`User ID ${userId} has ${completedTasksByUser[userId]} completed tasks.`);
    }
  }
});
