import sys; sys.stdin = open("30664.txt", "r")

while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num % 42 == 0:
            print("PREMIADO")
        else:
            print("TENTE NOVAMENTE")