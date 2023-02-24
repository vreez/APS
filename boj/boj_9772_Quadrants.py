import sys; sys.stdin = open("9772.txt", "r")

while True:
    x, y = map(float, input().split())
    if x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif x > 0 and y < 0:
        print("Q4")
    elif x == 0 or y == 0:
        print("AXIS")
    if x == y and x == 0:
        break