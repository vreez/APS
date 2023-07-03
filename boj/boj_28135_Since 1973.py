import sys; sys.stdin = open("28135.txt", "r")

N = int(input())
cnt = 0
for i in range(N):
    cnt += 1
    if str(i).find("50") != -1:
        cnt += 1
print(cnt)