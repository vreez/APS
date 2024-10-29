import sys; sys.stdin = open("1505.txt", "r")

N, M = map(int, input().split())
total = 0
for i in range(1, M+1):
    total += (i * N)
print(total)