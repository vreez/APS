import sys; sys.stdin = open("27182.txt", "r")

n, m = map(int, input().split())
total = abs(n-m) + 14

if n > 7:
    print(n-7)
else:
    print(total - (7 - n))

