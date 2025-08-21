from math import trunc, ceil

a = int(input())

def func(a):
    ans = a**2*3.14
    print("원의 반지름 :", end=" ")
    print("원의 넓이")
    print("버림 : {}".format(int(trunc(ans))))
    print("반올림 : {}".format(int(round(ans))))
    print("올림 : {}".format(int(ceil(ans))))

func(a)