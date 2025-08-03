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
        result = 0
    print("{} {} {} = {}".format(a, b, c, int(result)))

func(a, b, c)