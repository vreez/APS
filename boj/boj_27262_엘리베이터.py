import sys; sys.stdin = open("27262.txt", "r")

n, k, a, b = map(int, input().split())

e = (k - 1) * b + (n - 1) * b
w = (n - 1) * a

print(e, w)