a, b, c = map(int, input().split())

arr = []

if a > b:
    arr.append("True")
else:
    arr.append("False")
if b >= c:
    arr.append("True")
else:
    arr.append("False")
if a <= b:
    arr.append("True")
else:
    arr.append("False")
if b < c:
    arr.append("True")
else:
    arr.append("False")

print(*arr)