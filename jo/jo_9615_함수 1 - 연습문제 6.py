a, b, c = input().split(" ")

def func(a, b, c):
    if b == "+":
        result = float(a) + float(c)
    elif b == "-":
        result = float(a) - float(c)
    elif b == "*":
        result = float(a) * float(c)
    elif b == "/":
        result = float(a) / float(c)
    else:
        result = 0.0
    print("{} {} {} = {:.1f}".format(a, b, c, result))

func(a, b, c)