import sys; sys.stdin = open("10474.txt", "r")

while True:
    A, B = map(int, input().split())
    if A == 0 and A == B:
        break
    else:
        print("{} {} / {}".format(A // B, A % B, B))