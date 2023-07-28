import sys; sys.stdin = open("26340.txt", "r")

N = int(input())
for i in range(N):
    a, b, c = map(int, input().split())
    originA = a
    originB = b
    originC = c
    for j in range(c):
        if a > b:
            a = a//2
        else:
            b = b//2

    print("Data set: {} {} {}".format(originA, originB, originC))
    if a > b:
        print(a, b)
    else:
        print(b, a)
    print()


