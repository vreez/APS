from math import ceil, floor

a, b, c = map(float, input().split())

def func(a, b, c):
    arr = [a, b, c]
    new = sorted(arr)
    big = ceil(max(arr))
    small = floor(min(arr))
    middle = round(new[1])
    print(big, small, middle)

func(a, b, c)