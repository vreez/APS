import sys; sys.stdin = open("15128.txt", "r")

p1, q1, p2, q2 = map(int, input().split())

if p1 / q1 * p2 / q2 / 2 == int(p1 / q1 * p2 / q2 / 2):
    print(1)
else:
    print(0)