#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(arg => parseInt(arg, 10));

if (numbers.length === 0 || numbers.length === 1) {
    console.log(0);
} else {
    const uniqueNumbers = [...new Set(numbers)];
    uniqueNumbers.sort((a, b) => b - a);
    
    console.log(uniqueNumbers[1] !== undefined ? uniqueNumbers[1] : 0);
}
