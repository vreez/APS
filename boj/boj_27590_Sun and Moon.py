import sys; sys.stdin = open("27590.txt", "r")

ds, ys = map(int, input().split())
dm, ym = map(int, input().split())

S = ys-ds
M = ym-dm

while S != M:
    if S < M:
        S += ys
    else:
        M += ym
print(S)