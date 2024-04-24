import sys; sys.stdin = open("5692.txt", "r")
import math

while True:
    num = sys.stdin.readline().rstrip()
    if int(num) == 0:
        break
    else:
        n = len(num)
        a = n
        ans = 0
        for i in range(n):
            ans += int(num[i]) * math.factorial(a)
            a -= 1
        print(ans)

