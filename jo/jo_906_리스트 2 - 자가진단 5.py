import sys; sys.stdin = open("906.txt", "r")

arr = list(map(int, input().split()))
first = []
second = []
for i in range(10):
    if arr[i] < 100:
        first.append(arr[i])
    else:
        second.append(arr[i])

if len(first) == 0:
    mx = 100
else:
    mx = max(first)
if len(second) == 0:
    mn = 100
else:
    mn = min(second)

print(mx, mn)