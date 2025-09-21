def func(i, n):
    if i > n:
        return
    else:
        print(i, end=" ")
        func(i+1, n)

n = int(input())
i = 1
func(i, n)