import sys; sys.stdin = open("31048.txt", "r")
import math;

T = int(input())
for i in range(T):
    N = int(input())
    ans = math.factorial(N)
    print(ans%10)