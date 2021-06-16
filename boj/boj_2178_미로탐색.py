import sys; sys.stdin = open("2178.txt", "r")
from collections import deque

N, M = map(int, input().split())
arr = list(input() for _ in range(N))

visited = [[0] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '1' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
    return visited[N-1][M-1]

print(bfs(0, 0))