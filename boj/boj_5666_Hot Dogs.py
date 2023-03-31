import sys; sys.stdin = open("5666.txt", "r")

while True:
    try:
        p, h = map(int, input().split())
        print("{:.2f}".format(p/h))
    except EOFError:
        break