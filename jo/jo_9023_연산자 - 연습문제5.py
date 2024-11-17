import sys; sys.stdin = open("9023.txt", "r")

a, b, c = map(int, input().split())
arr = []
if a == b:
    arr.append(1)
else:
    arr.append(0)
if b == c:
    arr.append(1)
else:
    arr.append(0)
for i in range(2):
    if arr[i] == 1:
        arr.append(0)
    else:
        arr.append(1)
print(*arr)