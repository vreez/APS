import sys; sys.stdin = open("5086.txt", "r")

while True:
    a, b = map(int, input().split())
    if a == b and a == 0:
        break
    else:
        if a > b:
            if a % b == 0:
                print("multiple")
            else:
                print("neither")
        else:
            if b % a == 0:
                print("factor")
            else:
                print("neither")