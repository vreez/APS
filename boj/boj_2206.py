dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    Q = []
    Q.append([0, 0, 1])
    visit[0][0][1] = 1
    while Q:
        x, y, z = Q.pop(0)
        if x == N-1 and y == M-1:
            return visit[x][y][z]
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < N and 0 <= newY < M:
                if arr[newX][newY] == 1 and z == 1:
                    visit[newX][newY][0] = visit[x][y][1] + 1
                    visit[newX][newY][1] = 1
                    Q.append([newX, newY, 0])
                elif arr[newX][newY] == 0 and visit[newX][newY][z] == 0:
                    visit[newX][newY][z] = visit[x][y][z] + 1
                    Q.append([newX, newY, z])


    return -1

N, M = map(int, input().split())

arr = [list(map(int, list(input()))) for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs())