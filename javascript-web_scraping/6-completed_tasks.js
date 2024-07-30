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

  const result = {};
  for (let i = 1; i <= 10; i++) {
    result[i] = completedTasksByUser[i] || 0;
  }

  let output = '';
  for (let i = 1; i <= 10; i++) {
    output += `  '${i}': ${result[i]},\n`;
  }
  output = output.slice(0, -2);
  console.log(`{\n${output}\n}`);
});
