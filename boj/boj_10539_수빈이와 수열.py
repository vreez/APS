import sys; sys.stdin = open("10539.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

num = 0
for i in range(1, N+1):
    print(i * arr[i-1] - num, end=" ")
    num = i * arr[i-1]