n = int(input())

def func(n):
    if n <= 1:
        return n
    else:
        return func(n-1) + func(n-2)
print(func(n))