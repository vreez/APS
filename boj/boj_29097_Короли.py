import sys; sys.stdin = open("29097.txt", "r")

n, m, k, a, b, c = map(int, input().split())
j = n * a
r = m * b
s = k * c
arr = [j, r, s]
big = max(arr)

if j == big:
    print("Joffrey", end=" ")
if r == big:
    print("Robb", end=" ")
if s == big:
    print("Stannis", end=" ")