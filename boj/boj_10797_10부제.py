import sys; sys.stdin = open("10797.txt", "r")

N = list(input())

result = 0
arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] == int(N[-1]):
        result += 1

print(result)
