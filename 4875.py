import sys
sys.stdin = open("4875.txt")


# 미로를 찾아갈 수 있는 지 검사
def MAZE(A, B):
    global result

    if maze[A][B] == 3:
        result = 1
        return

    visited.append((A, B))

    for dir in range(4):
        new_A = A + dx[dir]
        new_B = B + dy[dir]
        # 경계 확인
        if (new_A >= 0 and new_A < N and new_B >= 0 and new_B < N and maze[new_A][new_B] != 1) and (new_A, new_B) not in visited:
            MAZE(new_A, new_B)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                A, B = i, j
    result = 0
    # 방문검사
    visited = []
    # 4방향 조사
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    MAZE(A, B)


    print("#{} {}".format(tc, result))

