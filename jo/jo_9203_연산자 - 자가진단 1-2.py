import math
a, b, c = map(int, input().split())

print("sum = {}".format(a+b+c))
print("avg = {}".format(math.trunc((a+b+c)/3)))