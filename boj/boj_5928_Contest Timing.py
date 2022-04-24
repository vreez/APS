import sys; sys.stdin = open("5928.txt", "r")

D, H, M = map(int, input().split())

T1 = (D * 24 * 60) + (H * 60) + M
T2 = (11 * 24 * 60) + (11 * 60) + 11

if T1 - T2 < 0:
    print(-1)
else:
    print(T1 - T2)
