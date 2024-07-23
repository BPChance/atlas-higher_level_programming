#!/usr/bin/node
const lines = [
    `C is fun`,
    `Python is cool`,
    `JavaScript is amazing`
];
let result = ``;
for (const line of lines) {
    result += line + '\n';
}

console.log(result.trim());
