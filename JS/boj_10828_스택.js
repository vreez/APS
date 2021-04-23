const fs = require('fs');

// 공백으로 구분된 input값을 불러온다.
// const input = fs.readFileSync('/dev/stdin').toString().split('\r\n');
// 전개연산자를 사용하여 T와 괄호를 구분한다.
const [T, ...arr] = fs.readFileSync('10828.txt').toString().split('\r\n');
// console.log(T)
// console.log(arr)

const stack = []
for (var i = 0; i < parseInt(T); i++) {
  const order = arr[i].split(' ')
  // console.log(order)
  if (order[0] === 'push') {
    stack.push(order[1])
  } else if (order[0] === 'pop') {
    if (stack.length > 0) {
      console.log(parseInt(stack[stack.length-1]))
      stack.pop()
    } else{
      console.log(-1)
    }
  } else if (order[0] === 'size') {
    console.log(parseInt(stack.length))
  } else if (order[0] === 'empty') {
    if (stack.length > 0) {
      console.log(0)
    } else {
      console.log(1)
    }
  } else if (order[0] === 'top') {
    if (stack.length > 0) {
      console.log(parseInt(stack[stack.length-1]))
    } else {
      console.log(-1)
    }
  }
}