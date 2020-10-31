'''
3 4 5
3 2
2 2
3 1
2 3
1 1

2 2 3
1 1
1 2
2 1

8 10 7
1 1
2 3
2 5
3 4
3 9
4 6
4 8

3 4 0
'''

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
big = 0
count = 0
def bfs(x, y):
    global big, count
    Q.append([x, y])
    visit[x][y] = 1
    count = 1
    while Q:
        x, y = Q.pop(0)
        if count >= big:
            big = count
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < N+1 and 0 <= newY < M+1 and G[newX][newY] == 1 and visit[newX][newY] == 0:
                visit[newX][newY] = 1
                count += 1
                Q.append([newX, newY])

N, M, K = map(int, input().split())
G = [[0] * (M + 1) for _ in range(N + 1)]
visit = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
    r, c = map(int, input().split())
    G[r][c] = 1

Q = []
for i in range(N+1):
    for j in range(M+1):
        if G[i][j] == 1 and visit[i][j] == 0:
            bfs(i, j)

if big == 0:
    print(0)
else:
    print(big)

