function solution(n, computers) {
  var answer = 0;
  // 각 컴퓨터의 방문 여부를 표시할 visited 배열을 생성한다.
  let visited = [];
  // 방문하지 않은 경우를 0, 방문한 경우를 1로 표시할 예정이므로,
  // for문을 돌며 n의 개수만큼 0을 더한다.
  for (let i = 0; i < n; i++) {
      visited.push(0)
  }
  // 모든 컴퓨터를 하나씩 살펴본다.
  for (let i = 0; i < n; i++) {
      // 아직 해당 컴퓨터를 방문하지 않았을 경우
      if (visited[i] === 0) {
          // 해당 컴퓨터의 index를 queue에 집어 넣고, 방문 표시를 한다.
          let queue = [i]
          visited[i] = 1
          // 해당 컴퓨터와 연결되어 있는 모든 컴퓨터가 있는지 확인하기 위해
          // queue가 빌때 까지 while문을 사용해 검사한다.
          while (queue.length > 0) {
              // queue의 가장 앞에 위치한 요소를 빼서 v라는 변수에 담는다.
              let v = queue.shift()
              for (let j = 0; j < n; j++) {
                  // v와 연결되어 있고, 아직 방문하지 않은 컴퓨터가 있으면
                  // queue에 넣고, 방문 표시를 한다.
                  if (computers[v][j] === 1 && visited[j] !== 1) {
                      queue.push(j)
                      visited[j] = 1
                  }
              }
          }
          // 하나의 컴퓨터와 연결되어 있는 컴퓨터를 모두 확인했으면 
          // 연결된 하나의 네트워크가 존재한다는 의미이므로 
          // answer에 1을 더한다.
          answer++
      }
  }
  
  return answer;
}