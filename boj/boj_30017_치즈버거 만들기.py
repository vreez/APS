import sys; sys.stdin = open("30017.txt", "r")

A, B = map(int, input().split())
if B >= (A - 1):
    print(A + A - 1)
elif A >= (B + 1):
    print(B + B + 1)
