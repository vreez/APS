'''
8 9 10
'''
from collections import deque

ans = []
def bfs(x, y):
    Q.append([x, y])
    while Q:
        x, y = Q.popleft()
        z = C - x - y
        if visit[x][y] != 0: continue
        visit[x][y] = 1
        if x == 0:
            ans.append(z)
        if y < B:
            water = min(x, B-y)
            newx = x - water
            newy = y + water
            Q.append([newx, newy])
        if z < C:
            water = min(x, C-z)
            newx = x - water
            Q.append([newx, y])
        if x < A:
            water = min(y, A-x)
            newy = y - water
            newx = x + water
            Q.append([newx, newy])
        if z < C:
            water = min(y, C-z)
            newy = y - water
            Q.append([x, newy])
        if x < A:
            water = min(z, A-x)
            newx = x + water
            Q.append([newx, y])
        if y < B:
            water = min(z, B-y)
            newy = y + water
            Q.append([x, newy])

A, B, C = map(int, input().split())
visit = [[0] * (B + 1) for _ in range(A + 1)]
Q = deque()
bfs(0, 0)
result = sorted(ans)

for i in range(len(result)):
    print(result[i], end=" ")
