import sys; sys.stdin = open("4597.txt", "r")

while True:
    num = input()
    if num == "#":
        break
    else:
        n = num.count("1")
        if num[-1] =="e":
            if n % 2 == 0:
                num = num[:-1] + "0"
            else:
                num = num[:-1] + "1"
        else:
            if n % 2 == 0:
                num = num[:-1] + "1"
            else:
                num = num[:-1] + "0"
        print(num)
