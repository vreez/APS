import sys; sys.stdin = open("27159.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

total = arr[0]
for i in range(1, N):
    if arr[i] - arr[i-1] > 1:
        total += arr[i]

print(total)