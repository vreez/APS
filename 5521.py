import sys; sys.stdin = open("5521.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    visit = [0] * 501
    Q = [1]
    visit[1] = 1

    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                visit[w] = visit[v] + 1
                Q.append(w)
    total = 0
    for i in range(501):
        if visit[i] == 2 or visit[i] == 3:
            total += 1

    print("#{} {}".format(tc, total))
