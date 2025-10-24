a, b = map(float, input().split())
c = round(a+b, 2)
a = round(a, 2)
b = round(b, 2)

print("{:.2f} {:.2f} {:.2f}".format(a, b, c))