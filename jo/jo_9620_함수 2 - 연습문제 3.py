a, b = map(int, input().split())
c, d = map(float, input().split())

def func(a, b, c, d):
    print("두 정수의 차 : {}".format(abs(a-b)))
    print("두 실수의 차 : {:.6f}".format(abs(c-d)))

func(a, b, c, d)