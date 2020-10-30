import sys; sys.stdin = open("5188.txt", "r")

dx = [0, 1]
dy = [1, 0]

def dfs(x, y):
    global cnt, min_num
    cnt += arr[x][y]
    if min_num < cnt:
        return
    if x == N-1 and y == N-1:
        min_num = cnt
        return
    else:
        for i in range(2):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < N and 0 <= newY < N:
                dfs(newX, newY)
                cnt -= arr[newX][newY]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 1000000000
    cnt = 0
    dfs(0, 0)
    print("#{} {}".format(tc, min_num))