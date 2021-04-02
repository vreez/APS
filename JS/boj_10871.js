const fs = require('fs');

// 공백으로 구분된 input값을 불러온다.
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const input = fs.readFileSync('10871.txt').toString().split('\n');
const arr = input[0].split(' ')
const N = arr.shift()
const X = arr[0]


const Numbers = input[1].split(' ');

var result = ''
for (var i = 0; i < parseInt(N); i++) {
  if (Numbers[i] < parseInt(X)) {
    result += Numbers[i] + ' '
  }
}

console.log(result)
