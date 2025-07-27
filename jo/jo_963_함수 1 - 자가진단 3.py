n = int(input())
def func(num):
    a = 0
    for i in range(num):
        for j in range(num):
            a += 1
            print(a, end=" ")
        print()
func(n)