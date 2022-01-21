import sys; sys.stdin = open("9085.txt", "r")

N = int(input())
for _ in range(N):
    M = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))