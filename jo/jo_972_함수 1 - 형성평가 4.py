a, b = map(int, input().split())

def func(a, b):
    if a > b:
        print(a**2 - b**2)
    else:
        print(b**2 - a**2)
func(a, b)