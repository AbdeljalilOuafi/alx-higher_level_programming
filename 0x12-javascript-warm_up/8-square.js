#!/usr/bin/node

const argv = process.argv.slice(2);
const number = argv[0];
const convertedNumber = Number(number);
if (!isNaN(convertedNumber)) {
  for (let i = 0; i < convertedNumber; i++) {
    let string = '';
    for (let j = 0; j < convertedNumber; j++) {
      string += 'X';
    }
    console.log(string);
  }
} else {
  console.log('Missing size');
}
