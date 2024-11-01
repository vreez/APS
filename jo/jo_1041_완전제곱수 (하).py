import sys; sys.stdin = open("1041.txt", "r")

n, m = map(int, input().split())
cnt = 0
arr = []
for i in range(n, m+1):
    num = int(i ** 0.5)
    if num * num == i:
        cnt += 1
        arr.append(i)
if cnt > 0:
    print(*arr)
else:
    print(0)