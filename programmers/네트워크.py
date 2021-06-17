from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    while 0 in visited:
        for i in range(n):
            if visited[i] == 0:
                queue = deque([i])
                visited[i] = True
                while queue:
                    v = queue.popleft()
                    for i in range(n):
                        if computers[v][i] == 1 and not visited[i]:
                            queue.append(i)
                            visited[i] = True
                answer += 1
    return answer