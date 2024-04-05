import sys; sys.stdin = open("31656.txt", "r")

arr = list(input())
ans = arr[0]
for i in range(1, len(arr)):
    if arr[i-1] != arr[i]:
        ans += arr[i]
print(ans)