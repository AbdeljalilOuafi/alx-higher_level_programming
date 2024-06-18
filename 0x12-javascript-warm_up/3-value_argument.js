#!/usr/bin/node

const args = process.argv.slice(2);
let lengthOfArgs = 0;
for (let i = 0; i < args.length; i++) {
  lengthOfArgs += 1;
}

if (!lengthOfArgs) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
