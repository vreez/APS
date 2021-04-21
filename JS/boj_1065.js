const fs = require('fs');

// 공백으로 구분된 input값을 불러온다.
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const input = fs.readFileSync('1065.txt').toString();
console.log(input)

var count = 0
for (var i = 1; i < parseInt(input)+1; i++ ) {
  var number = i.toString().split('')
  console.log(number)
  for (var j = 0; j < number.length-1; j++) {
    var isit = 0;
    var minus = parseInt(number[i])-parseInt(number[i+1]);
    console.log(number)
    console.log(number.length)
    if (number.length < 3) {
      count += 1
    } else if ( minus === parseInt(number[i])-parseInt(number[i+1])) {
      isit += 1
    }
  };
  if (isit === number.length-1) {
    count += 1
  }
}

console.log(count)