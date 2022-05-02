import sys; sys.stdin = open("4299.txt", "r")

P, M = map(int, input().split())

A = (P + M) // 2
B = P - A

if P >= M:
    if A > B:
        if A - B == M:
            print(A, B)
        else:
            print(-1)
    else:
        if B - A == M:
            print(B, A)
        else:
            print(-1)
else:
    print(-1)