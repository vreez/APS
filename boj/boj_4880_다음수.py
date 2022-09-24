import sys; sys.stdin = open("4880.txt", "r")

while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == 0 and a1 == a2 and a2 == a3:
        break
    else:
        if a2 - a1 == a3 - a2:
            print("AP {}".format(a3 + (a3 - a2)))
        elif a2 // a1 == a3 // a2:
            print("GP {}".format(a3 * (a3 // a2)))