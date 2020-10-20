import sys; sys.stdin = open("5105.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    global result
    Q.append([x, y])
    visit[x][y] = 1
    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if arr[x][y] == 3:
                result = visit[x][y] - 2
                return result
            if 0 <= newX < N and 0 <= newY < N and arr[newX][newY] != 1 and visit[newX][newY] == 0:
                visit[newX][newY] = visit[x][y] + 1
                Q.append([newX, newY])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input()))for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    Q =[]
    result = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j

    bfs(x, y)

    print("#{} {}".format(tc, result))
