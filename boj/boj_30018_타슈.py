import sys; sys.stdin = open("30018.txt", "r")

N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

total = 0
for i in range(N):
    total += abs(arr1[i]-arr2[i])

ans = total // 2
print(ans)