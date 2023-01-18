import sys; sys.stdin = open("25494.txt", "r")

N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    answer = min(arr)
    print(answer)