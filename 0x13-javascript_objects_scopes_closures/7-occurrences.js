#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0; let occurences = 0;
  for (i; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurences++;
    }
  }
  return occurences;
};
