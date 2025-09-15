import math

def func(a, b):
    first = a**(1/2)
    second = b**(1/2)

    start = math.ceil(min(first, second))
    end = math.ceil(max(first, second))
    cnt = 0
    if start > min(first, second):
        cnt -= 1
    for i in range(start, end+1):
        cnt += 1
    print(cnt)

a, b = map(float, input().split())

func(a, b)
