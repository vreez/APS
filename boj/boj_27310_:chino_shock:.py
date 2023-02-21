import sys; sys.stdin = open("27310.txt", "r")

cnt = 0
arr = list(input())
for i in range(len(arr)):
    if arr[i] == "_":
        cnt += 1
print(len(arr) + 2 + (cnt * 5))