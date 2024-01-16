import sys; sys.stdin = open("15340.txt", "r")

while True:
    c, d = map(int, input().split())
    if c == d and c == 0:
        break
    else:
        T = (c * 30) + (d * 40)
        C = (c * 35) + (d * 30)
        P = (c * 40) + (d * 20)
        arr = [T, C, P]
        print(min(arr))