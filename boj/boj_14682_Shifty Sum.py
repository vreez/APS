import sys; sys.stdin = open("14682.txt", "r")

N = int(input())
k = int(input())
total = 0
m = 1
for i in range(k+1):
    total += (N * m)
    m *= 10
print(total)