#!/usr/bin/node

function add (a, b) {
  console.log(Number(a) + Number(b));
}

const argv = process.argv.slice(2);
const a = argv[0];
const b = argv[1];
add(a, b);
