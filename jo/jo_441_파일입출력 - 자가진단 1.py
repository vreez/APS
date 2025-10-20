a, b = map(int, input().split())
if a >= b:
    mx = a
    mi = b
else:
    mx = b
    mi = a

total = 0
for i in range(mi, mx+1):
    total += i

print(total)