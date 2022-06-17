import sys; sys.stdin = open("18411.txt", "r")

arr = list(map(int, input().split()))

print(sum(arr) - min(arr))