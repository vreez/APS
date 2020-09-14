# 시간초과 문제해결
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
ans = 0
def bfs(x, y):
    global cnt, ans
    # 초기에 토마토가 다 익어있었을 때
    for n in range(N):
        for m in range(M):
            if arr[n][m] != 0:
                cnt += 1
            if arr[n][m] == -1:
                visit[n][m] = -1

    if cnt == (N*M):
        return 0

    while Q:
        mine = Q.popleft()
        x, y = mine[0], mine[1]
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0 <= newx < N and 0 <= newy < M:
                if arr[newx][newy] == 0 and visit[newx][newy] == 0:
                    visit[newx][newy] = visit[x][y] + 1
                    Q.append([newx,newy])
                    ans = max(visit[newx][newy], ans)

    # 모든 arr를 다 돌았는데, 0이 남아있을 때 (안 익은 토마토가 남아있을 때)
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                return -1
    # 1부터 더하므로, 마지막에 계산할 때는 1을 빼준다.
    return ans - 1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]
Q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visit[i][j] == 0:
            # 익은 여러개의 토마토가 동시에 주변 토마토를 익게 만든다.
            Q.append([i, j])
            visit[i][j] = 1

print(bfs(i, j))