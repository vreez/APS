import sys; sys.stdin = open("9848.txt", "r")

n, k = map(int, input().split())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
ans = 0
for j in range(1, n):
    if arr[j-1] - arr[j] >= k:
        ans += 1
print(ans)
