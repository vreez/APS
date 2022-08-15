import sys; sys.stdin = open("25305.txt", "r")

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr, reverse = True)
print(arr[k-1])
