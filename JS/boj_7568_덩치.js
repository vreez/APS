const fs = require('fs');

// 공백으로 구분된 input값을 불러온다.
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const input = fs.readFileSync('7568.txt').toString().split('\r\n');

const N = input.shift();

const check = [] 
for (const i in input) {
  const info = input[i].split(' ')
  check.push(info)
};

var arr = []
for (var j = 0; j < parseInt(N); j++) {
  arr.push(parseInt(1))
};


for (const a in check) {
  for (const b in check) {
    if (a !== b) {
      if (check[a][0] < check[b][0] && check[a][1] < check[b][1]) {
        arr[a] += 1
      } 
    }
  }
};

var result = "";

for (const c in arr) {
  result = result + (arr[c] +' ')
}

console.log(result)