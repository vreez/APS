import sys; sys.stdin = open("31428.txt", "r")

N = int(input())
arr = list(input().split())
H = input()
cnt = 0
for i in range(N):
    if arr[i] == H:
        cnt += 1

print(cnt)