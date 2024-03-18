import sys; sys.stdin = open("9950.txt", "r")

while True:
    l, w, a = map(int, input().split())
    if l == w and w == a and l == 0:
        break
    else:
        if l == 0:
            l = a // w
        elif w == 0:
            w = a // l
        else:
            a = l * w
    print(l, w, a)
