import sys; sys.stdin = open("18247.txt", "r")

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    if N >= 12 and M >= 4:
        print((12 * M) - (M - 4))
    else:
        print(-1)

