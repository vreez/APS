import sys; sys.stdin = open("9838.txt", "r")

N = int(input())
arr = [0]*(N+1)
for i in range(N):
    num = int(input())
    arr[num] = i+1

for i in range(1, N+1):
    print(arr[i])