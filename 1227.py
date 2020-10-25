import sys; sys.stdin = open("1227.txt")

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
                result += 1
                return result
            if 0 <= newX < 100 and 0 <= newY < 100 and arr[newX][newY] != 1 and visit[newX][newY] == 0:
                visit[newX][newY] = 1
                Q.append([newX, newY])

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    visit = [[0] * 100 for _ in range(100)]
    Q = []
    result = 0

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                x, y = i, j

    bfs(x, y)

    print("#{} {}".format(tc, result))
