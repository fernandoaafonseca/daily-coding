/*
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
*/

function removeExclamationMarks(s) {
  // O modificador "g" é usado para realizar uma substituição global, ou seja, todas as ocorrências do padrão serão substituídas.
  return s.replace(/!/g, '')
}

console.log(removeExclamationMarks('Hello world!') === 'Hello world')
console.log(removeExclamationMarks('Hello world!!!') === 'Hello world')
