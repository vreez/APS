N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visit = [0] * (N + 1)
Q = []
def bfs(x):
    Q.append(x)
    visit[x] = 1
    while Q:
        x = Q.pop(0)
        for i in G[x]:
            if visit[i] == 0:
                visit[i] = visit[x] + 1
                Q.append(i)
bfs(1)
cnt = 0
for i in range(len(visit)):
    if visit[i] == 2 or visit[i] == 3:
        cnt += 1

print(cnt)