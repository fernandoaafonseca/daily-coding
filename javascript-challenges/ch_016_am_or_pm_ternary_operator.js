/*
Given a clock that measures 24 hours a day, and a program that takes the hour as input.

Task:
Complete the program to output "am" to the console if the hour is in the range of 0 to 12 (inclusive), and output "pm" if it's not.

Sample input:
13
Sample output:
pm
*/

function amOrPm(hour) {
  return (hour <= 12) ? 'am' : 'pm'
}

console.log(amOrPm(7) === 'am');
console.log(amOrPm(12) === 'am');
console.log(amOrPm(13) === 'pm');
