import sys; sys.stdin = open("26068.txt", "r")

N = int(input())
cnt = 0
for i in range(N):
    dday = list(input().split("-"))
    if int(dday[1]) <= 90:
        cnt += 1

print(cnt)