import sys; sys.stdin = open("10952.txt", "r")

while True:
    A, B = map(int, input().split())
    if A == 0 and A == B:
        break
    else:
        print(A + B)