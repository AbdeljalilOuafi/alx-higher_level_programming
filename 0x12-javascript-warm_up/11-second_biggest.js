#!/usr/bin/node

const argv = process.argv.slice(2);
if (argv.length === 0) {
  console.log(0);
} else if (argv.length === 1) {
  console.log(1);
} else {
  argv.sort((a, b) => b - a);
  console.log(argv[1]);
}
