import sys; sys.stdin = open("30143.txt", "r")

T = int(input())
for i in range(T):
    N, A, D = map(int, input().split())
    total = A
    num = A
    if N-1 > 0:
        for j in range(N-1):
            total += num + D
            num += D
    print(total)
