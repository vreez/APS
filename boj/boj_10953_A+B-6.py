import sys; sys.stdin = open("10953.txt", "r")

T = int(input())
for i in range(T):
    arr = list(input().split(","))
    print(int(arr[0]) + int(arr[1]))

