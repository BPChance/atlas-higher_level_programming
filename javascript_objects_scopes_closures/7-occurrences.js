#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let totalOccurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      totalOccurences++;
    }
  }
  return totalOccurences;
};
