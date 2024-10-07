import sys; sys.stdin = open("32369.txt", "r")

N, A, B = map(int, input().split())
p = 1
b = 1
for i in range(N):
    p += A
    b += B
    if p < b:
        im = p
        p = b
        b = im
    elif p == b:
        b -= 1

print(p, b)
