function convertCtoF(celsius) {
  let fahrenheit = celsius * 9 / 5 + 32;
  return fahrenheit;
}

function testAnswer(value, expected) {
  result = convertCtoF(value);
  if (result == expected) {
    console.log('Right!');
  } else {
    console.log('Wrong!')
  }
}

testAnswer(-30, -22);
testAnswer(30, 86);
testAnswer(0, 32);
testAnswer(20, 68);
