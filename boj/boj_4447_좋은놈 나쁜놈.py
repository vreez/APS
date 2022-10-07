import sys; sys.stdin = open("4447.txt", "r")

N = int(input())
for _ in range(N):
    arr = input()
    g = arr.count("g") + arr.count("G")
    b = arr.count("b") + arr.count("B")
    if g == b:
        print("{} is NEUTRAL".format(arr))
    elif g > b:
        print("{} is GOOD".format(arr))
    else:
        print("{} is A BADDY".format(arr))
