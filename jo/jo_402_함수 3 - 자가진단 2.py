def func(i, n):
    if i < 1:
        return
    else:
        print(i, end=" ")
        func(i-1, n)

n = int(input())
func(n, n)