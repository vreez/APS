import sys; sys.stdin = open("15178.txt", "r")

N = int(input())
for i in range(N):
    a, b, c = map(int, input().split())
    if a + b + c == 180:
        print("{} {} {} {}".format(a, b, c, "Seems OK"))
    else:
        print("{} {} {} {}".format(a, b, c, "Check"))
