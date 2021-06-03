function solution(n) {
  var answer = '';
  if (n <= 3) {
      answer = '124'[n-1]
      console.log(answer)
      return answer
  } else {
      // 나눗셈을 할 경우 몫을 정수로 변환시켜주기 위해 parseInt를 사용한다. 
      answer = solution(parseInt((n-1) / 3)) + '124'[(n-1) % 3]
      console.log(answer)
      return answer
  }
}