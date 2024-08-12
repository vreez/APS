import sys; sys.stdin = open("2399.txt", "r")

n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(n):
        ans += abs(arr[i] - arr[j])
print(ans)