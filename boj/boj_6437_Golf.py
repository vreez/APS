import sys; sys.stdin = open("6437.txt", "r")
num = 0
while True:
    num += 1
    a, b = map(int, input().split())
    if a == b and a == 0:
        break
    else:
        print("Hole #{}".format(num))
        if b == 1:
            print("Hole-in-one.")
        elif a - b == 0:
            print("Par.")
        elif a - b == 1:
            print("Birdie.")
        elif a - b == -1:
            print("Bogey.")
        elif a - b == 2:
            print("Eagle.")
        elif a - b == 3:
            print("Double eagle.")
        elif a - b <= -2:
            print("Double Bogey.")
    print()
