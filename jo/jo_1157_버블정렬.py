import sys; sys.stdin = open("1157.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1):
    for j in range(N-1):
        if arr[j] > arr[j+1]:
            new = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = new
    print(*arr)