import sys; sys.stdin = open("31880.txt", "r")

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = sum(a)
for i in range(m):
    if b[i] == 0:
        continue
    else:
        total *= b[i]
print(total)
