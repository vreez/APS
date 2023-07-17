import sys; sys.stdin = open("28281.txt", "r")

N, X = map(int, input().split())
arr = list(map(int, input().split()))

flag = 10000000000
for i in range(1, N):
    result = X * (arr[i-1] + arr[i])
    if result < flag:
        flag = result

print(flag)