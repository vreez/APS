import sys; sys.stdin = open("17912.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
result = arr.index(min(arr))
print(result)