import sys; sys.stdin = open("26026.txt", "r")

n = int(input())
arr = list(map(int, input()))

for i in range(n):
    if arr[i] == 1:
        if i + 1 < n and arr[i+1] == 0:
            arr[i+1] = 2
        if i + 2 < n and arr[i+2] == 0:
            arr[i+2] = 2
cnt = 0
for i in range(n):
    if arr[i] != 0:
        cnt += 1
print(cnt)


