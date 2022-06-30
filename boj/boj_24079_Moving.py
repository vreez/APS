import sys; sys.stdin = open("24079.txt", "r")

X = int(input())
Y = int(input())
Z = int(input())

if (X + Y) <= (Z + 0.5):
    print(1)
else:
    print(0)
