a, b, c = map(int, input().split())
result = a if a < b and a < c else(b if b < c else c)
print(result)