import sys
from collections import deque

# 시간초과 해결을 위해서 input() 대신 sys.stdin.readline()을 사용했다.

M, N, H = map(int, sys.stdin.readline().split())
arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

# 깊이를 나타내는 z축을 더해준다.

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

ans = 0
cnt = 0
def bfs():
    global ans, cnt
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if arr[h][n][m] != 0:
                    cnt += 1
                if arr[h][n][m] == -1:
                    visit[h][n][m] = -1

    if cnt == M * N * H:
        return 0

    while Q:
        mine = Q.popleft()
        z, x, y = mine[0], mine[1], mine[2]
        for i in range(6):
            newx = x + dx[i]
            newy = y + dy[i]
            newz = z + dz[i]
            if 0 <= newx < N and 0 <= newy < M and 0 <= newz < H:
                if arr[newz][newx][newy] == 0 and visit[newz][newx][newy] == 0:
                    Q.append([newz, newx, newy])
                    visit[newz][newx][newy] = visit[z][x][y] + 1
                    ans = max(ans, visit[newz][newx][newy])

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if visit[h][n][m] == 0:
                    return -1

    return ans - 1


visit = [[[0] * M for _ in range(N)] for _ in range(H)]
Q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1 and visit[i][j][k] == 0:
                Q.append([i, j, k])
                visit[i][j][k] = 1

print(bfs())
