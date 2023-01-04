import sys; sys.stdin = open("7595.txt", "r")

while True:
    num = int(input())
    if num == 0:
        break
    else:
        for i in range(1, num+1):
            print('*'*i)

