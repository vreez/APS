import sys; sys.stdin = open("4013.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(N):
        a, b = map(int, input().split())

        check = []
        check.append([a-1, b])

        # 오른쪽 톱니바퀴 확인
        direct = b
        for i in range(a, 4):
            if magnet[i-1][2] != magnet[i][6]:
                direct = -direct
                check.append([i, direct])
            else:
                break

        # 왼쪽 톱니바퀴 확인
        direct = b

        for i in range(a-2, -1, -1):
            if magnet[i+1][6] != magnet[i][2]:
                direct = -direct
                check.append([i, direct])
            else:
                break

        # 톱니 바퀴 돌리기
        for idx, dt in check:
            if dt == 1:
                magnet[idx].insert(0, magnet[idx].pop(7))  # 시계
            else:
                magnet[idx].append(magnet[idx].pop(0))  # 반시계

    result = 0
    for i in range(4):
        if magnet[i][0] == 1:
            result += (2 ** i)

    print("#{} {}".format(tc, result))