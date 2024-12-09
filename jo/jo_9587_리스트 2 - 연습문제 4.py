import sys; sys.stdin = open("9587.txt", "r")

arr = list(map(int, input().split()))
print(max(arr))