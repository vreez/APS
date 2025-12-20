n = int(input())
if n >= 1000000:
    m = int(n * 0.2)
elif n >= 500000:
    m = int(n * 0.15)
elif n >= 100000:
    m = int(n * 0.1)
else:
    m = int(n * 0.05)
print(m, n-m)
