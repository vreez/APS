import sys; sys.stdin = open("825.txt", "r")

while True:
    n = int(input())
    if n == -1:
        break
    else:
        if n % 3 == 0:
            print(n // 3)
