import sys; sys.stdin = open("28940.txt", "r")
import math

w, h = map(int, input().split())
n, a, b = map(int, input().split())

if (w < a) or (h < b):
    print(-1)
else:
    l = (w // a) * (h // b)
    ans = math.ceil(n / l)
    print(ans)