/*
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]
*/

function digitize(n) {
  let nString = String(n).split('').reverse().join('');
  let nReversedArray = Array.from(nString, Number);
  return nReversedArray;
}

console.log(digitize(35231).toString() == [1, 3, 2, 5, 3].toString());
console.log(digitize(0).toString() == [0].toString());
