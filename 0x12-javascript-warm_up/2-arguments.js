#!/usr/bin/node

const args = process.argv;
const lengthOfArgs = args.length - 2;

if (!lengthOfArgs) {
  console.log('No argument');
} else if (lengthOfArgs === 1) {
  console.log('Argument found');
} else if (lengthOfArgs > 1) {
  console.log('Arguments found');
}
