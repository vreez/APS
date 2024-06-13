import sys; sys.stdin = open("2702.txt", "r")
import math;

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    lcm = a*b//gcd
    print(lcm, gcd)
