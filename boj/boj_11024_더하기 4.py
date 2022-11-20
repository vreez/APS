import sys; sys.stdin = open("11024.txt", "r")

N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    print(sum(arr))