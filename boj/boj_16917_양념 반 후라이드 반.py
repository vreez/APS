import sys; sys.stdin = open("16917.txt", "r")

A, B, C, X, Y = map(int, input().split())

if A + B < 2 * C:
    print((A * X) + (B * Y))
else:
    mini = min(X, Y)
    ans = (C * mini * 2) + (min(2*C, A) * max(0, X-Y)) + (min(2 * C, B) * max(0, Y-X))
    print(ans)