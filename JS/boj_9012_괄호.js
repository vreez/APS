const fs = require('fs');

// 공백으로 구분된 input값을 불러온다.
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');
// 전개연산자를 사용하여 T와 괄호를 구분한다.
const [T, ...arr] = fs.readFileSync('9012.txt').toString().split('\r\n');

for (i = 0; i < T; i++) {
  const list = arr[i].split('')
  // list.push(arr[i].split(''))
  const stack = [];
  var answer = true;
  // const box = list;
  for (j = 0; j < list.length; j++) {
    if (list[j] === '(') {
      stack.push(list[j])
      // box.splice(list[j], 1)
    } else if(stack.length > 0 && list[j] === ')') {
      stack.pop()
      // box.splice(list[j], 1)
    } else if (stack.length === 0 && list[j] === ')') {
      var answer = false;
      break
    }
  };
  if (stack.length > 0 || answer === false) {
    console.log('NO')
  } else {
    console.log('YES')
  };
}