a, b = map(int, input().split())

def func(x, y):
    print("두 수의 합 = {}".format(x + y))
    print("두 수의 차 = {}".format(abs(x-y)))

func(a, b)