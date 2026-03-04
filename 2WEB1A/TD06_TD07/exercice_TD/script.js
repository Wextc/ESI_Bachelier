"use strict";

const array = [24, 10, 8, 4, 2, 1, 3, 7, 9, 23, 31];
let resultat = [];
const inversePair = (param) => {
  for (let i = param.length; i > 0; i--) {
    if (param[i] % 2 == 0) {
      resultat.push(param[i]);
    }

    return resultat;
  }
};
console.log(inversePair(array));
