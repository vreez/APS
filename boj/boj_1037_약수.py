import sys; sys.stdin = open("1037.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[0] * arr[-1])
