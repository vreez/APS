a, b = map(int, input().split())
if a >= b:
    small = b
    big = a
else:
    small = a
    big = b
for i in range(small, big+1):
    print(i, end=" ")