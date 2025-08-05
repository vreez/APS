a, b = map(int, input().split())

def func(m, n):
    if m > n:
        m //= 2
        n *= 2
    else:
        m *= 2
        n //= 2
    print(m, n)

func(a, b)