function solution(priorities, location) {
  // answer에는 출력 순서를 저장한다.
  var answer = 0;
  // 각 원소의 원래 index를 arr에 저장한다.     
  let arr = []
  for (let i = 0; i < priorities.length; i++) {
      arr.push(i)
  }
  while (priorities.length !== 0) {
      // 현재 priorities 가운데 최대값을 저장한다.
      let maxNum = Math.max(...priorities)
      if (priorities[0] < maxNum) {
          priorities.push(priorities.shift())
          arr.push(arr.shift())    
      } else {
          priorities.shift()
          answer += 1
          if (arr[0] === location) {
              break
          } else {
              arr.shift()
          }
      }
  }
  return answer;
}