n = int(input())

def func(n):
    if n == 0:
        return 0
    else:
        func(n//2)
        print(n, end=" ")
func(n)