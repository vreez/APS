import sys; sys.stdin = open("5365.txt", "r")

N = int(input())
arr = list(input().split())
for i in range(N):
    if i == 0:
        print(arr[i][0], end="")
    else:
        if len(arr[i-1]) <= len(arr[i]):
            print(arr[i][len(arr[i-1])-1], end="")
        else:
            print(" ", end="")