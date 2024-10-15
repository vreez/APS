import sys; sys.stdin = open("32498.txt", "r")

N = int(input())
cnt = 0
for i in range(N):
    if int(input()) % 2:
        cnt += 1
print(cnt)