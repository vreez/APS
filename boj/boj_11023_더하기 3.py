import sys; sys.stdin = open("11023.txt", "r")

arr = list(map(int, input().split()))
print(sum(arr))