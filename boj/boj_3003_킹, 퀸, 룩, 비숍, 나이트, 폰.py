import sys; sys.stdin = open("3003.txt", "r")

chess = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))

for i in range(6):
    print(chess[i] - arr[i], end=" ")
