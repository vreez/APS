import sys; sys. stdin = open("29683.txt", "r")

n, A = map(int, input().split())
arr = list(map(int, input().split()))
total = 0
for i in range(n):
    total += (arr[i] // A)
print(total)