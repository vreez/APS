import sys; sys.stdin = open("13163.txt", "r")

N = int(input())
for i in range(N):
    arr = list(input().split(" "))
    new = "".join(arr[1:])
    print("god"+new)