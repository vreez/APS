import sys; sys.stdin = open("input/2178.txt", "r")
from collections import deque

N, M = map(int, input().split())
arr = list(list(input()) for _ in range(N))
visit = [[0] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < N and 0 <= newY < M and arr[newX][newY] == '1' and visit[newX][newY] == 0:
                visit[newX][newY] = visit[x][y] + 1
                queue.append([newX, newY])

    return visit[N-1][M-1] + 1

print(bfs(0, 0))