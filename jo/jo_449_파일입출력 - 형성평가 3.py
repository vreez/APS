a, b, c = input().split()
result = 0
if c == "+":
    result = int(a) + int(b)
elif c == "-":
    result = int(a) - int(b)
elif c == "*":
    result = int(a) * int(b)
elif c == "/":
    result = int(a) // int(b)
else:
    result = int(a) % int(b)
print("{} {} {} = {}".format(int(a), c, int(b), result))