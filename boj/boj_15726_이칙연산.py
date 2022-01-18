import sys; sys.stdin = open("15726.txt", "r")

A, B, C = map(int, input().split())

multi = A * B / C
divi = A / B * C

if multi > divi:
    print(int(multi))
else:
    print(int(divi))
