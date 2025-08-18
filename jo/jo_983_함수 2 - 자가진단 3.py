a, b = map(int, input().split())
c, d = map(float, input().split())

def func(a, b, c, d):
    if abs(a) > abs(b):
        print(a)
    else:
        print(b)
    if abs(c) > abs(d):
        print(d)
    else:
        print(c)

func(a, b, c, d)