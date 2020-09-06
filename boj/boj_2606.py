'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

def dfs(v):
    visit[v] = 1
    # print(v, end=' ')
    for w in range(1, N+1):
        if G[v][w] == 1 and visit[w] == 0:
            visit[w] = 1
            dfs(w)

N = int(input())
E = int(input())
# 인접행렬
G = [[0] * (N+1) for _ in range (N+1)]
# 인접행렬에 값 저장
for i in range(E):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1
    # 방문체크
visit = [0] * (N+1)
dfs(1)
cnt = 0

for j in range(len(visit)):
    if visit[j] != 0:
        cnt += 1
print(cnt - 1)

