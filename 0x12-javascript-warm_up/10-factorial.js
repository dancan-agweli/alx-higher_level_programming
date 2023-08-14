#!/usr/bin/node

function factorial(n) {
  return (n === 0 || isNaN(n)) ? 1 : n * factorial(n - 1);
}

const inputNumber = Number(process.argv[2]);

if (isNaN(inputNumber) || process.argv[2] === undefined) {
  console.log('Invalid input. Please provide a number.');
} else {
  console.log(`Factorial of ${inputNumber} is: ${factorial(inputNumber)}`);
}

