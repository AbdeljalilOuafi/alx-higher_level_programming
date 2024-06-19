#!/usr/bin/node

function factorialRecursive (n) {
  if (n < 0) return undefined;
  if (n === 0 || isNaN(n)) return 1;
  return n * factorialRecursive(n - 1);
}

const argv = process.argv.slice(2);
const n = argv[0];
console.log(factorialRecursive(Number(n)));
