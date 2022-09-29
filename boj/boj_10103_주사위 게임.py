import sys; sys.stdin = open("10103.txt", "r")

N = int(input())
cs = 100
ss = 100
for i in range(N):
    c, s = map(int, input().split())
    if c > s:
        ss -= c
    elif s > c:
        cs -= s

print(cs)
print(ss)