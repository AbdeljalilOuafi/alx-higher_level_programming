#!/usr/bin/node

const argv = process.argv.slice(2);
const number = argv[0];
const convertedNumber = Number(number);
if (!isNaN(convertedNumber)) {
  console.log('My number: ' + convertedNumber);
} else {
  console.log('Not a number');
}
