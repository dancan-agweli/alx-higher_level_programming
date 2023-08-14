#!/usr/bin/node

const printXt = parseInt(process.argv[2]);

if (isNaN(printXt) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < printXt; i++) {
    console.log('C is fun');
  }
}

