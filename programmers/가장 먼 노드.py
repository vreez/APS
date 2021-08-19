from collections import deque

def solution(n, edge):
    answer = 0
    visited = [0] * (n + 1)
    node = [[] for _ in range(n + 1)]
    # 연결된 노드의 정보를 node에 저장한다.
    for i in range(len(edge)):
        node[edge[i][0]].append(edge[i][1])
        node[edge[i][1]].append(edge[i][0])
    # 1번 노드부터 시작하므로 queue에 1을 저장한다.
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for i in node[v]:
            # 방문한 적이 없고, i가 1이 아닐 경우, queue에 해당 수를 저장하고 방문 표시를 한다.
            if visited[i] == 0 and i != 1:
                queue.append(i)
                # 가장 먼 노드를 구해야 하므로 연결된 노드에 저장된 값보다 1을 더 더한다.
                visited[i] = visited[v] + 1
    # 가장 멀리 떨어진 노드의 길이를 maxNum에 저장한다.
    maxNum = max(visited)
    for item in visited:
        if item == maxNum:
            answer += 1
    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))