import sys; sys.stdin = open("10810.txt", "r")

N, M = map(int, input().split())
arr = [0] * (N + 1)
for _ in range(M):
    i, j, k = map(int, input().split())
    for p in range(i, j+1):
        arr[p] = k

for a in range(1, N+1):
    print(arr[a], end=" ")