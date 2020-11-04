'''
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
'''

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt1 = 0
def bfs1(x, y):
    global cnt1
    Q1.append([x, y])
    visit[x][y] = 1
    while Q1:
        x, y = Q1.pop(0)
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < M and 0 <= newY < N and visit[newX][newY] == 0 and arr[newX][newY] == 'W':
                visit[newX][newY] = visit[x][y] + 1
                cnt1 += 1
                Q1.append([newX, newY])
    count1.append(cnt1)

cnt2 = 0
def bfs2(x, y):
    global cnt2
    Q2.append([x, y])
    visit[x][y] = -1
    while Q2:
        x, y = Q2.pop(0)
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < M and 0 <= newY < N and visit[newX][newY] == 0 and arr[newX][newY] == 'B':
                visit[newX][newY] = visit[x][y] - 1
                cnt2 += 1
                Q2.append([newX, newY])
    count2.append(cnt2)

N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(M)]
visit = [[0] * N for _ in range(M)]

Q1 = []
Q2 = []
count1 = []
count2 = []

for i in range(M):
    for j in range(N):
        if arr[i][j] == 'W' and visit[i][j] == 0:
            cnt1 = 1
            bfs1(i, j)
        elif arr[i][j] == 'B' and visit[i][j] == 0:
            cnt2 = 1
            bfs2(i, j)

total1 = 0
for n in range(len(count1)):
    total1 += (count1[n]) ** 2

total2 = 0
for n in range(len(count2)):
    total2 += (count2[n]) ** 2

print("{} {}".format(total1, total2))

