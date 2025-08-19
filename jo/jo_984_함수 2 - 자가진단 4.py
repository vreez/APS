a = int(input())

def func(a):
    ans = (a / 3.14) ** 0.5
    print("{:.2f}".format(round(ans, 2)))
func(a)