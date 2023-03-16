import sys; sys.stdin = open("10995.txt", "r")

N = int(input())

for i in range(N):
    if i % 2 == 0:
        print("* " * N)
    else:
        print(" *" * N)