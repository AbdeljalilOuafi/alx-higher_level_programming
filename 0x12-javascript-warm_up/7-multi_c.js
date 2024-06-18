#!/usr/bin/node

const argv = process.argv.slice(2);
const number = argv[0];
const convertedNumber = Number(number);
if (!isNaN(convertedNumber)) {
  for (let i = 0; i < convertedNumber; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
