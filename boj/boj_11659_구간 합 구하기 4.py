import sys; sys.stdin = open("11659.txt", "r")

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = [0] * N
total = 0
for i in range(N):
    total += arr[i]
    result[i] = total

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if start == 1:
        print(result[end - 1])
    else:
        print(result[end - 1] - result[(start - 1) - 1])