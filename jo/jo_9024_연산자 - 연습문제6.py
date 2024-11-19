import sys; sys.stdin = open("9024.txt", "r")

a, b, c = map(int, input().split())
arr = []
if a > b:
    arr.append(1)
else:
    arr.append(0)
if b >= c:
    arr.append(1)
else:
    arr.append(0)
if a <= b:
    arr.append(1)
else:
    arr.append(0)
if b < c:
    arr.append(1)
else:
    arr.append(0)

print(*arr)
