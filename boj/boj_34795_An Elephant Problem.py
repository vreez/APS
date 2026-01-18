m, d = map(int, input().split())

if d % m > 0:
    print(d//m+1)
else:
    print(d//m)