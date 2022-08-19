import sys; sys.stdin = open("2501.txt", "r")

N, K = map(int, input().split())

arr = []
for i in range(1, int(N**(1/2))+1):
    if N % i == 0:
        arr.append(i)
        if i * i != N:
            arr.append(N // i)
arr = sorted(arr)
if K-1 >= len(arr):
    print(0)
else:
    print(arr[K-1])