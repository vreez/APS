import sys; sys.stdin = open("9699.txt", "r")

N = int(input())
for i in range(1, N+1):
    arr = list(map(int, input().split()))
    print("Case #{}: {}".format(i, max(arr)))