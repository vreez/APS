import sys; sys.stdin = open("21335.txt", "r")
from math import pi

a = int(input())

result = (a / pi) ** 0.5 * 2 * pi
print(result)