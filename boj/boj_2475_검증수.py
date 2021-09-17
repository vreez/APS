import sys; sys.stdin = open("2475.txt", "r")

arr = list(map(int, input().split()))

result = 0
for i in range(5):
    result += (arr[i] ** 2)

print(result % 10)