import sys; sys.stdin = open("6322.txt", "r")

num = 0
while True:
    num += 1
    a, b, c = map(int, input().split())
    if a == b and b == c and a == 0:
        break
    else:
        print("Triangle #{}".format(num))
        if c == -1:
            c = ((a**2) + (b**2))**0.5
            print("c = {:.3f}".format(c))
        elif max(a, b) >= c:
            print("Impossible.")
        elif a == -1:
            a = ((c**2)-(b**2))**0.5
            print("a = {:.3f}".format(a))
        elif b == -1:
            b = ((c**2)-(a**2))**0.5
            print("b = {:.3f}".format(b))
    print()
