import sys; sys.stdin = open("26530.txt", "r")

N = int(input())
for i in range(N):
    M = int(input())
    total = 0
    for j in range(M):
        arr = list(input().split())
        total += (float(arr[1]) * float(arr[2]))
    print("${:.2f}".format(total))