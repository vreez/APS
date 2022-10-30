import sys; sys.stdin = open("4562.txt", "r")

N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    if x >= y:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")