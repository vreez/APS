import sys; sys.stdin = open("31282.txt", "r")

N, M, K = map(int, input().split())
d = 0
b = N
c = 0
while d < b:
    d += K
    b += M
    c += 1
print(c)