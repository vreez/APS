n, m, s = map(int, input().split())

a = s * (m + 1) * (100 - n) // 100
b = m * s

print(min(a, b))
