import sys; sys.stdin = open("8721.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
num = 1
for i in range(n):
    if arr[i] != num:
        cnt += 1
    else:
        num += 1

print(cnt)
