import sys; sys.stdin = open("3053.txt", "r")
import math

R = int(input())
print("{:.6f}".format(R*R*math.pi))
print("{:.6f}".format(2*R*R))
