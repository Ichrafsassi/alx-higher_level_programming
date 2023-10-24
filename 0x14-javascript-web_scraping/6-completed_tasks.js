#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, resopnse, body) => {
  if (error) console.log(error);
  else {
    const completedTasks = {};
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed) {
        if (todo.userId in completedTasks) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
