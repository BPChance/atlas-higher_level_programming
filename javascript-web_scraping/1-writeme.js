#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if(err) {
    console.error('Error writing to file', 'utf-8', err);
  } else {
    console.log('File written successfully');
  }
});
