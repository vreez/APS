const fs = require('fs');

// 공백으로 구분된 input값을 불러온다.
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const input = fs.readFileSync('2231.txt').toString();
var ans = 0;
// input값이 10 이하인 경우에는 무조건 0을 출력한다.
if (input > 10) {
  for (var i = 1; i < input; i++) {
    var total = i;
    var k = i;
    while (k !== 0) {
      total += k % 10;
      k = parseInt(k / 10);
    }
    if (total === parseInt(input)) {
      ans = i
      break
    }
  };
}
console.log(ans)

