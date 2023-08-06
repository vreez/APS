import sys; sys.stdin = open("14720.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
result = 0
for i in range(N):
    if arr[i] == result % 3:
        result += 1
print(result)
