import sys; sys.stdin = open("14182.txt", "r")

while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num <= 1000000:
            print(num)
        elif num > 1000000 and num <= 5000000:
            print(num//10*9)
        else:
            print(num//10*8)