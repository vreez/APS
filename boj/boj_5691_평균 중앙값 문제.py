import sys; sys.stdin = open("5691.txt", "r")

while True:
    A, B = map(int, input().split())
    if A == B and A == 0:
        break
    else:
        print(A - (B - A))