import sys; sys.stdin = open("10817.txt", "r")

A, B, C = map(int, input().split())
arr = []
arr.append(A)
arr.append(B)
arr.append(C)
arr.sort()
print(arr[1])