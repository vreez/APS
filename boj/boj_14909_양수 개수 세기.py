import sys; sys.stdin = open("14909.txt", "r")

arr = list(map(int, input().split()))
cnt = 0
for i in range(len(arr)):
    if arr[i] > 0:
        cnt += 1
print(cnt)        