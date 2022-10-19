import sys; sys.stdin = open("10707.txt", "r")

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = P * A
Y = 0
if C < P:
    Y = B + ((P-C) * D)
else:
    Y = B

if X > Y:
    print(Y)
else:
    print(X)