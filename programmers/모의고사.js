function solution(answers) {
  var point = [0, 0, 0]
  const per1 = [1, 2, 3, 4, 5]
  const per2 = [2, 1, 2, 3, 2, 4, 2, 5]
  const per3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  for (var i = 0; i < answers.length; i++) {
      if (answers[i] === per1[i % 5]) {
          point[0] += 1
      } 
      if (answers[i] === per2[i % 8]) {
          point[1] += 1
      } 
      if (answers[i] === per3[i % 10]) {
          point[2] += 1
      }
  }
  // 전개연산자를 사용하면 객체나 배열의 원소들을 하나씩 펼쳐서 리턴하게 된다.
  var max = Math.max(...point)
  var answer = [];
  for (var j = 0; j < 3; j++) {
      if (point[j] === max) {
          answer.push(j+1)
      }
  }
  return answer;
}