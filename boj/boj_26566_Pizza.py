import sys; sys.stdin = open("26566.txt", "r")
from math import pi

N = int(input())
for i in range(N):
    a1, p1 = map(int, input().split())
    r1, p2 = map(int, input().split())
    one = a1 / p1
    two = (pi * (r1 ** 2)) / p2
    if one > two:
        print("Slice of pizza")
    else:
        print("Whole pizza")