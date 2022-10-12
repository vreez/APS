import sys; sys.stdin = open("4504.txt", "r")

N = int(input())
while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num % N == 0:
            print("{} is a multiple of {}.".format(num, N))
        else:
            print("{} is NOT a multiple of {}.".format(num, N))