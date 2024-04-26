import sys; sys.stdin = open("6378.txt", "r")

while True:
    num = input()
    if int(num) == 0:
        break
    else:
        while True:
            if len(num) == 1:
                break
            else:
                new = list(map(int, num))
                sumN = sum(new)
                num = str(sumN)
        print(num)