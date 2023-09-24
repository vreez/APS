import sys; sys.stdin = open("28444.txt", "r")

H, I, A, R, C = map(int, input().split())
first = H * I
second = A * R * C
print(first-second)