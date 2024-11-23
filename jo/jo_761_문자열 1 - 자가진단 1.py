import sys; sys.stdin = open("761.txt", "r")

arr = list(input().split())
print(arr[1], end=" ")
print(arr[0]+arr[1])