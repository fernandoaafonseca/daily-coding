function reverseString(str) {
  let reversedStr = str.split('').reverse().join('');
  return reversedStr;
}

function testAnswer(str, expected) {
  let result = reverseString(str);
  if (result == expected) {
    console.log('Right!');
  } else {
    console.log('Wrong!')
  }
}

testAnswer('hello', 'olleh');
testAnswer('Howdy', 'ydwoH');
testAnswer('Greetings from Earth', 'htraE morf sgniteerG');
