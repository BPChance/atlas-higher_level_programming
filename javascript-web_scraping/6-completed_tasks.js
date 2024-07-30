#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

function getCompletedTasks(apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Failed to retrieve data:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Failed to retrieve data: HTTP status', response.statusCode);
      return;
    }
    
    
    const tasks = JSON.parse(body);
    const userTaskCount = {};

  tasks.forEach(task => {
    if (task.completed) {
      const userId = task.userId;
      if (!userTaskCount[userId]) {
        userTaskCount[userId] = 0;
    }
    userTaskCount[userId]++;
}
});

  for (const userId in userTaskCount) {
    if (userTaskCount[userId] > 0) {
      console.log(`User ID: ${userId} - Completed Tasks: ${userTaskCount[userId]}`);
    }
}
});
}

getCompletedTasks(apiUrl);
