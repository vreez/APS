var fs = require("fs")

var input = fs.readFileSync("/dev/stdin").toString()

for (i = 1; i < 10; i++) {
  const N = parseInt(input)
  console.log(N + " * " + i + " = " + N * i  )
}