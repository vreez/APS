import sys; sys.stdin = open("17256.txt", "r")

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

print(cx - az, cy // ay, cz - ax)