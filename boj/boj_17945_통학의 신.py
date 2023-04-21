import sys; sys.stdin = open("17945.txt", "r")
import math

A, B = map(float, input().split())
ans1 = (-(2*A) + math.sqrt((2*A)**2 - 4*B))/2
ans2 = (-(2*A) - math.sqrt((2*A)**2 - 4*B))/2
if ans1 == ans2:
    print(int(ans1))
elif ans1 < ans2:
    print(int(ans1), int(ans2))
else:
    print(int(ans2), int(ans1))