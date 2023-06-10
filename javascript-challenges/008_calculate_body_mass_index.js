/*
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"
*/

function bmi(weight, height) {
  let bmi = weight / height ** 2;
  switch (true) {
    case bmi <= 18.5:
      return 'Underweight';
    case bmi <= 25.0:
      return 'Normal';
    case bmi <= 30.0:
      return 'Overweight';
    case bmi > 30:
      return 'Obese';
  }
}

console.log(bmi(50, 1.70) === 'Underweight');
console.log(bmi(80, 1.80) === 'Normal');
console.log(bmi(75, 1.65) === 'Overweight');
console.log(bmi(120, 1.77) === 'Obese');
