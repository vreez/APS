import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = 0

def bfs(x, y):
    global ans
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0 <= newx < N and 0 <= newy < M:
                if arr[newx][newy] == 'L' and visit[newx][newy] == 0:
                    visit[newx][newy] = visit[x][y] + 1
                    Q.append([newx,newy]
                    ans = max(ans, visit[newx][newy])
    return

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(N)]

Q = deque()
for i in range(N):
    for j in range(M):
		# 매번 visit를 0으로 초기화시켜줄 필요가 있다.
        visit = [[0] * M for _ in range(N)]
        if arr[i][j] == 'L' and visit[i][j] == 0:
            Q.append([i,j])
            visit[i][j] = 1
            bfs(i, j)

print(ans-1)