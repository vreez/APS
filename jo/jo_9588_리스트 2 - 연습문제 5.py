import sys; sys.stdin = open("9588.txt", "r")

arr = list(map(int, input().split()))
first = []
second = []
for i in range(10):
    if arr[i] % 2 == 0:
        first.append(arr[i])
    else:
        second.append(arr[i])

print(max(first), min(second))