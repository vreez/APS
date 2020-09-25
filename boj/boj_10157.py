C, R = map(int, input().split())
K = int(input())

def solve(arr):
    x, y = R-1, 0
    newX, newY = R-1, 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = 0
    num = 1
    for i in range(C*R):
        x, y = newX, newY
        arr[x][y] = num
        newX = x + dx[dir]
        newY = y + dy[dir]
        if newX < 0 or newX >= R or newY < 0 or newY >= C or arr[newX][newY] != 0:
            dir = (dir+1) % 4
            newX = x + dx[dir]
            newY = y + dy[dir]
        num += 1

arr = [[0] * C for _ in range(R)]

solve(arr)
# 인덱스에 유의해서 프린트하기!
for i in range(R):
    for j in range(C):
        if arr[i][j] == K:
            print("{} {}".format(j+1,  R - i))
if K > (C * R):
    print(0)