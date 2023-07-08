import sys; sys.stdin = open("25377.txt", "r")

N = int(input())
check = False
w = 1001
for i in range(N):
    at, st = map(int, input().split())
    if at <= st:
        check = True
        if st < w:
            w = st
if check:
    print(w)
else:
    print(-1)