import sys; sys.stdin = open("2765.txt", "r")

N = 0
pi = 3.1415927
while True:
    a, b, c = map(float, input().split())
    N += 1
    if b == 0:
        break
    else:
        di = (a / 5280 / 12) * pi * b
        mph = di / (c / 3600)
        print("Trip #{}: {:.2f} {:.2f}".format(N, di, mph))