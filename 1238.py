def bfs(v):
    Q = []
    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.pop(0)
        for w in range(1, N + 1):
            if G[v][w] == 1 and visit[w] == 0:
                Q.append(w)
                visit[w] = visit[v] + 1
    return

for tc in range(1, 11):
    E, v = map(int, input().split())
    fromto = list(map(int, input().split()))
    N = 100
    # 인접행렬
    G = [[0] * (N + 1) for _ in range(N + 1)]
    # 인접행렬에 연결
    for i in range(E // 2):
        s, e = fromto[2 * i], fromto[2 * i + 1]
        G[s][e] = 1
    # 방문체크
    visit = [0] * (N + 1)

    bfs(v)

    max_list = []
    max_num = visit[0]

    for idx, val in enumerate(visit):
        if val >= max_num:
            max_num = val
            max_idx = idx
    print("#{} {}".format(tc, max_idx))