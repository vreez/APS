import sys; sys.stdin = open("6975.txt", "r")

N = int(input())
for i in range(N):
    num = int(input())
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        print("{} is a perfect number.".format(num))
    elif total < num:
        print("{} is a deficient number.".format(num))
    else:
        print("{} is an abundant number.".format(num))
    print()