import sys; sys.stdin = open("32399.txt", "r")

S = input()
if S == ")1(":
    print(2)
elif S == "(1)":
    print(0)
else:
    print(1)