import sys; sys.stdin = open("31281.txt", "r")

arr = list(map(int, input().split()))
new = sorted(arr)
print(new[1])