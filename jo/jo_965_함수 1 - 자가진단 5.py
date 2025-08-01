m, n = map(int, input().split())

def func(a, b):
    result = 1
    for i in range(b):
        result *= a
    print(result)

func(m, n)