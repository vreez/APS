num = int(input())

def func(num):
    if num < 10:
        return num
    else:
        return num % 10 + func(num // 10)
print(func(num))