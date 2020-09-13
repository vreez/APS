'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
'''
# 런타임에러 방지를 위해!
import sys; sys.setrecursionlimit(1000000000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count = 0
my_count = []

def dfs(x, y):
    global count
    visit[x][y] = 1
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < M and 0 <= newy < N and visit[newx][newy] == 0:
            if G[newx][newy] == 0:
                visit[newx][newy] = 1
                count += 1
                dfs(newx, newy)

M, N, K = map(int, input().split())
arr = []
for i in range(K):
    arr.append(list(map(int, input().split())))
# print(arr)

G = [[0] * N for _ in range(M)]
visit = [[0] * N for _ in range(M)]
# print(G)
for k in range(K):
    for j in range(arr[k][1], arr[k][3]):
        for i in range(arr[k][0], arr[k][2]):
            G[j][i] = 1
# print(G)

cnt = 0
for m in range(M):
    for n in range(N):
        if G[m][n] == 0 and visit[m][n] == 0:
            cnt += 1
            count = 1
            dfs(m, n)
            my_count.append(count)
# print(visit)
print(cnt)
new_list = sorted(my_count)
for i in range(len(new_list)):
    print(new_list[i], end=' ')


