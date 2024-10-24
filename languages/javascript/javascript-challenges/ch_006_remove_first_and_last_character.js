/*
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
*/

function removeChar(str) {
  strArray = str.split('');
  lastChar = strArray.length - 1;
  newStrArray = strArray.slice(1, lastChar);
  finalStr = newStrArray.join('');
  return finalStr;
};

console.log(removeChar('eloquent') === 'loquen');
console.log(removeChar('country') === 'ountr');
console.log(removeChar('person') === 'erso');
console.log(removeChar('place') === 'lac');
console.log(removeChar('ooopsss') === 'oopss');
