import sys; sys.stdin = open("1526.txt", "r")

N = int(input())

while True:
    btn = True
    for i in str(N):
        if i != '4' and i != '7':
            btn = False
            N -= 1
    if btn == True:
        print(N)
        break
