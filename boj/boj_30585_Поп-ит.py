import sys; sys.stdin = open("30585.txt", "r")

h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]

zero = 0
one = 0
for i in range(h):
    for j in range(w):
        if arr[i][j] == '0':
            zero += 1
        else:
            one += 1

print(min(zero, one))