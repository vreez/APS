# 그래프 문제
# 이 문제에서 사람은 정점, 두 사람이 서로 아는 관계가 간선
# 결합 컴포넌트 (직/간접적인 관계로 이어져 있는 것)
# 무향 그래프
import sys; sys.stdin = open('7465.txt', 'r')

def dfs(v):
    visit[v] = 1
    for w in range(N+1):
        if G[v][w] == 1 and visit[w] == 0:
            dfs(w)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        s, e = map(int, input().split())
        G[s][e] = 1
        G[e][s] = 1
    visit = [0] * (N+1)

    cnt = 0
    for j in range(1, N+1):
        if visit[j] == 0:
            dfs(j)
            cnt += 1

    print('#{} {}'.format(tc, cnt))
