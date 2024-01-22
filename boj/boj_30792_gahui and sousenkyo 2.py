import sys;sys.stdin = open("30792.txt", "r")

n = int(input())
num = int(input())
arr = list(map(int, input().split()))
ans = 1
for i in range(len(arr)):
    if arr[i] >= num:
        ans += 1
print(ans)