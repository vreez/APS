const fs = require("fs")

const input = fs.readFileSync("/dev/stdin").toString()
const result = input.split(' ');

console.log(parseInt(result[0]) + parseInt(result[1]))