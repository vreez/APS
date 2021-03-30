const fs = require('fs');

// 공백으로 구분된 input값을 불러온다.
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
// 로컬
// const input = fs.readFileSync('10773.txt').toString().split('\n');

// shift()는 배열의 맨 앞의 값을 제거한다.
N = input.shift();

const arr = [];
for (var i = 0; i < N; i++) {
  if (input[i] === '0' || input[i] === '0\r') {
    arr.pop()
  }
  else {
    arr.push(input[i])
  }
};

var result = 0
if (arr.length > 0) {
  for (var i = 0; i < arr.length; i++) {
    result += parseInt(arr[i])
  }
} else {
  result = 0
}

console.log(result)

