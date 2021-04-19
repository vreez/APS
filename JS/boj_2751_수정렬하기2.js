const fs = require('fs');

// 공백으로 구분된 input값을 불러온다.
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const input = fs.readFileSync('2751.txt').toString().split('\n');
// shift()는 배열의 맨 앞의 값을 제거한다.

console.log(input)

const N = input.shift()

console.log(N)

function quicksort(input) {
  if (input.length < 2) {
    return input
  }
  else {
    const selected = input[0]
    const less = []
    const greater = []
    for (i = 1; i < N; i++) {
      if (input[i] <= selected) {
        less.push(input[i])
      }
      else {
        greater.push(input[i])
      }
    }
    return quicksort(less).concat(selected, quicksort(greater))
  }
}

console.log(quicksort(input))

