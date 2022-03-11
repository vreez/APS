import sys; sys.stdin = open("8370.txt", "r")

arr = list(map(int, input().split()))
print(arr[0] * arr[1] + arr[2] * arr[3])