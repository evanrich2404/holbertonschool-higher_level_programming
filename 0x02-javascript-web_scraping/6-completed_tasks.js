#!/usr/bin/node
// script that computes the number of tasks completed by user id
const request = require('request');

if (process.argv.length < 3) {
  console.error('Incorrect number of arguments');
} else {
  const url = process.argv[2];
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(` An error occurred while requesting the url: ${error}`);
    } else {
      const tasks = JSON.parse(body);
      const completedTasks = {};
      for (const task of tasks) {
        if (task.completed) {
          if (completedTasks[task.userId]) {
            completedTasks[task.userId]++;
          } else {
            completedTasks[task.userId] = 1;
          }
        }
      }
      console.log(completedTasks);
    }
  });
}
