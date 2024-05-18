import sys; sys.stdin = open("31798.txt", "r")

a, b, c = map(int, input().split())
if a == 0:
    print(c**2 - b)
elif b == 0:
    print(c**2 - a)
else:
    print(int((a + b) ** 0.5))