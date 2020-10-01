# 결과 출력시, -1을 해주므로, 촌수를 구할 수 없을 때, return 되는 값을 0으로 설정해야 한다는 것에 주의하기!

def bfs(v):
    Q = []
    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.pop(0)
        if v == b:
            return visit[v]
        for w in range(1, n + 1):
            if G[v][w] == 1 and visit[w] == 0:
                Q.append(w)
                visit[w] = visit[v] + 1
    return 0

n = int(input())
a, b = map(int, input().split())
m = int(input())
G = [[0] * (n+1) for _ in range(n+1)]
visit = [0] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = 1

print(bfs(a)-1)
