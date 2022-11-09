import sys; sys.stdin = open("10480.txt", "r")

N = int(input())
for i in range(N):
    num = int(input())
    if num % 2:
        print("{} is odd".format(num))
    else:
        print("{} is even".format(num))
