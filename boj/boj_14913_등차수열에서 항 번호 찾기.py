import sys; sys.stdin = open("14913.txt", "r")

a, d, k = map(int, input().split())

if (k - a) % d == 0 and (k - a) // d >= 0:
    print((k - a) // d + 1)
else:
    print("X")