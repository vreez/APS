import sys; sys.stdin = open("7581.txt", "r")

while True:
    l, w, h, v = map(int, input().split())
    if l == w and w == h and h == v and l == 0:
        break
    else:
        if l == 0:
            l = v // w // h
        elif w == 0:
            w = v // l // h
        elif h == 0:
            h = v // w // l
        else:
            v = l * w * h
        print(l, w, h, v)