#!/usr/bin/node
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

const arg = process.argv[2];
const num = parseInt(arg, 10);

if (isNaN(num)) {
    console.log(1);
} else {
    console.log(factorial(num));
}
