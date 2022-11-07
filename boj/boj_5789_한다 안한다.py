import sys; sys.stdin = open("5789.txt", "r")

N = int(input())
for i in range(N):
    arr = list(input())
    m = len(arr) // 2 - 1
    if arr[m] == arr[m+1]:
        print("Do-it")
    else:
        print("Do-it-Not")