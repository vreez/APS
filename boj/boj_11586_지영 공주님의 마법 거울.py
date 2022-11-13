import sys; sys.stdin = open("11586.txt", "r")

N = int(input())
arr = list((list(input()) for _ in range(N)))
K = int(input())

if K == 1:
    for i in range(N):
        print("".join(arr[i]))
elif K == 2:
    for i in range(N):
        new = arr[i][::-1]
        print("".join(new))
else:
    for i in range(N-1, -1, -1):
        print("".join(arr[i]))