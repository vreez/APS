import sys; sys.stdin = open("5988.txt", "r")

N = int(input())
for _ in range(N):
    if int(input()) % 2 == 0:
        print("even")
    else:
        print("odd")