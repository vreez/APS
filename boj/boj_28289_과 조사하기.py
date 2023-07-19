import sys; sys.stdin = open("28289.txt", "r")

p = int(input())
s = 0
im = 0
a = 0
no = 0
for i in range(p):
    g, c, n = map(int, input().split())
    if g == 1:
        no += 1
    else:
        if c == 1 or c == 2:
            s += 1
        elif c == 3:
            im += 1
        else:
            a += 1

print(s)
print(im)
print(a)
print(no)