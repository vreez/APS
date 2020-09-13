'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

5
3 8 4 2 4
2 10 12 3 2
3 3 5 6 2
3 11 8 7 3
2 12 9 10 9

5
100 100 99 99 100
100 99 100 99 100
99 99 100 100 99
100 99 99 99 100
100 99 100 100 100

5
3 3 3 3 3
3 3 3 3 3
3 3 3 3 3
3 3 3 3 3
3 3 3 3 3
'''
import sys;

sys.setrecursionlimit(1000000000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    visit[x][y] = 1
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < N and 0 <= newy < N:
            if G[newx][newy] == 0 and visit[newx][newy] == 0:
                dfs(newx, newy)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for number in range(0, 101):
    G = [[0] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] <= number:
                G[i][j] = 1

    cnt = 0
    for i in range(N):
        for j in range(N):
            if G[i][j] == 0 and visit[i][j] == 0:
                dfs(i, j)
                cnt += 1

    if cnt == 0:
        break
    ans = max(ans, cnt)

print(ans)