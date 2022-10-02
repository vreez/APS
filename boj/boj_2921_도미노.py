import sys; sys.stdin = open("2921.txt", "r")

N = int(input())

total = 0
arr = []
for i in range(N+1):
    for j in range(i, N+1):
        total += (i + j)

print(total)

