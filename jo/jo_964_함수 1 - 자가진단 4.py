a, b, c = map(int, input().split())

def func(x, y, z):
    new = []
    new.append(x)
    new.append(y)
    new.append(z)
    print(max(new))

func(a, b, c)
