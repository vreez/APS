import sys; sys.stdin = open("20361.txt", "r")

N, X, K = map(int, input().split())
arr = [0]*(N+1)
arr[X] = 1
for _ in range(K):
    a, b = map(int, input().split())
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

print(arr.index(1))