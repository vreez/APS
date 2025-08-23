a, b, c, d, e = map(int, input().split())

def func(a, b, c, d, e):
    arr = [a, b, c, d, e]
    new = sorted(arr)
    print(*new)

func(a, b, c, d, e)