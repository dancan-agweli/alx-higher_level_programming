#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let pstr = 'X'.repeat(size);
  while (size > 0) {
    console.log(pstr);
    size--;
  }
}

