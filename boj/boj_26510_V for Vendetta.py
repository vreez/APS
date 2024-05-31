import sys; sys.stdin = open("26510.txt", "r")

arr = list(map(int, input().split()))
for i in range(len(arr)):
    N = arr[i]
    for j in range(N):
        if j < N-1:
            print(" "*j+"*"+" "*(2*(N-1-j)-1)+"*")
        else:
            print(" "*(N-1)+"*")