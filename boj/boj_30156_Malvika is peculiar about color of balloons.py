import sys; sys.stdin = open("30156.txt", "r")

n = int(input())
for i in range(n):
    balloon = list(input())
    a = balloon.count("a")
    b = balloon.count("b")
    if a == 0 or b == 0:
        print(0)
    else:
        if a > b:
            print(b)
        else:
            print(a)


