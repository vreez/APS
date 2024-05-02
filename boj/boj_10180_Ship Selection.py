import sys; sys.stdin = open("10180.txt", "r")

T = int(input())
for i in range(T):
    N, D = map(int, input().split())
    cnt = 0
    for j in range(N):
        v, f, c = map(int, input().split())
        if v * (f / c) >= D:
            cnt += 1
    print(cnt)