import sys; sys.stdin = open("2145.txt", "r")

while True:
    num = input()
    if num == '0':
        break
    else:
        while True:
            if len(num) == 1:
                print(num)
                break
            else:
                num = str(sum(list(map(int, num))))
