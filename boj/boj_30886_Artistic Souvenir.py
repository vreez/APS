import sys; sys.stdin = open("30886.txt", "r")
import math

a = int(input())
n = ((a/math.pi)**0.5)

ans = ((n+1)*2)**2
print("{:.10f}".format(ans))


