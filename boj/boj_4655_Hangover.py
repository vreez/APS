import sys; sys.stdin = open("4655.txt", "r")

while True:
    n = float(input())
    if n == 0:
        break
    else:
        a = 2
        b = 0
        while b < n:
            b += 1/a
            a += 1
        print("{} card(s)".format(a-2))