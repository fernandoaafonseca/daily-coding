/*
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
*/

function grow(x) {
  let result = 1;
  for (let i = 0; i < x.length; i++) {
    result *= x[i];
  }
  return result;
}

console.log(grow([1, 2, 3]) === 6);
console.log(grow([4, 1, 1, 1, 4]) === 16);
console.log(grow([2, 2, 2, 2, 2, 2]) === 64); 
