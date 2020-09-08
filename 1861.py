# 모든 위치에 대해 다 가봐야 한다.

import sys
sys.stdin = open('1861.txt', 'r')
sys.setrecursionlimit(100000000)

# 4방향 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global cnt
    visit[x][y] = 1
    cnt += 1
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        # 경계 체크
        if 0 <= newx < N and 0 <= newy < N:
            # 값이 정확히 하나 크면 그곳으로 이동하기
            if arr[newx][newy] == (arr[x][y] + 1):
                dfs(newx, newy)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 방문체크
    visit = [[0] * (N+1) for _ in range(N+1)]
    my_list = {}
    for n in range(N):
        for m in range(N):
            cnt = 0
            if visit[n][m] == 0:
                dfs(n, m)
                my_list[arr[n][m]] = cnt

    new_list = sorted((my_list.items()))

    for i in range(len(new_list)):
        if new_list[i][1] == max(my_list.values()):
            print('#{} {} {}'.format(tc, new_list[i][0], new_list[i][1]))
            break


