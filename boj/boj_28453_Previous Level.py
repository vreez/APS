import sys; sys.stdin = open("28453.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    if arr[i] == 300:
        print(1, end=" ")
    elif arr[i] >= 275:
        print(2, end=" ")
    elif arr[i] >= 250:
        print(3, end=" ")
    else:
        print(4, end=" ")
