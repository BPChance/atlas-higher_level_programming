#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('Failed to retrieve data:', error);
    return;
  }
  const tasks = JSON.parse(body);
  const userTaskCount = {};

  tasks.forEach(task => {
    if (task.completed) {
      const userId = task.userId; if (!userTaskCount[userId]) {
        userTaskCount[userId] = 0;
      }
      userTaskCount[userId]++;
    }
  });
  console.log(userTaskCount);
});
