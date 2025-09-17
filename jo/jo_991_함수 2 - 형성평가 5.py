def func(a, b, c):
    sum1 = a + b + c
    avg1 = sum1 / 3
    print(round(avg1))
    sum2 = round(a) + round(b) + round(c)
    avg2 = sum2 / 3
    print(round(avg2))

a, b, c = map(float, input().split())
func(a, b, c)