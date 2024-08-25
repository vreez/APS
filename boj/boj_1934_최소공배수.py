import sys; sys.stdin = open("1934.txt", "r")
import math;

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(int(a*b / math.gcd(a, b)))