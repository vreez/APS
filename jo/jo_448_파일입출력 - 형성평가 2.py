a, b, c = map(int, input().split())
total = a + b + c
n = total // 3
m = total % 3

print("{} {}...{}".format(total, n, m))