n = int(input())

def func(n):
    for i in range(1, n+1):
        for j in range(n):
            print(i+(j*i), end=" ")
        print()

func(n)
