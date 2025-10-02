n = int(input())

def func(n):
    if n <= 1:
        return n
    else:
        return func(n//2) + func(n-1)
print(func(n))