import sys; sys.stdin = open("5656.txt", "r")

num = 0
while True:
    a, op, b = input().split()
    num += 1
    if op == "E":
        break
    else:
        if op == ">":
            if int(a) > int(b):
                ans = "true"
            else:
                ans = "false"
        elif op == ">=":
            if int(a) >= int(b):
                ans = "true"
            else:
                ans = "false"
        elif op == "<":
            if int(a) < int(b):
                ans = "true"
            else:
                ans = "false"
        elif op == "<=":
            if int(a) <= int(b):
                ans = "true"
            else:
                ans = "false"
        elif op == "==":
            if int(a) == int(b):
                ans = "true"
            else:
                ans = "false"
        elif op == "!=":
            if int(a) != int(b):
                ans = "true"
            else:
                ans = "false"
    print("Case {}: {}".format(num, ans))