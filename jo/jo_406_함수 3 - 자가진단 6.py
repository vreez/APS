num = int(input())

def func(num):
    if num == 0:
        return 0
    else:
        n = num % 10
        return n**2 + func(num//10)
print(func(num))