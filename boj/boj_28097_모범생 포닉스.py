import sys; sys.stdin = open("28097.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

total = sum(arr) + (8*(N-1))

print(total//24, total%24)
