import sys; sys.stdin = open("27959.txt", "r")

N, M = map(int, input().split())
if (N*100) >= M:
    print("Yes")
else:
    print("No")