import sys; sys.stdin = open("10409.txt", "r")

n, T = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
for i in range(n):
    total += arr[i]
    if total > T:
        print(i)
        break
    elif i == n-1:
        print(n)