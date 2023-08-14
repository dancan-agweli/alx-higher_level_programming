#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const integers = [];
  for (let i = 2; i < process.argv.length; i++) {
    const parsedInt = parseInt(process.argv[i]);
    if (!isNaN(parsedInt)) {
      integers.push(parsedInt);
    }
  }

  if (integers.length < 2) {
    console.log('At least 2 valid integers are required.');
  } else {
    integers.sort((a, b) => b - a);
    console.log('Second largest integer:', integers[1]);
  }
}

