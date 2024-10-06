import sys; sys.stdin = open("19813.txt", "r")

n = int(input())
for i in range(n):
    date = input()
    if "." in date:
        D, M, Y = map(int, date.split("."))
        print("{:02d}.{:02d}.{:04d}".format(D, M, Y), end=" ")
        print("{:02d}/{:02d}/{:04d}".format(M, D, Y))
    else:
        M, D, Y = map(int, date.split("/"))
        print("{:02d}.{:02d}.{:04d}".format(D, M, Y), end=" ")
        print("{:02d}/{:02d}/{:04d}".format(M, D, Y))