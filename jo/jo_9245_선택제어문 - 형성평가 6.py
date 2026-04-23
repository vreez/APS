x = int(input())
y = int(input())
o = input()

if o == "+":
    print("ans = {}".format(x + y))
elif o == "-":
    print("ans = {}".format(x - y))
elif o == "*":
    print("ans = {}".format(x * y))
else:
    print("ans = {}".format(x % y))