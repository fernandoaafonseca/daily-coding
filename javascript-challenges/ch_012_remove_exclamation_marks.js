/*
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
*/

function removeExclamationMarks(s) {
  // The "g" modifier is used to perform a global replacement, i.e. all occurrences of the pattern will be replaced.
  return s.replace(/!/g, '')
}

console.log(removeExclamationMarks('Hello world!') === 'Hello world')
console.log(removeExclamationMarks('Hello world!!!') === 'Hello world')
